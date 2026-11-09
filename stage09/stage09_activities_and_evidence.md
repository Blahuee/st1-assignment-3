# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: 1:30 - 3:30\
Members and responsibilities: Alicia Hurst (Blahuee) - STage 9 Code; Aagney Mani Sharma (Aagneyf1r3) – Reviewer and Editor; Ngedup Jigme Lhazeen (njlhazin) – Part A and G\
Stage 8 integrated SHA: `a8c7d01c1f6a2cf26b8bd089c234c7023f194290`\
 Working directory: `project/`\
Result: `37 passed in 0.03s`
  
## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity |Required session/domain state |FR-01 AND FR-02 must be registered once and found later by the same ID. Appointments link to that actual patient object. |
| Appointment history |Required session/domain state  | FR-07: cancelled appointments are kept and can still be found and listed in the same session. |
| Temporary menu choice |Transient | only decides which command runs this time round the loop, nothing needs it afterwards. |
| Practitioner specialty | Required session/domain state | FR-03: stored with the practitioner and available when the practitioner is found. |
| Debug print output | Transient|Only helps a developer while testing, it is not part of the system's data and should not be kept. |
| Appointment status | Required session/domain state | FR-06 AND FR-07- shows Scheduled, Cancelled or Completed. Conflict checks and status filters depend on it.|

What is intentionally lost on exit? Everything. Patients, practitioners and appointments (including cancelled history) live only in the in-memory SmartCareDataStore, so they are discarded when the program exits and a new launch starts empty. This is the declared scope (FR-10 restart persistence is retired), not a bug.

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key | appointment: Appointment | tuple[datetime, str] (date_time, appointment_id) | Gives one reusable ordering rule: earliest time first, then appointment ID to break ties. No validation, no side effects. | Appointment.date_time and appointment_id properties (read-only) |
| select_appointments | `appointments: list[Appointment]`, `practitioner_id: str`, `status: AppointmentStatus \| None = None` | New list[Appointment] sorted with appointment_sort_key | Pure: keeps only this practitioner's appointments, optionally one status; never changes the input list or objects; no input/print/store. | Appointment.practitioner.practitioner_id and AppointmentStatus enum. |
| Service listing | `practitioner_id: str`, `status: AppointmentStatus \| None = None` | New ordered list (may be empty) | AppointmentService checks the practitioner exists (LookupError), blank ID (ValueError), non-enum status (ValueError), gets a fresh list from the store, then calls select_appointments. | SmartCareDataStore.find_practitioner / list_appointments contracts. |
| Console | Typed text from the user | Printed messages and details | run_menu reads input, converts text (date/time with parse_date_time, status text to enum), calls services, prints results, and catches ValueError/LookupError so the menu continues. | Uses one data store and one set of services for the whole session. |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: Patient and Practitioner IDs are trimmed, non-blank, case-sensitive and read-only; names and specialty must be non-blank (domain.py `required_text`). An Appointment holds the actual registered Patient and Practitioner objects (not copies or just IDs), a minute-precision date_time, and a status that only changes through guarded methods such as `cancel()`. The store rejects duplicate IDs and unregistered participants. The listing and query only read these properties; they add no new fields.

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input | A domain object is doing console work (asking "Confirm?"), so it cannot be tested or reused without a keyboard. | Appointment.cancel only checks the SCHEDULED rule and changes status. Any confirmation belongs in the console. |
| Service prints/reads the menu | The service mixes user interface with business coordination, so tests and other interfaces can't use it cleanly. | Services take values and return objects or raise errors; run_menu in console.py prints and reads. |
| Query sorts its source in place | appointments.sort() changes the caller's list, a hidden side effect, so the function is no longer pure. | Use sorted(...) to return a new list and leave the source unchanged. |
| Store prints Appointment saved | Storage is doing output. Callers can't check the result and the message appears even in tests. | The store just stores and returns (or raises an error); the console decides what message to show. |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: appointments.sort(key=appointment_sort_key) changes the order of the source list itself and returns None. result = sorted(appointments, key=appointment_sort_key) leaves the source order unchanged and returns a new list, so result is not appointments; it still holds the same Appointment objects. Mutation check: before calling, save a snapshot such as [(a.appointment_id, a.date_time, a.status) for a in appointments]; after the call, assert the source still equals that snapshot (same order and fields). Checking only len() is not enough, because sorting in place keeps the same length.

Score-example prediction and explanation of passing the named key: sorted(scores, key=score_key) returns a new list ordered by score and then by name for equal scores, and scores keeps its original order. We pass the function name score_key without brackets, so sorted can call it once for each item. Writing score_key() would call it straight away and fail. Using a named key means the same ordering rule is written once, can be tested on its own, and is reused everywhere.

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion:Cancelling changes the status of the same Appointment object to CANCELLED and keeps it in the store, because FR-07 needs the history kept. Deleting would lose that record. Checks: (1) after cancelling A1, find_appointment("A1") returns the same object with status CANCELLED; (2) listing D1 with no status includes A1 as Cancelled; (3) listing D1 with SCHEDULED leaves A1 out, because that filter should only show scheduled appointments. Cancelling also frees the slot, so a new A3 can be booked with D1 at the same time.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: 
- **Keep the query pure.** `select_appointments` gets everything through its arguments (a list, a practitioner ID, an optional status) and returns a new list. It never uses the store, input or print. Then it can be tested on its own, and calling it twice gives the same answer.
- **The service does the checking, the query does the selecting.** `list_practitioner_appointments` checks that the practitioner exists and the status is valid, gets a fresh list from `data_store.list_appointments()`, then calls the query. It passes the *stored* practitioner's ID, so an accepted ID like `" D1 "` still matches.
- **Status text becomes an enum only in the console.** The menu turns `scheduled` / `cancelled` / `completed` into `AppointmentStatus`, and blank means all statuses. Service callers must pass an enum or `None`; text like `'scheduled'` raises ValueError rather than quietly returning nothing.
- **One store for the whole session.** `run_menu` creates one `SmartCareDataStore` and one set of services before the loop, so records last until exit. It reuses `parse_date_time` and `format_appointment` rather than writing new ones.
- **Cancel, never delete.** Cancelling keeps the same Appointment object with status CANCELLED, so the history stays (FR-07).

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| FR-01 Register patient | Patient ID `P1`, name `Alex Example` | Menu 1 → `PatientService.register_patient` | Patient stored and details shown; duplicate or blank ID → ValueError, original record kept | <!-- test ID / link --> |
| FR-02 Find patient | `P1`, `p1`, `P9`, blank | Menu 2 → `PatientService.find_patient` | `P1` returns the stored patient; `p1`/`P9` → LookupError (IDs are case-sensitive); blank → ValueError | <!-- test ID / link --> |
| FR-03 Register practitioner (+ lookup) | `D1 Taylor Example, General practice`; `D2 Jordan Example, Cardiology` | Menu 3/4 → `PractitionerService` | Stored and shown with all three fields; unknown → LookupError; blank → ValueError | <!-- test ID / link --> |
| FR-04 Book appointment | `A1, P1, D1, 2026-10-01 09:00` | Menu 5 → `parse_date_time` then `AppointmentService.book_appointment` | Scheduled A1 linked to the actual P1/D1 objects; unknown participant → LookupError; duplicate ID or bad/impossible date → ValueError; nothing stored on failure | <!-- test ID / link --> |
| FR-05 Prevent practitioner conflict | Second booking `A-CONFLICT` with D1 at the same time; `A2` with D2 at the same time | `book_appointment` uses `has_practitioner_conflict` | Same practitioner/time → ValueError and A-CONFLICT not stored; a different practitioner at the same time is allowed (AC-04.2) | <!-- test ID / link --> |
| FR-06 Cancel appointment | Cancel `A1` twice; cancel unknown ID | Menu 6 → `cancel_appointment` → `Appointment.cancel` | First cancel → CANCELLED, same object returned; repeat cancel → ValueError, status unchanged; unknown → LookupError | <!-- test ID / link --> |
| FR-07 Retain cancelled history | Cancelled `A1` | Menu 7 and 8 | A1 is still found and appears in the all-status list as Cancelled | <!-- test ID / link --> |
| FR-08 Find appointment | `A1`, `UNKNOWN`, blank | Menu 7 → `find_appointment` | Stored object with all details; unknown → LookupError; blank → ValueError | <!-- test ID / link --> |
| FR-09 / service listing | `D1`, `D9`, blank, status `'scheduled'` (text) | `list_practitioner_appointments` | Known D1 → new ordered list; D9 → LookupError; blank → ValueError; text status → ValueError | <!-- test ID / link --> |
| QRY-01 Practitioner isolation | Appointments for D1 and D2 | `select_appointments` | Only D1's appointments returned; D2's are left out (D2 is the control) | <!-- test ID / link --> |
| QRY-02 Status filter | `None`, SCHEDULED, CANCELLED, COMPLETED, a status with no match | `select_appointments` | `None` → every status; each enum → only that status; no match → `[]` | <!-- test ID / link --> |
| QRY-03 Ordering | Unsorted list; two appointments at the same time (one cancelled, one completed) | `select_appointments` with `appointment_sort_key` | Sorted by date/time, then appointment ID; source order and fields unchanged | <!-- test ID / link --> |
| QRY-04 Known but empty | D1 with no appointments, or no matching status | `list_practitioner_appointments` | New empty list, no error | <!-- test ID / link --> |
| FP-01 Purity | Same input called twice | `select_appointments` | Same result both times; code has no input, print, store or global state | <!-- test ID / link --> |
| FP-02 New list | Empty, already-sorted and unsorted inputs | `select_appointments` | Always a new list (`result is not source`); the Appointment objects inside are the same and unchanged | <!-- test ID / link --> |
| FP-03 Named key | One appointment | `appointment_sort_key` | Returns `(date_time, appointment_id)`; sorting really uses this key | <!-- test ID / link --> |
| UI-01 Full menu run | The 17-step demo (P1, D1, D2, A1, A-CONFLICT, A2, cancel, filter, A3, exit) | `run_menu` | Matches the Final Console Demonstration; exit prints goodbye | <!-- evidence link --> |
| UI-02 Error recovery | `99`, blank/unknown IDs, duplicate ID, `not a date`, `2026-02-30 09:00`, `UNKNOWN`, repeat cancel, `pending` | `run_menu` catches ValueError/LookupError | Short error message, menu returns, records unchanged, the next action (find P1) works | <!-- evidence link --> |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: 
- **Empty, unknown and invalid are different.** *Empty*: D1 exists but has no matching appointments, so we return `[]` and it is not an error. *Unknown*: no practitioner has that ID (for example `D9`), so it raises LookupError. *Invalid*: the input itself is wrong (a blank ID, or a status that isn't an enum), so it raises ValueError. If we mixed them up, a typo like `D9` would wrongly look like "no appointments".
- **Enum conversion.** Only the console turns typed text into `AppointmentStatus`, and blank means `None` (all). Any other text, such as `pending`, gives "Status must be scheduled, cancelled or completed".
- **Object identity.** Lookups and lists return the *actual* stored objects (tests use `is`, not just "not None"), so a cancelled A1 found later is the same A1 that was booked.
- **Error handling.** The menu catches only ValueError and LookupError, prints `Error: ...` and shows the menu again. It does not hide every exception, so real bugs still show up.
- **Unchanged state on rejection.** Every check happens before anything is stored, and `Appointment.cancel` only changes status after its check passes. A rejected booking does not reserve its ID, and a rejected cancel keeps the old status. Tests compare the store before and after.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| | | | | |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- response -->
What the tests do and do not establish: <!-- response -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | | | | |
| UI-02 invalid-input recovery | | | | |
| Automated service workflow | | | | |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- reference -->
Actual prompt/context supplied: <!-- paste or accessible reference -->
Actual response: <!-- accessible reference -->

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| | | | | | |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? It only reads its inputs and returns a new list. It does no input or printing, does not use the store, has no hidden state, and changes no list or object, so the same inputs give the same result. Sorting the source in place, printing or cnacelling an appointment would break purity. 
2. Which explicit inputs are needed, and why avoid a global store? The appointment list, the practitioner ID and an optional status. A global store would be hidden input, making results harder to predict and test.
3. How can a new list reuse Appointment objects safely? The list is new but holds the same Appointment objects. This is safe because the query only reads them and never changes them.
4. Why use a named key, and what breaks equal-time ties? A named key (appointment_sort_key) writes the sorting rule once, so it can be tested on its own and reused. It returns (date_time, appointment_id), so appointments are sorted by time first. If two have the same time, the appointment ID breaks the tie, so A1 comes before A3 at 09:00.
5. How do default and explicit status filters differ? The default (status None, or blank in the menu) shows every status: Scheduled, Cancelled and Completed. This shows the full history. An explicit status shows only that status, so a cancelled A1 is left out when you filter by Scheduled.
6. How do empty, unknown practitioner and invalid filter cases differ? Empty means the practitioner exists but has no matching appointments, so it returns [] and the menu shows "No appointments found." Unknown means no practitioner has that ID (for example D9), so it raises LookupError. Invalid means the status isn't scheduled, cancelled or completed (for example "pending"), so it raises ValueError.
7. Which console errors recover, and how is unchanged state checked? Bad menu choice, bad/unknown/duplicate IDs, bad date, conflicts, repeat cancel and invalid status all show an error and return to the menu. We check by finding or listing the records afterwards to see nothing changed.
8. What is data integrity for registered participants, conflicts and history? Appointments link to real registered patients and practitioners, a practitioner can't be double-booked, and cancelled appointments are kept. Failed actions change nothing.
9. What is Copilot's review role, and who verifies findings? Copilot suggests possible problems or improvements after our group has done its own design and review. It does not run tests, approve merges or replace a teammate's review. We check each suggestion against the requirements, the code and our own test run, then record Accept, Modify or Reject with a reason.
10. How do pure functions and OOP responsibilities work together? Each part has one job. The Appointment object protects its own rules (like only cancelling Scheduled), the store holds the data, and the services check input and coordinate the work. The pure query just selects and sorts the list it is given, and the console handles input and output.

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
