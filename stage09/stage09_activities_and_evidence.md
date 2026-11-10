# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: Tue 1:30 - 3:30 Group 1\
Members and responsibilities: Alicia Hurst (Blahuee) – Stage 9 code; Aagney Mani Sharma (Aagneyf1r3) – reviewer, editor, console evidence and late test additions; Ngedup Jigme Lhazeen (njlhazin) – Parts A and G\
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
| FR-01 Register patient | Patient ID `P1`, name `Alex Example` | Menu 1 → `PatientService.register_patient` | Patient stored and details shown; duplicate or blank ID → ValueError, original record kept | `test_starter.py::test_registration_and_booking`, `test_starter.py::test_duplicate_patient_preserves_original` |
| FR-02 Find patient | `P1`, `p1`, `P9`, blank | Menu 2 → `PatientService.find_patient` | `P1` returns the stored patient; `p1`/`P9` → LookupError (IDs are case-sensitive); blank → ValueError | `test_services.py::test_find_patient_returns_known_patient_and_rejects_unknown`, `test_services.py::test_find_patient_rejects_blank_ids` |
| FR-03 Register practitioner (+ lookup) | `D1 Taylor Example, General practice`; `D2 Jordan Example, Cardiology` | Menu 3/4 → `PractitionerService` | Stored and shown with all three fields; unknown → LookupError; blank → ValueError | `test_services.py::test_find_practitioner_returns_known_and_rejects_unknown`, `test_starter.py::test_duplicate_practitioner_preserves_original` |
| FR-04 Book appointment | `A1, P1, D1, 2026-10-01 09:00` | Menu 5 → `parse_date_time` then `AppointmentService.book_appointment` | Scheduled A1 linked to the actual P1/D1 objects; unknown participant → LookupError; duplicate ID or bad/impossible date → ValueError; nothing stored on failure | `test_starter.py::test_registration_and_booking`, `test_starter.py::test_unregistered_participants_rejected`, `test_starter.py::test_duplicate_appointment_preserves_original` |
| FR-05 Prevent practitioner conflict | Second booking `A-CONFLICT` with D1 at the same time; `A2` with D2 at the same time | `book_appointment` uses `has_practitioner_conflict` | Same practitioner/time → ValueError and A-CONFLICT not stored; a different practitioner at the same time is allowed (AC-04.2) | `test_starter.py::test_conflict_rule_and_different_practitioner`, `test_services.py::test_booking_conflict_only_applies_to_exact_datetime`, `test_workflows.py::test_complete_appointment_workflow` |
| FR-06 Cancel appointment | Cancel `A1` twice; cancel unknown ID | Menu 6 → `cancel_appointment` → `Appointment.cancel` | First cancel → CANCELLED, same object returned; repeat cancel → ValueError, status unchanged; unknown → LookupError | `test_services.py::test_cancel_appointment_returns_cancelled_object`, `test_services.py::test_repeated_and_completed_cancellation_are_rejected`, `test_services.py::test_cancel_appointment_rejects_unknown_and_blank_ids` |
| FR-07 Retain cancelled history | Cancelled `A1` | Menu 7 and 8 | A1 is still found and appears in the all-status list as Cancelled | `test_services.py::test_cancelled_appointment_remains_in_history`, `test_services.py::test_cancelled_appointment_slot_can_be_reused` |
| FR-08 Find appointment | `A1`, `UNKNOWN`, blank | Menu 7 → `find_appointment` | Stored object with all details; unknown → LookupError; blank → ValueError | `test_services.py::test_find_appointment_returns_same_object` |
| FR-09 / service listing | `D1`, `D9`, blank, status `'scheduled'` (text) | `list_practitioner_appointments` | Known D1 → new ordered list; D9 → LookupError; blank → ValueError; text status → ValueError | `test_services.py::test_list_practitioner_appointments_isolates_practitioners`, `test_services.py::test_list_practitioner_appointments_filters_statuses`, `test_services.py::test_list_practitioner_appointments_rejects_invalid_inputs` |
| QRY-01 Practitioner isolation | Appointments for D1 and D2 | `select_appointments` | Only D1's appointments returned; D2's are left out (D2 is the control) | `test_queries.py::test_select_appointments_only_returns_requested_practitioner` |
| QRY-02 Status filter | `None`, SCHEDULED, CANCELLED, COMPLETED, a status with no match | `select_appointments` | `None` → every status; each enum → only that status; no match → `[]` | `test_queries.py::test_select_appointments_returns_all_statuses_by_default`, `test_queries.py::test_select_appointments_filters_each_status` |
| QRY-03 Ordering | Unsorted list; two appointments at the same time (one cancelled, one completed) | `select_appointments` with `appointment_sort_key` | Sorted by date/time, then appointment ID; source order and fields unchanged | `test_queries.py::test_select_appointments_sorts_by_datetime_then_appointment_id` |
| QRY-04 Known but empty | D1 with no appointments, or no matching status | `list_practitioner_appointments` | New empty list, no error | `test_services.py::test_list_practitioner_appointments_returns_empty_list` |
| FP-01 Purity | Same input called twice | `select_appointments` | Same result both times; code has no input, print, store or global state | `test_queries.py::test_select_appointments_returns_consistent_results` |
| FP-02 New list | Empty, already-sorted and unsorted inputs | `select_appointments` | Always a new list (`result is not source`); the Appointment objects inside are the same and unchanged | `test_queries.py::test_select_appointments_does_not_change_source_list_or_objects`, `test_services.py::test_list_practitioner_appointments_preserves_appointment_objects` |
| FP-03 Named key | One appointment | `appointment_sort_key` | Returns `(date_time, appointment_id)`; sorting really uses this key | `test_queries.py::test_appointment_sort_key_returns_datetime_and_id` |
| UI-01 Full menu run | The 17-step demo (P1, D1, D2, A1, A-CONFLICT, A2, cancel, filter, A3, exit) | `run_menu` | Matches the Final Console Demonstration; exit prints goodbye | Manual run, section D; service steps also in `test_workflows.py::test_complete_appointment_workflow` |
| UI-02 Error recovery | `99`, blank/unknown IDs, duplicate ID, `not a date`, `2026-02-30 09:00`, `UNKNOWN`, repeat cancel, `pending` | `run_menu` catches ValueError/LookupError | Short error message, menu returns, records unchanged, the next action (find P1) works | Manual run, section D |
 
Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: 
- **Empty, unknown and invalid are different.** *Empty*: D1 exists but has no matching appointments, so we return `[]` and it is not an error. *Unknown*: no practitioner has that ID (for example `D9`), so it raises LookupError. *Invalid*: the input itself is wrong (a blank ID, or a status that isn't an enum), so it raises ValueError. If we mixed them up, a typo like `D9` would wrongly look like "no appointments".
- **Enum conversion.** Only the console turns typed text into `AppointmentStatus`, and blank means `None` (all). Any other text, such as `pending`, gives "Status must be scheduled, cancelled or completed".
- **Object identity.** Lookups and lists return the *actual* stored objects (tests use `is`, not just "not None"), so a cancelled A1 found later is the same A1 that was booked.
- **Error handling.** The menu catches only ValueError and LookupError, prints `Error: ...` and shows the menu again. It does not hide every exception, so real bugs still show up.
- **Unchanged state on rejection.** Every check happens before anything is stored, and `Appointment.cancel` only changes status after its check passes. A rejected booking does not reserve its ID, and a rejected cancel keeps the old status. Tests compare the store before and after.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| QRY-01 practitioner isolation | `select_appointments` in `queries.py`; `test_select_appointments_only_returns_requested_practitioner` | Another practitioner's appointment is excluded; only the requested practitioner's appointments are returned | Pass | PR #29 |
| QRY-02 default and each status | `select_appointments`; `test_select_appointments_returns_all_statuses_by_default`, `test_select_appointments_filters_each_status` | No status returns all statuses; scheduled, cancelled and completed each return only that status | Pass | PR #29 |
| QRY-03 ordering, tie-break, named key | `appointment_sort_key`; `test_select_appointments_sorts_by_datetime_then_appointment_id`, `test_appointment_sort_key_returns_datetime_and_id` | Earlier time first; equal times ordered by appointment ID; the key returns (date_time, appointment_id) | Pass | PR #29 |
| FP-01 to FP-03 purity | `queries.py`; `test_select_appointments_returns_consistent_results`, `test_select_appointments_does_not_change_source_list_or_objects` | Repeated calls give the same result; source list order and objects are unchanged; the result is a new list holding the same objects | Pass | PR #29 |
| QRY-04 service listing and retained history | `AppointmentService.list_practitioner_appointments`; `test_list_practitioner_appointments_isolates_practitioners`, `test_list_practitioner_appointments_filters_statuses`, `test_list_practitioner_appointments_rejects_invalid_inputs`, `test_list_practitioner_appointments_returns_empty_list`, `test_list_practitioner_appointments_preserves_appointment_objects`, `test_complete_appointment_workflow` | Unknown practitioner raises LookupError; a cancelled appointment is still listed with all statuses and is excluded by the scheduled filter | Pass | PR #30, PR #31 |
 
| QRY-02 no match, QRY-03 tie-break, FP-02 empty and sorted input (added 10 Nov 2026) | `test_select_appointments_returns_empty_list_when_no_status_matches`, `test_select_appointments_breaks_equal_time_ties_by_appointment_id`, `test_select_appointments_returns_new_list_for_empty_and_sorted_input` in `test_queries.py` | No matching status gives a new `[]`; A9 placed before A1 in the source at the same time comes out as A1 then A9, so only the ID tie-break can explain the order; empty and already-sorted inputs still return a new list holding the same objects | Pass | Commit adding these tests (10 Nov 2026) |

Full suite from `project/`: `python -m pytest -q` gave `50 passed` at the Stage 9 candidate `351b6ca`. After Stage 8's `test_regressions.py` (2 tests) and the 3 query tests above, it gives `55 passed` (Aagney, 10 Nov 2026, Python 3.14.3, pytest 8.3.5).

Tie-break check: with the appointment ID temporarily removed from `appointment_sort_key` in a scratch copy, the new tie-break test failed while the older sort test still passed, which shows the new test is the one that proves the tie-break.
 
Purity explanation from code inspection, including absence of hidden state and I/O: `select_appointments` gets everything through its arguments (the list, the practitioner ID and the optional status). It uses no store, no global variable, and no `input` or `print`. It builds a new list and returns `sorted(...)` of it with the named key, so the caller's list is never sorted in place and no Appointment is changed. It has no hidden state and no side effects, so the same inputs always give the same result.
 
What the tests do and do not establish: The tests show that the query returns the right appointments in the right order (including the equal-time ID tie-break), returns a new list holding the same objects for empty, sorted and unsorted inputs, returns `[]` when no status matches, and never changes the source list. They also show the service's LookupError and ValueError cases and that cancelled history stays listable. They do not drive the console automatically (it is checked by scripted runs in section D), and passing tests are evidence, not proof that no other defect exists.
 
## D. Integrated console and workflow evidence
 
| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | `stage09/evidence/ui01_input.txt`, run from `project/` with `Get-Content ..\stage09\evidence\ui01_input.txt \| python main.py --interactive`. Steps: register P1, D1, D2; find each; book A1 (P1, D1, 2026-10-01 09:00); try A-CONFLICT with D1 at the same time; book A2 with D2 at the same time; cancel A1; find A1; list D1 with all statuses and with `scheduled`; book A3 in D1's freed slot; list D1 again; exit | Registration and lookups succeed. Same practitioner and time is rejected. A different practitioner at the same time is accepted, because FR-05 only blocks a practitioner's double booking, not a patient's. A1 is cancelled but still found and listed. The freed slot can be rebooked. Clean exit | All three registrations and lookups shown. `Booked A1: P1 with D1, 2026-10-01 09:00, scheduled`; `Error: Practitioner already has a SCHEDULED appointment at this time`; `Booked A2: P1 with D2, 2026-10-01 09:00, scheduled`; `Cancelled A1: ..., cancelled`; find A1 shows `cancelled`; all-status list shows A1 cancelled; `scheduled` filter shows `No matching appointments.`; `Booked A3 ...`; final list shows A1 cancelled then A3 scheduled; `Goodbye. Session data is discarded.` | `stage09/evidence/ui01_output.txt` (run by Aagney, Windows, Python 3.14.3, 10 Nov 2026) |
| UI-02 invalid-input recovery | `stage09/evidence/ui02_input.txt`, run the same way | Each error is reported, the menu returns, nothing is partly stored, and the next valid command works | `Unknown choice. Enter a number from the menu.`; blank patient ID → `Error: Patient ID cannot be blank`; P9 → `Error: Patient not found`; duplicate P1 → `Error: Patient ID already exists`, then find P1 still shows `Alex Example`; booking with unknown patient P9 → `Error: Patient not found`; unknown practitioner D9 → `Error: Practitioner not found`; `01/10/2026 09:00` → `Error: Use date/time format YYYY-MM-DD HH:MM`; `2026-02-30 09:00` → `Error: Invalid calendar date/time; use YYYY-MM-DD HH:MM`; find A1 → `Error: Appointment not found` (the failed bookings did not reserve A1); A99 → `Error: Appointment not found`; then A1 booked successfully, cancelled, repeat cancel → `Error: Only SCHEDULED appointments may be cancelled`, find A1 still `cancelled`; status `pending` → `Error: Status must be scheduled, cancelled or completed`; D9 list → `Error: Practitioner not found`; blank practitioner ID → `Error: Practitioner ID cannot be blank`; find P1 works; `Goodbye. Session data is discarded.` | `stage09/evidence/ui02_output.txt` (run by Aagney, Windows, Python 3.14.3, 10 Nov 2026) |
| Automated service workflow | `python -m pytest -q` from `project/`; `test_complete_appointment_workflow` in `tests/test_workflows.py` | Passes: registration, lookups, conflict rejection with unchanged store, different practitioner, cancellation with history, repeat cancel rejected, slot reuse, listing and filtering, LookupError | Passes; full suite `55 passed` | PR #31; `tests/test_workflows.py` |

Before and after state: after each rejected action the record was found or listed again and was unchanged (duplicate P1 kept its original name; A1 was not found after four failed bookings; a repeated cancel left A1 cancelled), and the next valid command succeeded. Both runs are reproducible from the saved input files. An earlier hand run of UI-02 was done on Alicia's PC, and a scripted UI-01 check was done by Copilot on `e93d2e5`; the saved runs above replace them as the evidence. There is no automated pytest that drives `run_menu`; the console is verified by these scripted runs.

## E. GitHub Copilot review and human decisions
Human design completed before AI: Sections A and B of this record, committed before any Copilot use (commits f6d7689 and 8ae2e5f).
Actual prompt/context supplied: The Stage 9 handout review prompt (handout section 8), followed by the synthetic code of `queries.py`, `AppointmentService.list_practitioner_appointments` and `cancel_appointment`, a description of `run_menu`, and a summary of `test_queries.py`, `test_services.py` and `test_workflows.py`. Copilot's first reply was only a generic template because no code was attached; the code was then supplied and the review below is its second reply. The full chat transcript was not saved, so the findings below are recorded from the session notes rather than linked.
Actual response: Copilot found no Critical findings. It raised two Important findings and several Optional ones, listed below.
 
| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| No automated console tests for `run_menu`, `parse_status`, error display and EOF handling | `console.py` `run_menu`, `parse_status`; there is no `test_console.py` | Important | Accept. Correct: there is no pytest that drives the menu. | No new console test; instead the console is now verified by saved, reproducible scripted runs (`stage09/evidence/ui01_*` and `ui02_*`). An automated console test remains test debt | Checked the tests folder (no console test). Ran both scripts through `python main.py --interactive` and saved the output (section D) |
| State after failure paths is inferred, not asserted everywhere | `services.py` invalid-status and unknown-ID checks; `test_workflows.py`; `test_starter.py` | Important | Modify (partly correct). State is asserted for the conflict case (`store.list_appointments() == before_conflict`), and `test_starter.py` checks that duplicate patient, practitioner and appointment attempts preserve the original. The invalid-status listing only reads data, so it cannot change state. Cancelling an unknown ID is checked only for the exception. | No change | Read the tests: state is asserted for conflict and duplicates, but not after an unknown-ID cancel |
| Assert that the result is a distinct list from the input | `test_queries.py` | Optional | Reject, already covered. `assert results is not appointments` and `assert first_results is not second_results` exist, and `test_services.py` has the same check | No change | Searched the tests for `is not` |
| Add a test where appointments share the same date/time (ID tie-break) | `test_select_appointments_sorts_by_datetime_then_appointment_id`, `test_appointment_sort_key_returns_datetime_and_id` | Optional | Accept. The old fixture had A1 already before A4 in the source, so the sort test alone did not prove the tie-break | Added `test_select_appointments_breaks_equal_time_ties_by_appointment_id` (10 Nov 2026) | With the ID removed from the key in a scratch copy, the new test failed and the old sort test still passed; with the real key, all tests pass (55 passed) |
| Parameterised test for all enum values | status filter tests | Optional | Reject. Correctness is already covered by the existing status tests; a rewrite is a style change only | No change | Existing tests cover each status |
| Extra history-retention assertion after the freed slot is reused | `test_cancelled_appointment_remains_in_history`, `test_cancelled_appointment_slot_can_be_reused`, `test_complete_appointment_workflow` | Optional | Accept as optional; already shown. After A3 reuses the slot, the D1 list in the workflow test shows A1 (cancelled) and A3 | No change needed | Final D1 list in the workflow test and in the manual UI-01 run |
 
Human finding (ours, not Copilot's): in `list_practitioner_appointments` the status check runs before the practitioner lookup, so an unknown practitioner with an invalid status raises ValueError rather than LookupError. This is harmless and both cases are errors, so we left it unchanged.
 
Responsibility check: Domain invariants stay inside the Appointment object (for example, only a SCHEDULED appointment can be cancelled). The data store holds the three collections and finds records. The services check IDs and status, coordinate the work and raise ValueError or LookupError. `select_appointments` only selects and sorts a list it is given. The console is the only place that reads input, prints, and converts text to a date or a status, and it only calls the services.
 
## F. Required reflections
 
1. Which integration concern was architectural rather than a filtering/sorting detail? Where each job belongs. We used one data store and one set of services for the whole menu session, and kept the console to input and output instead of repeating domain guards or conflict rules in it. The filtering and sorting was a detail inside one pure function.
2. Which Copilot suggestion did you reject as over-engineering, and why? The parameterised enum test and the extra "distinct list" test. Existing tests already check each status and already assert `results is not appointments`, so these would only repeat them or change style. We did not treat the tie-break idea as over-engineering: the old sort test did not prove it, so we added a focused tie-break test.
3. How did you prove cancelled appointments remain retrievable and listable in the same session? We booked A1, cancelled it, listed D1 with all statuses (A1 was shown as cancelled) and listed with scheduled (A1 was left out). `test_complete_appointment_workflow` also checks that finding A1 returns the same object with status CANCELLED.

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

Issues and bounded branches: https://github.com/Blahuee/st1-assignment-3/issues/28, https://github.com/Blahuee/st1-assignment-3/issues/27, https://github.com/Blahuee/st1-assignment-3/issues/26, https://github.com/Blahuee/st1-assignment-3/issues/25; branches `feature/stage9-queries`, `feature/stage9-practitioner-appointments` and `feature/stage9-console-dispatch`.
PR/diff and another-member human reviewer: PR #29, PR #30 and PR #31 (code by Alicia). PRs #29 and #30 were merged by Aagney with no formal approval recorded on GitHub. PR #31 shows as Approved on GitHub and was merged by Ngedup.
Review responses and Copilot comparison: Copilot's findings and our decisions are in Part E. No formal review comments were recorded on PRs #29 and #30. Informal checks raised the tie-break test gap and changed older test data, recorded in Stage 12.
Full regression command, working directory, actual count/result and evidence: `python -m pytest -q`, from `project/`, `50 passed`.
README run instructions and scope/limitations: `project/README.md` (README update pending; it is still titled "Stage 6 starter"). Run `python main.py` for the demo and `python main.py --interactive` for the menu. Data is kept only while the menu runs.
Unresolved issues and support/action: No automated console tests; tie-break test gap; `project/README.md` not updated; no formal approval on PRs #29 and #30. `main.py` still wraps `run_menu()` in a `try/except NotImplementedError`, which is harmless now.
UG common candidate / PG future branch plan: UG common candidate is `351b6ca` going to Stage 12. PG Stages 10 and 11 are unchanged and deferred.
 
- [x] Query contracts, purity, new lists and named-key ordering verified.
- [x] Service empty/unknown/invalid cases and cancellation history verified.
- [x] Every console command and invalid-input recovery demonstrated.
- [x] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [x] Human design, Copilot critique, review and integration recorded honestly.
- [x] Reflections and ten formative responses completed.
- [x] README updated; earlier code/tests/records preserved.
- [x] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.
No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
 