# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Tue 1:30 - 3:30 Group 1
Members and UG/PG cohorts: UG - Alicia Hurst - Blahuee, UG - Aagney Mani Sharma - Aagneyf1r3, UG - Ngedup Jigme Lhazeen - njlhazin
Record owner / contribution links for each member: [complete]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.

**Response and Reason:**

| Statement                                                        | Classification | Reason                                                                                            |
| ---------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------- |
| Appointment disappears after cancellation                        | Symptom        | Describes what the user observes without explaining why it happens                                |
| The data-store removal path is probably being called             | Hypothesis     | Suggests a possible cause that needs investigation                                                |
| The failing test shows store.find_appointment('A1') returns None | Evidence       | Describes an observable result from a test                                                        |
| The service layer is badly designed                              | Opinion        | A subjective judgement without supporting evidence                                                |
| Traceback points to smartcare/services.py line 42 in the example | Evidence       | A traceback identifies where an exception occurred or propagated. The actual line must be checked |

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

**Response and reason:**

- **Expected:** A cancelled appointment should remain stored and be retrievable using its appointment ID
- **Observed:** After cancellation, the appointment remains in the list but cannot be retrieved using `find_appointment()`
- **Reproduction:** Register a patient and practitioner, book appointment A1, cancel A1, then attempt to retrieve A1
- **Hypothesis:** The data store may be filtering cancelled appointments from its lookup results
- **Evidence to inspect:** `find_appointment()`, `list_appointments()`, the appointment status and the service lookup method

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

**Response and reason:** 
- The test should be changed because expecting cancelled appointments to be deleted contradicts FR-07, which requires appointment history to be retained. The implementation should preserve the appointment and its cancelled status

- A test expecting two different practitioners to conflict at the same time is also incorrect. AC-04.2 permits different practitioners to have appointments at the same time. The test should verify that the second booking succeeds

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. 

**Response and reason:**

| Proposed change                                      | Classification | Explanation                                                   |
| ---------------------------------------------------- | -------------- | ------------------------------------------------------------- |
| Rename appt to appointment                           | Refactoring    | Improves readability without changing behaviour               |
| Extract a repeated conflict helper                   | Refactoring    | Reduces duplication while preserving conflict rules           |
| Add rescheduling                                     | Feature        | Introduces new functionality                                  |
| Restore retained cancellation lookup                 | Repair         | Corrects behaviour that violates the requirements             |
| Replace a magic status string with the existing enum | Refactoring    | Uses an existing named constant instead of a hardcoded string |

**Explain the behaviour that must remain unchanged:**
- The refactoring should improve readability and maintainability without changing the application's existing behaviour. Appointment booking, cancellation, validation, returned objects and retained history must continue to work as before.

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

**Response and reason:**
- **Actual failure:** `test_cancelled_appointment_remains_in_history` failed because `appointment_service.find_appointment("A1")` returned `None` instead of the original appointment object.

- **Expected behaviour:** FR-07 requires cancelled appointments to remain in history. The same appointment object should remain retrievable with its status set to `CANCELLED`.

- **Observed behaviour:** The lookup returned `None`, causing the identity assertion `assert found_appointment is appointment` to fail. The relevant assertion is in `project/tests/test_services.py`, inside `test_cancelled_appointment_remains_in_history` (line 184 in the supplied broken repository).

- **Application call path:** The test calls `AppointmentService.find_appointment()`, which delegates the lookup to `SmartCareDataStore.find_appointment()`. The data-store method returns `None` because its lookup condition excludes appointments with a cancelled status.

- **Possible causes ranked by likelihood:**
  1. The data-store lookup method filters out cancelled appointments. Check the status condition inside `find_appointment()` to determine whether cancelled records are being excluded.
  2. The cancellation process removes the appointment from the data store. Check `list_appointments()` immediately after cancellation to confirm whether the original object is still stored.
  3. The appointment ID is not matching the stored record. Compare the stored appointment ID with the requested ID and inspect the trimming and matching conditions.

The first cause is most likely because the lookup method contains a condition that excludes cancelled appointments. A traceback alone does not establish the root cause because it identifies where the failure occurred, not necessarily why it occurred. Inspecting the service and data-store methods, along with the stored appointment state, provides evidence to confirm the cause.

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: [complete]

**Classification responses (1–5, each with reason):** Completed in the relevant Part A sections above\
**Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect:** [complete]\
**Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks:** [complete]

## B. Stage 7 baseline and safe preparation

- **Stage 7 code SHA and requirement baseline:**\
  e6b3579c1c29e57894abef33fcae152c9d4f8c7b, SmartCare Assignment 3 Requirements Baseline, Revision 2
- **Baseline test command / working directory / observed result / evidence:**
  - **Command:** `python -m pytest -vv -s`
  - **Working directory:** `D:\_Scripts\Repos\st1-assignment-3\project`
  - **Observed result:** 37 passed, 0 failed in 0.12 seconds.
  - **Evidence:** 37 tests passed before Stage 8 preparation.
- **Clean preparation SHA if a record-only commit followed Stage 7:**\
  No separate record-only commit was made between the Stage 7 baseline and Stage 8 preparation. The clean preparation SHA remained e6b3579c1c29e57894abef33fcae152c9d4f8c7b
- **Branch and preparer / how teammates obtained this branch:**
  - **Branch:** debug/stage08
  - **Preparer:** Alicia
  - **How teammates obtained the branch:** Aagney and Ngedup were instructed to run the following commands from their local repository:\
    `git switch main`\
    `git fetch origin`\
    `git switch --track origin/debug/stage08`\
  This created a local tracking branch for origin/debug/stage08, allowing teammates to access the prepared Stage 8 changes.
- **Downloaded tool version, source SHA256 and --check outcome:**
  - **Tool version:** Stage 8 tool 1.1
  - **--check outcome:** Preflight passed; project remained unchanged; both proposed fault signatures were verified in a temporary copy.
- **--apply and --verify output summaries / artefact references:**\
  - **--apply:** Successfully prepared F8-01 (practitioner conflict) and F8-02 (retained-history lookup).
  - **Expected failures:** test_f8_01_conflict and test_f8_02_history (2 failed).
  - **Backup:** Backup and hash recorded in .stage8_faults.
  - **--verify:** Confirmed exactly two expected failures and both approved symptom signatures.
- **Bounded diff inspected and recovery location (not committed):**\
  Inspected commit `b99a90f` using `git show`. The diff contains changes to two files:
  - project/smartcare/data_store.py: introduced F8-01 by changing the practitioner comparison from `==` to `!=`, and F8-02 by excluding cancelled appointments from `find_appointment()`
  - .gitignore: removed the prepare_debugging.py exclusion while retaining .stage8_faults/.
  The recovery backup is stored locally in project/.stage8_faults/. This directory is excluded from Git and was not committed.
- **Prepared faulty-state commit SHA:**\
  b99a90f474f67b9e47b3f196adc8d6d78e7346e0
- **Preparation or recovery issues and resolution, if any:**\
  No issues encountered
- **Initial prepared full-suite command / result / key failures:**
  - Command: python -m pytest -v
  - Working directory: D:\_Scripts\Repos\st1-assignment-3\project
  - Observed result: 33 passed, 4 failed (37 tests total).
  - Key failures:
    - F8-01 – Practitioner conflict: `test_booking_conflict_only_applies_to_exact_datetime` and `test_conflict_rule_and_different_practitioner` failed because the system did not raise the expected `ValueError` when booking the same practitioner at the same time
    - F8-02 – Retained-history lookup: `test_cancelled_appointment_remains_in_history` and `test_repeated_and_completed_cancellation_are_rejected` failed because cancelled appointments could not be retrieved, resulting in `LookupError: Appointment not found`

## C. F8-01 diagnosis and repair

- **Symptom / observed behaviour:**\
  The system allowed a second appointment to be booked for the same practitioner at the same date and time. The expected ValueError was not raised, meaning the booking conflict rule was not correctly enforced
- **Expected behaviour and requirement:**\
  The system should prevent a practitioner from having two scheduled appointments at the same date and time. Appointments for different practitioners at the same time should still be permitted. Appointments at different times should also be permitted
- **Minimal synthetic reproduction steps:**
  1. Create the SmartCare test services.
  2. Register or use an existing practitioner with ID D1.
  3. Book an appointment for patient P1, practitioner D1, at 2026-11-05 10:00.
  4. Attempt to book another appointment for the same practitioner at the same date and time.
  5. Observe whether the system raises the expected `ValueError`.
- **Meaningful failing test path/name and exact relevant failure:**\
  - **Test:** tests/test_services.py::test_booking_conflict_only_applies_to_exact_datetime
  - **Failure:** `Failed: DID NOT RAISE <class 'ValueError'>`
  - **Location:** `tests/test_services.py, line 99`, when the test checks that booking a second appointment with the same practitioner at the same date and time raises a `ValueError`.\
  A second test also encountered the problem:
  - **Test:** tests/test_starter.py::test_conflict_rule_and_different_practitioner
  - **Failure:** `Failed: DID NOT RAISE <class 'ValueError'>`
  - **Location:** tests/test_starter.py, line 127, when the test checks that a booking conflict is rejected while allowing appointments with different practitioners.
- **Human hypothesis and intended checks: see E, F8-01.**
- **Supported root cause and inspected code/runtime evidence:**\
  Inspection of project/smartcare/data_store.py, inside `has_practitioner_conflict()`, identified an incorrect comparison operator. The practitioner ID comparison used `!=` instead of `==`.
  This caused the conflict check to identify appointments belonging to different practitioners rather than appointments belonging to the same practitioner. The initial test failures supported this diagnosis.
- **Smallest justified fix / diff / why other behaviour is preserved:**
  - Changed the practitioner ID comparison in project/smartcare/data_store.py, inside `has_practitioner_conflict()`, from `!=` to `==`.
  - The appointment ID exclusion condition (`!=`), exact date/time comparison (`==`) and scheduled-status check were preserved. This ensures that only another scheduled appointment for the same practitioner at the same date and time is treated as a conflict.
- **Repair SHA / focused verification result:**
  - **Repair SHA:** ed76dc8af625654d916a3345e274d138bb05978d
  - **Focused verification result:**
    - `test_booking_conflict_only_applies_to_exact_datetime` - PASSED
    - `test_conflict_rule_and_different_practitioner` - PASSED
    - **Result:** 2 passed, 0 failed in 0.02 seconds.

## D. F8-02 diagnosis and repair

- **Symptom / observed behaviour:**\
  After an appointment was cancelled, attempting to retrieve it by its appointment ID returned no result. The service then raised `LookupError: Appointment not found`, even though the cancelled appointment remained stored.
- **Expected behaviour and requirement:**\
  The system must retain cancelled appointments in its history and allow them to be retrieved using their appointment ID. This supports FR-07 (retained appointment history). Cancellation must change the appointment status without removing the appointment from the data store.
- **Minimal synthetic reproduction steps:**
  1. Create the SmartCare test services.
  2. Book an appointment with ID A1 for patient P1 and practitioner D1.
  3. Cancel appointment A1.
  4. Attempt to retrieve appointment A1 using `appointment_service.find_appointment("A1")`.
  5. Observe whether the cancelled appointment is returned or a `LookupError` is raised.
- **Meaningful failing test path/name and exact relevant failure:**
  - **Test:** tests/test_services.py::test_cancelled_appointment_remains_in_history
  - **Failure:** `LookupError: Appointment not found`
  - **Location:** smartcare/services.py, line 136, when `find_appointment()` receives `None` from the data store.\
    A second affected test was:
  - **Test:** tests/test_services.py::test_repeated_and_completed_cancellation_are_rejected
  - **Failure:** `LookupError: Appointment not found`
  - **Location:** smartcare/services.py, line 149, when `cancel_appointment()` cannot retrieve the previously cancelled appointment.
- **Human hypothesis and intended checks: see E, F8-02.**
- **Supported root cause and inspected code/runtime evidence:** [complete after diagnosis]
- **Smallest justified fix / diff / why other behaviour is preserved:** [complete]
- **Repair SHA / focused verification result:**
  - **Repair SHA:** bb070749a483e84011dac9f2d2ed0f23730f8264
  - **Focused verification:**
  - `test_cancelled_appointment_remains_in_history` - PASSED
  - `test_repeated_and_completed_cancellation_are_rejected` - PASSED
  - `test_find_appointment_returns_same_object` - PASSED
  - **Result:** 3 passed, 0 failed in 0.02 seconds.

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
**Likely cause and why plausible:** The practitioner conflict checking logic may be incorrectly comparing practitioner IDs. This makes sense because the system allows two appointments with the same practitioner at the same date and time, even though the booking should normally be rejected.\
**Evidence intended to inspect / competing explanation / discriminating check:**  I will inspect the implementation of `has_practitioner_conflict()` within data_store.py and check how practitioner IDs, appointment dates and appointment statuses are compared. Alternatively, it may be attributed to the booking service not calling the conflict checking function correctly. I would check whether the function is called during booking and compare the results for appointments involving the same practitioner versus different practitioners at the same time.\
**Member and saved sequence/time or commit showing this preceded consultation:** Ngedup Jigme Lhazeen, Stage 8 documentation saved on 07/11/2026 at 21:30, before Copilot consultation.

### F8-02 human entry
**Likely cause and why plausible:** I suspect the appointment lookup logic may be incorrectly filtering the cancelled appointments. This is plausible because the appointment is expected to remain in the system's history after cancellation, but attempting to retrieve it by its appointment ID results in a `LookupError`.\
**Evidence intended to inspect / competing explanation / discriminating check:** I will inspect the `find_appointment()` function inside data_store.py to find out whether cancelled appointments are being excluded during the lookup process. Another possibility is that the cancellation process removes the appointment from the data store. I will check whether the appointment still exists in storage after it is canceled and confirm whether a search using its ID can still locate it.\
**Member and saved sequence/time or commit showing this preceded consultation:** Ngedup Jigme Lhazeen, Stage 8 documentation saved on 07/11/2026 at 21:30, before Copilot consultation.

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
**Actual prompt / output reference and member:**\
Member: Alicia
> I am investigating a deliberately introduced defect in the
> SmartCare application. Do not rewrite the application or
> suggest changes yet. Treat all explanations as hypotheses.
>
> Observed behaviour:
> Booking a second appointment with the same practitioner at
> the same date and time does not raise a ValueError.
>
> Expected behaviour:
> The system must reject two scheduled appointments for the
> same practitioner at the exact same date and time.
> Different practitioners and different appointment times
> must still be allowed.
>
> Steps to reproduce:
> 1. Create the test services.
> 2. Book appointment A1 for patient P1 with practitioner D1
>    at 2026-11-05 10:00.
> 3. Attempt to book another appointment with practitioner D1
>    at the same date and time.
> 4. Observe that the expected ValueError is not raised.
>
> Failing test:
> tests/test_services.py::test_booking_conflict_only_applies_to_exact_datetime
> Failure: Failed: DID NOT RAISE <class 'ValueError'>
> Location: tests/test_services.py, line 99.
>
> Human hypothesis:
> The practitioner conflict checking logic may be incorrectly
> comparing practitioner IDs.
>
> Relevant code:
>  def has_practitioner_conflict(
>         self,
>         practitioner_id: str,
>         date_time: datetime,
>         exclude_appointment_id: str | None = None,
>     ) -> bool:
>         for appointment in self.list_appointments():
>             if (appointment.appointment_id != exclude_appointment_id
>                     and appointment.practitioner.practitioner_id != practitioner_id
>                     and appointment.date_time == date_time
>                     and appointment.status.value == "scheduled"):
>                 return True
>         return False
>
> Task:
> Rank the three most likely causes of this defect.
> For each cause:
> - Explain why it is plausible.
> - Identify the specific code or test evidence I should inspect.
> - Explain what evidence would distinguish it from the
>   other possible causes.
>
> Do not rewrite the application.
> Do not invent requirements.
> Treat all suggested explanations as hypotheses.

| Ranked Suggestion                                                                                                                                               | Evidence Check                                                                                                                                                                            | Observed Evidence                                                                                                                                                                                                                                                                                                  | Classification | Decision                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The practitioner conflict predicate uses `!=` instead of `==`, meaning it detects appointments for different practitioners rather than the same practitioner    | Inspected `has_practitioner_conflict()` in `data_store.py` and checked the practitioner comparison. Also reviewed the failing test `test_booking_conflict_only_applies_to_exact_datetime` | The faulty code used `appointment.practitioner.practitioner_id != practitioner_id`. In the test scenario, both appointments use practitioner ID D1, so the comparison evaluates to `False` and the conflict is not detected. After changing the comparison to `==`, the two focused F8-01 tests passed             | Correct        | **Accept.** The code directly supports this explanation, and the focused tests confirmed that correcting the comparison resolved the observed failure                        |
| The booking process may be passing an incorrect practitioner ID to `has_practitioner_conflict()`, or the stored practitioner ID may not match the supplied ID   | Inspected the call to `has_practitioner_conflict()` and the practitioner ID values used by the booking process                                                                            | The test scenario uses practitioner ID `D1` for both appointments. The failure was explained by the incorrect `!=` comparison in the conflict predicate. Correcting that comparison resolved the focused tests without needing to change practitioner creation, storage or the booking call                        | Wrong          | **Reject.** There was no evidence of an incorrect practitioner ID being passed or stored. The existing comparison operator was the cause of the failure                      |
| The existing appointment may not be returned by `list_appointments()`, or another condition in the predicate may prevent it from being recognised as a conflict | Inspected the appointment iteration and the remaining conflict conditions, including appointment ID exclusion, date/time matching and scheduled status                                    | The existing appointment was available to the conflict check, and the appointment ID exclusion, exact date/time comparison and scheduled-status condition were not responsible for the failure. The practitioner comparison was the incorrect condition. The focused tests passed after correcting that comparison | Wrong          | **Reject.** The evidence did not indicate a problem with appointment retrieval or the other predicate conditions. The failure was isolated to the practitioner ID comparison |

**Final human conclusion and comparison with initial hypothesis:**\
- The investigation confirmed that the F8-01 defect was caused by an incorrect practitioner ID comparison in `has_practitioner_conflict()`. The faulty code used `!=` instead of `==`, meaning appointments for different practitioners could be identified as conflicts while appointments for the same practitioner were not correctly detected.
- My initial human hypothesis was that the practitioner conflict logic was incorrectly comparing practitioner IDs. Copilot's first-ranked suggestion supported this hypothesis, and inspection of the code confirmed it. I accepted the first suggestion and rejected the other two because the evidence did not support them. I corrected the comparison while retaining the existing appointment exclusion, exact date/time comparison and scheduled-status check. The two focused F8-01 tests passed after the repair.

**Final human conclusion and comparison with initial hypothesis:**\
- The investigation confirmed that the F8-01 defect was caused by an incorrect practitioner ID comparison in `has_practitioner_conflict()`. The faulty code used `!=` instead of `==`, meaning appointments for different practitioners could be identified as conflicts while appointments for the same practitioner were not correctly detected.
- My initial hypothesis was that the practitioner conflict logic was incorrectly comparing practitioner IDs. Copilot's first-ranked suggestion supported this hypothesis, and inspection of the code confirmed it. I accepted the first suggestion and rejected the other two because the evidence did not support them. I corrected the comparison while retaining the existing appointment exclusion, exact date/time comparison and scheduled-status check. The two focused F8-01 tests passed after the repair.

### F8-02 Copilot review
**Actual prompt / output reference and member:**\
Member: Alicia
> I am investigating a deliberately introduced defect in the
> SmartCare application. Do not rewrite the application or
> suggest changes yet. Treat all explanations as hypotheses.
>
> Observed behaviour:
> After an appointment is cancelled, attempting to retrieve
> it by its appointment ID results in LookupError:
> Appointment not found.
>
> Expected behaviour:
> Cancelled appointments must remain in the appointment
> history and be retrievable by their appointment ID.
> Cancellation should change the appointment status without
> removing the stored record.
>
> Steps to reproduce:
> 1. Create the test services.
> 2. Book appointment A1 for patient P1 with practitioner D1
>    at 2026-11-05 10:00.
> 3. Cancel appointment A1.
> 4. Attempt to retrieve appointment A1 using find_appointment.
> 5. Observe that LookupError is raised.
>
> Failing tests:
> tests/test_services.py::test_cancelled_appointment_remains_in_history
> Failure: LookupError: Appointment not found
> Location: tests/test_services.py, line 182.
>
> tests/test_services.py::test_repeated_and_completed_cancellation_are_rejected
> Failure: LookupError: Appointment not found
> Location: tests/test_services.py, line 207.
>
> Human hypothesis:
> The appointment lookup logic may be incorrectly filtering
> out cancelled appointments.
>
> Relevant code:
> def find_appointment(self, appointment_id: str) -> Appointment | None:
>         if not isinstance(appointment_id, str) or not appointment_id.strip():
>             raise ValueError("Appointment ID cannot be blank")
>         for appointment in self.list_appointments():
>             if (appointment.appointment_id == appointment_id.strip()
>                     and appointment.status.value != "cancelled"):
>                 return appointment
>         return None
>
> Task:
> Rank the three most likely causes of this defect.
> For each cause:
> - Explain why it is plausible.
> - Identify the specific code or test evidence I should inspect.
> - Explain what evidence would distinguish it from the
>   other possible causes.
>
> Do not rewrite the application.
> Do not invent requirements.
> Treat all suggested explanations as hypotheses.

| Ranked Suggestion                                                                                                                                            | Evidence                                                                                                                                                       | Observed                                                                                                                                                                                                                                                                                             | Classification | Decision                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `find_appointment()` contains a status filter that prevents appointments with a cancelled status from being returned, even when their appointment ID matches | Inspected `find_appointment()` in `data_store.py`, particularly the condition `appointment.status.value != "cancelled"`                                        | The faulty code checked both the appointment ID and whether its status was not cancelled. After cancellation, the appointment still existed in storage, but the status condition prevented it from being returned. Removing the status restriction allowed the cancelled appointment to be retrieved | Correct        | The code directly supported this explanation. The focused tests passed after removing the status restriction while retaining appointment ID matching                            |
| The cancellation process may be deleting the appointment from storage rather than changing its status                                                        | Inspected the cancellation process and the appointment storage/lookup logic to determine whether cancellation removes the record                               | The appointment remained stored after cancellation. The problem was that `find_appointment()` excluded cancelled appointments when searching by ID. Removing that filter restored access to the existing record                                                                                      | Wrong          | The evidence showed that cancellation did not remove the appointment. The record remained in storage, but the lookup condition prevented it from being returned                 |
| `list_appointments()` may be excluding cancelled appointments before they reach the ID comparison in `find_appointment()`                                    | Inspected `list_appointments()` and the iteration used by `find_appointment()` to determine whether cancelled appointments were available to the lookup method | The issue was within the status condition in `find_appointment()`, rather than an upstream filter in `list_appointments()`. Removing the status condition allowed the existing cancelled appointment to be returned                                                                                  | Wrong          | There was no evidence that `list_appointments()` was responsible for excluding the record. The defect was isolated to the additional status restriction in `find_appointment()` |

**Final human conclusion and comparison with initial hypothesis:**
- The investigation confirmed that F8-02 was caused by `find_appointment()` excluding appointments with a cancelled status. This meant that cancelled appointments remained stored but could no longer be retrieved using their appointment ID, resulting in a LookupError.
- My initial hypothesis was that the lookup logic was incorrectly filtering out cancelled appointments. Copilot's first-ranked suggestion supported this hypothesis, and inspection of the code confirmed it. I accepted the first suggestion and rejected the other two because the evidence did not support them. I removed the cancelled-status restriction while retaining the existing blank ID validation and appointment ID matching. The focused tests passed after the repair.

## G. Failing to passing regression evidence

| Checkpoint                                     | Code SHA or precise diff                 | Command and working directory                                 | Actual result and artefact reference                                                                                                                                                                                                                           |
| ---------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F8-01 before repair                            | b99a90f474f67b9e47b3f196adc8d6d78e7346e0 | **Directory:** project **Command:** `python -m pytest -vv -s` | Failed: `DID NOT RAISE ValueError` in `test_booking_conflict_only_applies_to_exact_datetime`. Initial full-suite result: 33 passed, 4 failed. Evidence: Initial Stage 8 pytest terminal output.                                                                |
| F8-01 after repair                             | ed76dc8af625654d916a3345e274d138bb05978d | **Directory:** project **Command:** `python -m pytest -vv -s` | Passed: F8-01 conflict tests passed. Evidence: Focused test output showing 2 passed, 0 failed.                                                                                                                                                                 |
| F8-02 before repair                            | b99a90f474f67b9e47b3f196adc8d6d78e7346e0 | python -m pytest -v                                           | Failed: `LookupError: Appointment not found` in `test_cancelled_appointment_remains_in_history` and `test_repeated_and_completed_cancellation_are_rejected`. Initial full-suite result: 33 passed, 4 failed. Evidence: Initial Stage 8 pytest terminal output. |
| F8-02 after repair                             | bb070749a483e84011dac9f2d2ed0f23730f8264 | **Directory:** project **Command:** `python -m pytest -vv -s` | **Passed:** 3 focused F8-02 tests passed, 0 failed (2 tests in the first run and 1 in the second). Evidence: Focused pytest terminal outputs.                                                                                                                  |
| Full suite after both repairs, before refactor | bb070749a483e84011dac9f2d2ed0f23730f8264 | **Directory:** project **Command:** `python -m pytest -vv -s` | **Passed:** 37 passed, 0 failed. Evidence: Final full-suite pytest terminal output.                                                                                                                                                                            |

**Explain how the assertions detect each relevant incorrect result and protect previous behaviour:** 
- The F8-01 assertions check that booking a second appointment with the same practitioner at the exact same date and time raises a `ValueError`. They also verify that appointments with different practitioners or different appointment times are still permitted. This ensures the conflict rule works without incorrectly rejecting valid bookings.
- The F8-02 assertions check that a cancelled appointment remains retrievable by its appointment ID and that the original appointment object is returned. They also verify that repeated cancellations and cancellations of completed appointments are rejected with a ValueError. This ensures appointment history is retained while existing cancellation rules remain enforced.\

**Unrelated failures investigated / resolution:**
- Not applicable. All four initial test failures were associated with the two identified Stage 8 faults (F8-01 and F8-02). No unrelated failures were identified during the initial full-suite run. After both repairs, the complete test suite passed with 37 passed and 0 failed.

## H. Refactoring decision and before/after verification

**Smell and exact location:** No significant code smell was identified in the repaired methods. `has_practitioner_conflict()` and `find_appointment()` have relatively simple logic, and their conditions are clear. No unnecessary duplication or structural complexity was identified that justified refactoring\
**Small proposed structural change / why justified:** No structural change was proposed because the repaired methods are already straightforward and readable. Further restructuring would add complexity without providing a clear maintainability benefit. The existing implementation was therefore retained\
**External behaviour to preserve / relevant tests:** The existing external behaviour must remain unchanged. This includes:
- Preventing two scheduled appointments for the same practitioner at the exact same date and time
- Allowing appointments for different practitioners or different times
- Excluding the appointment being updated from conflict detection where applicable
- Allowing appointments to be retrieved by ID regardless of whether they are scheduled, cancelled or completed
- Raising the appropriate exceptions for invalid IDs, missing appointments and invalid cancellation transitions

Relevant tests include `tests/test_services.py`, `tests/test_starter.py` and the full test suite\
**Before result:** Before refactoring, the repaired application passed the complete test suite: 37 passed, 0 failed. The result was recorded in Section G\
**Actual change / diff / separate refactor SHA:** No refactoring changes were made. The existing repaired implementation was retained. No additional diff or separate refactoring commit was created\
**Focused and full after-refactor commands / working directory / results / evidence:** Not applicable. No refactoring changes were made, so there was no separate after-refactor test run. The repaired implementation remained unchanged from the passing full-suite result recorded in Section G\
**Result — accepted, revised or rejected / reason / behaviour-preservation conclusion:** Rejected, no refactoring performed. The proposed refactoring was not considered necessary because the repaired methods were already simple and readable. Making structural changes without a clear benefit would introduce unnecessary risk. The existing implementation was retained, preserving the behaviour verified by the passing test suite.

## I. Git, human review and integration

**Issues for both defects / refactor scope and owners:**
- [F8-01 - Practitioner conflict detection defect](https://github.com/Blahuee/st1-assignment-3/issues/19)
- [F8-02 – Cancelled appointments excluded from history lookup](https://github.com/Blahuee/st1-assignment-3/issues/20)
- Issue Owners: Alicia (Blahuee)

**Branch / prepared, repair and refactor checkpoints:**
| Checkpoint                    | Git SHA                                  | Description                                     |
| ----------------------------- | ---------------------------------------- | ----------------------------------------------- |
| Stage 7 baseline              | e6b3579c1c29e57894abef33fcae152c9d4f8c7b | Last known passing Stage 7 baseline             |
| Stage 8 prepared faulty state | b99a90f474f67b9e47b3f196adc8d6d78e7346e0 | Deliberately introduced F8-01 and F8-02 defects |
| F8-01 repair                  | ed76dc8af625654d916a3345e274d138bb05978d | Corrected practitioner comparison               |
| F8-02 repair                  | bb070749a483e84011dac9f2d2ed0f23730f8264 | Restored cancelled appointment lookup           |
| Refactor checkpoint           | Not applicable                           | No refactoring performed                        |

Stage 8 was completed in `debug/stage08`. The prepared faulty state and later repairs are identifiable through the Git commit history. F8-01 and F8-02 were repaired in separate commits. No separate refactoring commit was created because the refactoring decision was to retain the existing repaired implementation.

**PR link and another member's reviewer identity:**
- PR: [Stage 8 – Repair appointment conflict and history lookup defects, completed sections I to H](https://github.com/Blahuee/st1-assignment-3/pull/21)
- Reviewer: Alicia (Blahuee).
**Key human feedback, difference from Copilot findings and response/outcome:** [complete]
**Actual review approval / merge evidence:** [complete]
**Integrated code SHA and team pull/retest command / working directory / result:** [complete]
**Evidence-only later SHA / explanation if different:** [complete or not applicable]
**Each member's substantive contribution and artefact:** [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
