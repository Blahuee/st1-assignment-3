# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: 1:30 - 3:30\
Members and responsibilities: Alicia Hurst (Blahuee) Aagney Mani Sharma (Aagneyf1r3) – <!-- complete -->; Ngedup Jigme Lhazeen (njlhazin) – <!-- complete -->
Stage 8 integrated SHA, command, working directory and actual result: <!-- complete -->

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity |Required session/domain state |FR-01 AND FR-02 must be registered once and found later by the same ID. Appointments link to that actual patient object. |
| Appointment history |Required session/domain state  | FR-07: cancelled appointments are kept and can still be found and listed in the same session. |
| Temporary menu choice |Transient | only decides which command runs this time round the loop, nothing needs it afterwards. |
| Practitioner specialty | Required session/domain state |FR-03: stored witht the practitioner and shown when finding the practitioner or an appointment. |
| Debug print output | Transient|Only helps a developer while testing, it is not part of the system's data and should not be kept. |
| Appointment status | Required session/domain state | FR-06 AND FR-07- shows Scheduled, Cancelled or Completed. Conflict checks and status filters depend on it.|

What is intentionally lost on exit? Everything. Petients, practitioners and appointments (including cancelled hsitory) live only in the in-memory SmartCareDataStore, so they are discarded when the program exits and a new launch starts empty. This is the declared scope (FR-10 restart persistance is retired), not a bug. 

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key |appointment: Appointment |tuple[date_time, appointment_id] |Gives one reusable ordering ruke: earlist time first, then apppointment ID to break ties. No validation, no side effects. |Appointment.date_time and appointment_id properties (read-only) |
| select_appointments | appointments: list[Appointment], practitioner_id: str, status: AppointmentStatus None = None| New list[Appointment] sorted with appointment_sort_key|Pure: keeps only this practitioner's appointments, optionally one status; never changes the input list or objects; no input/print/store. | Appointment.practitioner.practitioner_id and AppointmentStatus enum.|
| Service listing | `practitioner_id: str`, `status: AppointmentStatus \| None = None` | New ordered list (may be empty) | AppointmentService checks the practitioner exists (LookupError), blank ID (ValueError), non-enum status (ValueError), gets a fresh list from the store, then calls select_appointments. | SmartCareDataStore.find_practitioner / list_appointments contracts. |
| Console | Typed text from the user | Printed messages and details | run_menu reads input, converts text (date/time with parse_date_time, status text to enum), calls services, prints results, and catches ValueError/LookupError so the menu continues. | Uses one data store and one set of services for the whole session. |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: Patient and Practitioner IDs are trimmed, non-blank, case-sensitive and read-only; names and specialty must be non-blank (domain.py `required_text`). An Appointment holds the actual registered Patient and Practitioner objects (not copies or just IDs), a minute-precision date_time, and a status that only changes through guarded methods such as `cancel()`. The store rejects duplicate IDs and unregistered participants. The listing and query only read these properties; they add no new fields.

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input | A domain object is doing console work (asking "Confirm?"), so it cannot be tessted or reused without a keyboard.|Appointment.cancel only checks the SCHEDULED rule and changes status. Any confirmation belongs in the console.  |
| Service prints/reads the menu |The service mizes user interface with business coordination, so tests and other interfaces can't use it cleanly. |Services take values and return objects or raise errors; run_menu in console.py prints and reads. |
| Query sorts its source in place | appointments.sort() changes the caller's list, a hidden side effect, so the function is no longer pure. |use sorted (...) to return a new list and leave the source unchanged. |
| Store prints Appointment saved |sotrage is doing output. callers can't check the result and the mssage appears even in tests.  |The store just stores and returns (or raises an erroe); the console decides what message to show. |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: appointments.sort(key=appointment_sort_key) changes the order of the source list itself and returns None. result = sorted(appointments, key=appointment_sort_key) leaves the source order unchanged and returns a new list, so result is not appointments; it still holds the same Appointment objects. Mutation check: before calling, save a snapshot such as [(a.appointment_id, a.date_time, a.status) for a in appointments]; after the call, assert the source still equals that snapshot (same order and fields). Checking only len() is not enough, because sorting in place keeps the same length.

Score-example prediction and explanation of passing the named key: sorted(scores, key=score_key) returns a new list ordered by score and then by name for equal scores, and scores keeps its original order. We pass the function name score_key without brackets, so sorted can call it once for each item. Writing score_key() would call it straight away and fail. Using a named key means the same ordering rule is written once, can be tested on its own, and is reused everywhere.

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion:Cancelling changes the status of the same Appointment object to CANCELLED and keeps it in the store, because FR-07 needs the history kept. Deleting would lose that record. Checks: (1) after cancelling A1, find_appointment("A1") returns the same object with status CANCELLED; (2) listing D1 with no status includes A1 as Cancelled; (3) listing D1 with SCHEDULED leaves A1 out, because that filter should only show scheduled appointments. Cancelling also frees the slot, so a new A3 can be booked with D1 at the same time.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: <!-- response -->

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| | | | | |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: <!-- response -->

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

1. What makes select_appointments pure, and what side effect breaks purity? <!-- response -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

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
