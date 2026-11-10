# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: 1:30 - 3:30\
Members and responsibilities: Alicia Hurst (Blahuee) - STage 9 Code; Aagney Mani Sharma (Aagneyf1r3) – Reviewer and Editor; Ngedup Jigme Lhazeen (njlhazin) – Part A, B, C, D, E, F, G, AND H\
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
 
Full suite from `project/`: `python -m pytest -q` gave `50 passed`.
 
Purity explanation from code inspection, including absence of hidden state and I/O: `select_appointments` gets everything through its arguments (the list, the practitioner ID and the optional status). It uses no store, no global variable, and no `input` or `print`. It builds a new list and returns `sorted(...)` of it with the named key, so the caller's list is never sorted in place and no Appointment is changed. It has no hidden state and no side effects, so the same inputs always give the same result.
 
What the tests do and do not establish: The tests show that the query returns the right appointments in the right order, as a new list holding the same objects, and that the source list is not changed. They also show the LookupError case and that cancelled history stays listable. They do not prove behaviour for very large lists or for typed console input (the console is checked separately in section D), and passing tests are evidence, not proof that no other defect exists.
 
## D. Integrated console and workflow evidence
 
| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | From `project/`: `python main.py --interactive`, then: `1` P1 "Alex Example"; `3` D1 "Taylor Example" "General practice"; `3` D2 "Jordan Example" "Physio"; `5` A1 P1 D1 `2026-10-01 09:00`; `5` A2 P1 D1 same time; `5` A2 P1 D2 same time; `6` A1; `8` D1 blank; `8` D1 `scheduled`; `5` A3 P1 D1 same time; `8` D1 blank; `0` | Registration and booking succeed. The same practitioner and time is rejected. A different practitioner at the same time is accepted. A1 is cancelled but still listed. The freed slot can be rebooked. Clean exit |  `Booked A1: P1 with D1, 2026-10-01 09:00, scheduled`; `Error: Practitioner already has a SCHEDULED appointment at this time`; `Booked A2: P1 with D2, ...`; `Cancelled A1: ..., cancelled`; D1 all-status list shows A1 cancelled; the scheduled filter shows `No matching appointments.`; `Booked A3 ...`; final D1 list shows A1 cancelled and A3 scheduled; `Goodbye. Session data is discarded.` | **[terminal output file or link]** |
| UI-02 invalid-input recovery | From `project/`: `python main.py --interactive`, then: `9`; `2` P5; `1` P1 "Hello World"; `1` P1 "Hello James"; `5` A1 P5 D2 `01/10/2026 09:00`; `5` A5 P1 D2 `2026-13-40 25:90`; `7` A7; `7` A1; `4` D1; `3` D1 "Dr. Jones" "Specialty"; `5` A1 P1 D1 `2026-10-01 09:00`; `6` A1; `6` A1; `8` D1 `pending`; `0` | Each error is reported and the menu returns. A failed action stores nothing. The next valid command works | `Unknown choice. Enter a number from the menu.` `Error: Patient not found` (find P5). `Error: Patient ID already exists` (duplicate P1). `Error: Use date/time format YYYY-MM-DD HH:MM` (`01/10/2026 09:00`). `Error: Invalid calendar date/time; use YYYY-MM-DD HH:MM` (`2026-13-40 25:90`). `Error: Appointment not found` (A7, and A1 after the failed bookings, so no booking was stored). `Error: Practitioner not found` (D1 before registering). Then D1 was registered and `Booked A1: P1 with D1, 2026-10-01 09:00, scheduled` worked. `Cancelled A1: ..., cancelled`, then `Error: Only SCHEDULED appointments may be cancelled`. `Error: Status must be scheduled, cancelled or completed`. `Goodbye. Session data is discarded.` | Terminal output of this run (run on Alicia's PC): **[attach file or paste]** |
| Automated service workflow | `python -m pytest -q` from `project/`; test `test_complete_appointment_workflow` in `tests/test_workflows.py` | Passes: registration, lookups, conflict rejection, different practitioner, cancellation with history, repeat cancel rejected, slot reuse, listing and filtering, LookupError | `50 passed` for the full suite | PR #31 |
 
Before and after state: after each rejected action the record was found or listed again and was unchanged (for example A1 was not found after the failed bookings), and the next valid command succeeded. The console itself was demonstrated by hand. There is no automated test that drives `run_menu` with scripted input. The UI-02 run did not enter a blank ID, an unknown participant on booking, or an unknown practitioner when listing, so those cases are not claimed here.

## E. GitHub Copilot review and human decisions
Human design completed before AI: Sections A and B of this record, committed before any Copilot use (commits f6d7689 and 8ae2e5f).
Actual prompt/context supplied: The Stage 9 handout review prompt, followed by the synthetic code of `queries.py`, `AppointmentService.list_practitioner_appointments` and `cancel_appointment`, a description of `run_menu`, and a summary of `test_queries.py`, `test_services.py` and `test_workflows.py`. (Copilot's first reply was only a generic template because no code was attached; the code was then supplied and the review below is its second reply.) 
"Here is the code and test evidence. Please now give a concrete review using the same rules (Critical / Important / Optional, with the code or test to check for each finding, separating observed evidence from optional improvements). Do not redesign the domain or add storage/frameworks.
<br>
queries.py:
```python
def appointment_sort_key(appointment):
    return appointment.date_time, appointment.appointment_id
<br>
def select_appointments(appointments, practitioner_id, status=None):
    selected = []
    for appointment in appointments:
        if appointment.practitioner.practitioner_id != practitioner_id:
            continue
        if status is not None and appointment.status is not status:
            continue
        selected.append(appointment)
    return sorted(selected, key=appointment_sort_key)
<br>
services.py (AppointmentService):
```python
def list_practitioner_appointments(self, practitioner_id, status=None):
    if status is not None and not isinstance(status, AppointmentStatus):
        raise ValueError('Invalid appointment status')
    practitioner = self.data_store.find_practitioner(practitioner_id)
    if practitioner is None:
        raise LookupError('Practitioner not found')
    appointments = self.data_store.list_appointments()
    return select_appointments(appointments, practitioner.practitioner_id, status)
<br>
def cancel_appointment(self, appointment_id):
    appointment = self.data_store.find_appointment(appointment_id)
    if appointment is None:
        raise LookupError('Appointment not found')
    appointment.cancel()
    return appointment
```
<br>
console.py: run_menu creates one SmartCareDataStore and one set of services before a `while True` loop. Each command calls a service. Only (ValueError, LookupError) are caught and printed as "Error: ...". A bad date is rejected by parse_date_time before booking. EOFError ends the session. Choice 8 uses parse_status (blank means all, otherwise scheduled/cancelled/completed else ValueError).
<br>
Tests: test_queries.py (7 tests: practitioner isolation, all statuses by default, each status, sorting by date then ID, consistent results, no mutation of the source list or objects, sort key value); test_services.py (listing isolation, status filters, invalid input, empty list, same objects preserved, cancelled history and slot reuse); test_workflows.py (one service workflow: register, book, conflict rejected, different practitioner, cancel, second cancel rejected, slot reuse, list with and without status filter, LookupError). run_menu itself has no automated tests; it was tried by hand. 50 tests pass."

Actual response: Copilot found no Critical findings. It raised two Important findings and several Optional ones, listed below. SmartCare Review

Scope reviewed:

queries.py
AppointmentService.list_practitioner_appointments()
AppointmentService.cancel_appointment()
Console integration description
Tests in test_queries.py, test_services.py, and test_workflows.py

Findings are separated into Observed Evidence and Optional Improvements.

Critical Findings
None observed

Based on the supplied code and tests, I did not find evidence of:

partial state updates on failed cancellation;
deletion of cancelled appointments;
identity replacement during queries;
invalid status filtering;
loss of appointment history.

The existing tests specifically exercise cancellation history retention, second-cancel rejection, slot reuse, lookup failures, and status-filtered listing.

Important Findings
1. Console layer has no automated integration tests
Observed evidence

You state:

run_menu itself has no automated tests; it was tried by hand.

The console contains responsibility for:

parsing menu choices;
handling ValueError;
handling LookupError;
EOF session termination;
status parsing ("scheduled/cancelled/completed");
dispatching calls to services.

These behaviours are not covered by automated tests even though they affect user-visible workflow outcomes.

Code/Test evidence to check

console.py:

run_menu
choice handling
exception handling
parse_status
EOF handling

Test suite:

absence of test_console.py
absence of automated menu-flow tests
Risk

Manual verification is difficult to repeat and can miss regressions in:

command routing;
error recovery;
input validation.
2. Recovery behaviour is only indirectly tested through workflows
Observed evidence

Workflow tests verify:

conflict rejection;
lookup failures;
second cancel rejection.

However, the supplied evidence does not show tests proving state remains unchanged after every failure path.

For example, no test evidence was listed that explicitly captures state before and after:

invalid status passed to list_practitioner_appointments;
appointment lookup failures in cancellation.
Code/Test evidence to check

services.py

if status is not None and not isinstance(status, AppointmentStatus):
    raise ValueError(...)

if appointment is None:
    raise LookupError(...)


Check whether tests explicitly verify:

appointment collection unchanged after exceptions;
history unchanged after exceptions.
Risk

Current implementation appears safe, but preservation of state during failure is inferred rather than directly asserted.

Optional Findings
1. Query purity coverage is strong
Observed evidence

The supplied tests include:

no mutation of source list;
no mutation of source objects;
consistent repeated results.

This directly supports the requirement for:

explicit inputs;
query purity;
source non-mutation.
Code/Test evidence checked

select_appointments

selected = []
...
selected.append(appointment)
return sorted(selected, key=appointment_sort_key)


and the tests covering:

no source-list mutation;
no object mutation;
consistent results.
Optional improvement

Add an assertion that the returned list itself is a distinct list instance from the input list if not already present.

2. Object identity preservation is well covered
Observed evidence

The implementation returns existing appointment objects.

selected.append(appointment)


No copying, recreation, or mapping occurs.

You also report service tests covering:

same objects preserved

Code/Test evidence checked

queries.py

selected.append(appointment)


test_services.py

same object preservation test
Optional improvement

None required for the supplied requirements.

3. Enum filtering implementation appears correct
Observed evidence

Filtering is performed using enum identity:

if status is not None and appointment.status is not status:
    continue


Service validation ensures:

isinstance(status, AppointmentStatus)


and reported tests cover:

each status;
service status filters;
blank status meaning all.
Code/Test evidence checked
select_appointments
list_practitioner_appointments
status filtering tests
Optional improvement

A parameterized test covering all enum values in one test case could reduce duplication, but correctness already appears covered.

4. Ordering requirements appear satisfied
Observed evidence

Sorting is centralized:

def appointment_sort_key(appointment):
    return appointment.date_time, appointment.appointment_id


and selection returns:

return sorted(selected, key=appointment_sort_key)


The test suite reportedly includes:

sorting by date then ID;
sort-key verification.
Code/Test evidence checked

appointment_sort_key

and query sorting tests.

Optional improvement

Add a test where multiple appointments share exactly the same datetime to verify deterministic ID ordering at that boundary.

5. Retained-history behaviour appears covered
Observed evidence

Cancellation does not remove records:

appointment.cancel()
return appointment


There is no deletion logic shown.

The tests reportedly cover:

cancelled history;
slot reuse;
cancelled status filtering;
workflow cancellation.
Code/Test evidence checked

cancel_appointment

and tests:

cancelled history
slot reuse
workflow cancellation sequence
Optional improvement

Add an explicit assertion that a cancelled appointment remains discoverable through history-oriented listing after additional appointments are created in the released slot.

The behaviour likely exists already, but this is a useful integrity regression test.

Missing Test Coverage
Important
Console tests

Recommended automated coverage for:

valid menu choice dispatch;
invalid menu choice recovery;
ValueError display path;
LookupError display path;
parse_status("") meaning all statuses;
invalid status text;
EOF session termination.
Optional
Additional recovery assertions

For exception paths, explicitly verify:

appointment count unchanged;
appointment identities unchanged;
historical appointments unchanged.
Overall Assessment

Critical: None observed.

Important:

No automated console integration tests.
Failure-path state preservation is mostly inferred rather than explicitly asserted.

Optional:

Additional boundary tests for deterministic ordering.
Additional history-retention regression assertions.
Additional explicit exception-state-preservation assertions.

The supplied code aligns well with the review criteria around explicit inputs, query purity, non-mutation, object identity preservation, enum filtering, ordering, and retained history. The primary gap is lack of automated console testing, not a defect in the query or service implementation itself.
 
| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| No automated console tests for `run_menu`, `parse_status`, error display and EOF handling | `console.py` `run_menu`, `parse_status`; there is no `test_console.py` | Important | Accept. Correct: the console was only demonstrated by hand (section D). | No change | Checked the tests folder for a console test file (none). Manual UI-01 and UI-02 runs are recorded in section D |
| State after failure paths is inferred, not asserted everywhere | `services.py` invalid-status and unknown-ID checks; `test_workflows.py`; `test_starter.py` | Important | Modify (partly correct). State is asserted for the conflict case (`store.list_appointments() == before_conflict`), and `test_starter.py` checks that duplicate patient, practitioner and appointment attempts preserve the original. The invalid-status listing only reads data, so it cannot change state. Cancelling an unknown ID is checked only for the exception. | No change | Read the tests: state is asserted for conflict and duplicates, but not after an unknown-ID cancel |
| Assert that the result is a distinct list from the input | `test_queries.py` | Optional | Reject, already covered. `assert results is not appointments` and `assert first_results is not second_results` exist, and `test_services.py` has the same check | No change | Searched the tests for `is not` |
| Add a test where appointments share the same date/time (ID tie-break) | `test_select_appointments_sorts_by_datetime_then_appointment_id` | Optional | Reject, already covered. The fixture has A1 and A4 both at 2026-11-05 10:00, and the expected order `A1, A4, A3, A5` shows the ID tie-break | No change | Read `create_test_appointments` and ran the suite (50 passed) |
| Parameterised test for all enum values | status filter tests | Optional | Reject. Correctness is already covered by the existing status tests; a rewrite is a style change only | No change | Existing tests cover each status |
| Extra history-retention assertion after the freed slot is reused | `test_cancelled_appointment_remains_in_history`, `test_cancelled_appointment_slot_can_be_reused`, `test_complete_appointment_workflow` | Optional | Accept as optional; already shown. After A3 reuses the slot, the D1 list in the workflow test shows A1 (cancelled) and A3 | No change needed | Final D1 list in the workflow test and in the manual UI-01 run |
 
Human finding (ours, not Copilot's): in `list_practitioner_appointments` the status check runs before the practitioner lookup, so an unknown practitioner with an invalid status raises ValueError rather than LookupError. This is harmless and both cases are errors, so we left it unchanged.
 
Responsibility check: Domain invariants stay inside the Appointment object (for example, only a SCHEDULED appointment can be cancelled). The data store holds the three collections and finds records. The services check IDs and status, coordinate the work and raise ValueError or LookupError. `select_appointments` only selects and sorts a list it is given. The console is the only place that reads input, prints, and converts text to a date or a status, and it only calls the services.
 
## F. Required reflections
 
1. Which integration concern was architectural rather than a filtering/sorting detail? Where each job belongs. We used one data store and one set of services for the whole menu session, and kept the console to input and output instead of repeating domain guards or conflict rules in it. The filtering and sorting was a detail inside one pure function.
2. Which Copilot suggestion did you reject as over-engineering, and why? Copilot suggested a parameterised enum test and extra "distinct list" and same-time tie-break tests. We rejected these because the tests already exist: the fixture has A1 and A4 at the same time, and `results is not appointments` is already asserted. Adding them would only repeat existing tests, so it would be over-engineering.
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

Issues and bounded branches:(https://github.com/Blahuee/st1-assignment-3/issues/28); (https://github.com/Blahuee/st1-assignment-3/issues/27); (https://github.com/Blahuee/st1-assignment-3/issues/26); (https://github.com/Blahuee/st1-assignment-3/issues/25)\
 Branches `feature/stage9-queries`, `feature/stage9-practitioner-appointments` and `feature/stage9-console-dispatch`.\
PR/diff and another-member human reviewer: PR #29, PR #30 and PR #31 (code by Alicia), reviewed and merged by Ngedup.
Review responses and Copilot comparison: not applicable.\
 No Copilot review was completed; human review only.\
Integrated common Stage 9 SHA: `351b6ca334415e52054d8a29ef9dab4bed175a2a`
Full regression command, working directory, actual count/result and evidence: `python -m pytest -q`, from `project/`, `50 passed`.\
README run instructions and scope/limitations: `project/README.md` README.md. Run `python main.py` for the demo and `python main.py --interactive` for the menu. Data is kept only while the menu runs.\
Unresolved issues and support/action: Stage 8 section B follow-up, Stage 6 and 7 record fixes, Stage 12 not completed. `main.py` still wraps `run_menu()` in a `try/except NotImplementedError`, which is harmless now.
UG common candidate\
 PG future branch plan: UG common candidate is `351b6ca` going to Stage 12. PG Stages 10 and 11 are unchanged and deferred.
 
- [x] Query contracts, purity, new lists and named-key ordering verified.
- [x] Service empty/unknown/invalid cases and cancellation history verified.
- [x] Every console command and invalid-input recovery demonstrated. 
- [x] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [x] Human design, Copilot critique, review and integration recorded honestly (Copilot not run; stated above).
- [x] Reflections and ten formative responses completed.
- [x] README updated; earlier code/tests/records preserved. 
- [x] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.
No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
 