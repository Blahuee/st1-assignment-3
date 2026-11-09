# Stage 7 Testing and Verification Record

Group/tutorial: Tue 1:30 - 3:30 Group 1 

Members/cohorts: UG - Alicia Hurst (Blahuee), UG - Aagney Mani Sharma (Aagneyf1r3), UG - Ngedup Jigme Lhazeen (njlhazin) 

Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement                         | Positive test                                                                               | Negative test                                                                                                                                     | Key assertion                                                                                                                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR-01 Register patient              | Register a patient with a unique ID and required name, then check they are stored correctly | Attempt to register another patient using an existing patient ID                                                                                  | Check the patient is stored with the correct details and that duplicate registration raises ValueError without overwriting the original patient             |
| FR-05 Prevent practitioner conflict | Schedule an appointment for a practitioner at a particular date and time.                   | Attempt to schedule another appointment for the same practitioner at the exact same date and time while the first appointment is still SCHEDULED. | Check that the first appointment is retained, the second booking raises ValueError, and a booking with a different practitioner at the same time is allowed |
| FR-06 Cancel appointment            | Cancel a scheduled appointment                                                              | Attempt to cancel an already cancelled appointment                                                                                                | Check that the status becomes CANCELLED for the valid cancellation and that a second cancellation raises ValueError                                         |
| FR-07 Retain cancelled history | Cancel an appointment and then retrieve it from the appointment history | Look up an unknown appointment ID (for example A99) after one appointment has been cancelled | Check that the cancelled appointment remains retrievable with its original ID and CANCELLED status, that it is still in the list, and that the unknown ID raises LookupError without changing any stored record |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

| Example Assertion                                          | Strong or Weak? | Why                                                                                                                                                                                 |
| ---------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assert True`                                              | Weak            | It always passes, regardless of whether SmartCare works correctly. It does not check any behaviour                                                                                  |
| `assert appointment is not None`                           | Weak            | It only checks that an appointment exists. It does not check whether the appointment has the correct ID, patient, practitioner, time or status                                      |
| `assert appointment.status == AppointmentStatus.CANCELLED` | Strong          | It checks that the appointment's status actually changed to CANCELLED, which directly verifies the expected cancellation behaviour                                                  |
| `assert len(results) > 0`                                  | Weak            | It only checks that the results contain at least one item. It does not check whether the correct appointment or appointments were returned                                          |
| `assert data_store.find_appointment('A1') is appointment`  | Strong          | It checks that looking up appointment A1 returns the exact same appointment object. This is useful for verifying that the stored appointment has been retained rather than replaced |

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.

| Boundary/Edge Case | Input/State | Output | Contract Supporting Expectation |
| ------------------ | ----------- | ------ | ------------------------------- |
| Blank Identifier | Register patient with ID `""` (empty string) | `ValueError('Patient ID cannot be blank')` | Revision 2 FR-01: IDs are trimmed and non-blank; blank or invalid values raise ValueError |
| Whitespace-Only Name | Register patient with name `" "` (spaces only) | `ValueError('Patient name cannot be blank')` | Revision 2 FR-01: required names are trimmed and non-blank; invalid values raise ValueError |
| Same-Time Practitioner Booking | Book two appointments with the same practitioner at exactly 10:00 on the same date, with the first appointment still SCHEDULED | Reject the second booking and raise ValueError | FR-05, AC-04.1: a practitioner cannot have conflicting scheduled appointments at the same date and time |
| Cancelled Appointment | Cancel an appointment, then check its status and retrieve it from the store | Its status becomes CANCELLED, and the appointment remains available in the current-session history | FR-06, AC-05.1, and FR-07, AC-05.2 |
| Invalid Status Transition | Cancel an appointment that is already CANCELLED, or one that is COMPLETED | Reject the cancellation and raise ValueError; the existing status must remain unchanged | FR-06, AC-05.3: repeated cancellation is rejected; only SCHEDULED appointments may be cancelled (a COMPLETED appointment can be supplied at construction to test the guard) |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
| --------- | ------------- | ------------------------ |
| 1 | It only asserts that the registered patient is not None. This passes even if the ID or name is wrong or empty, so it does not prove FR-01 (register patient). | Register patient P1 "Alexander Stewart", then check the data store returns that same patient with ID P1 and name "Alexander Stewart". |
| 2 | It only asserts that the booked appointment is not None. It would pass with the wrong patient, practitioner, time or status, so it does not prove booking works. | Book appointment A1 for patient P1 with practitioner D1 at a fixed time, then check the stored appointment has that patient, that practitioner, that time and the status SCHEDULED. |
| 3 | assert True always passes whatever the code does. It tests nothing and gives false confidence. | Cancel appointment A1 and check its status is AppointmentStatus.CANCELLED (FR-06). Check the appointment is still in the data store (FR-07). |
| 4 | It assumes an SMS is sent after booking. SMS is not in the requirements baseline and the project has no notification code, so the test checks a feature that does not exist. | Test a real rule instead: a second booking for the same practitioner at the same time is rejected with ValueError, and the store still holds only the first appointment (FR-05). |
| 5 | It assumes an SMS cancellation message is sent. This is also an unrequested feature, so it would need fake code just to pass. | Test the cancellation rules: cancelling an appointment twice is rejected with ValueError, and the appointment stays CANCELLED and unchanged. |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
100% coverage only shows that every line ran during the tests, not that the assertions would catch wrong behaviour. A test with no meaningful assertion, or one that checks the wrong value, still executes the code and raises coverage. Coverage also cannot show missing requirements or untested combinations of inputs.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
| ----------- | -------------------- | ------- | --------- | -------------------- | ------------------ | ------------------------ | ---------------------------- |
| FR-01 Register patient | Revision 2 validation contract (not AC-01.2): blank required values raise ValueError | T-01 | Domain, negative | `test_required_fields`, project/tests/test_starter.py | Blank patient ID and blank practitioner specialty raise ValueError | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-01 Register patient | AC-01.2 Registration with an existing patient ID is rejected | T-02 | Service, negative | `test_duplicate_patient_preserves_original`, project/tests/test_starter.py | ValueError raised; original patient and name unchanged | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-03 Register practitioner | Supporting contract (FR-03): a duplicate practitioner ID is rejected without overwriting | T-03 | Service, negative | `test_duplicate_practitioner_preserves_original`, project/tests/test_starter.py | ValueError raised; original practitioner unchanged | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-04 Book appointment | AC-03.1 Registered participants, unique ID and free time produce a stored SCHEDULED appointment | T-04 | Service, positive | `test_registration_and_booking`, project/tests/test_starter.py | Appointment found by ID, SCHEDULED and stored | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-04 Book appointment | AC-03.2 Booking an unknown patient or practitioner is rejected | T-05 | Service, negative | `test_unregistered_participants_rejected`, project/tests/test_starter.py | LookupError for an unknown patient ID; an unregistered participant object is rejected with ValueError; nothing stored | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-05 Prevent practitioner conflict | AC-04.1 and AC-04.2 Same practitioner, exact time and SCHEDULED conflicts; another practitioner is allowed | T-06 | Service, positive and negative | `test_conflict_rule_and_different_practitioner`, project/tests/test_starter.py | Same practitioner and time rejected; different practitioner at same time allowed | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-06 Cancel appointment | AC-05.1 and AC-05.3 (domain evidence only) | T-07 | Domain, positive and negative | `test_domain_cancellation_and_guard`, project/tests/test_starter.py | cancel() changes status to CANCELLED; second cancel raises ValueError | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-01 Register patient | Revision 2 validation contract: IDs are trimmed and non-blank; blank or invalid raises ValueError | T-08 | Domain, negative and boundary | `test_patient_id_must_not_be_blank_or_invalid`, project/tests/test_domain.py | ValueError for empty, spaces-only and None patient IDs | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-01 Register patient | AC-01.1 Valid required patient data is stored (partial: domain evidence only) | T-09 | Domain, positive | `test_patient_details_are_trimmed`, project/tests/test_domain.py | patient_id and name are stored trimmed | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-03 Register practitioner | Supporting contract (FR-03): a practitioner needs a non-blank ID, name and specialty, otherwise ValueError | T-10 | Domain, negative | `test_practitioner_id_must_not_be_blank_or_invalid`; `test_practitioner_name_must_not_be_blank`; `test_practitioner_specialty_must_not_be_blank`, project/tests/test_domain.py | Blank or None ID, blank name or blank specialty raises ValueError | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-04 Book appointment | AC-03.1 (partial: domain evidence only) | T-11 | Domain, positive | `test_new_appointment_is_scheduled`, project/tests/test_domain.py | New appointment status is SCHEDULED | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-04 Book appointment | Revision 2 contract: local datetime at minute precision; real Patient and Practitioner required | T-12 | Domain, negative and boundary | `test_appointment_requires_valid_participants`; `test_appointment_requires_minute_precision`; `test_appointment_rejects_invalid_datetime`; `test_appointment_rejects_invalid_status`, project/tests/test_domain.py | ValueError for a non-Patient or non-Practitioner, a time with seconds, a non-datetime value or an invalid status | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-06 Cancel appointment | AC-05.1 Cancelling a SCHEDULED appointment changes it to CANCELLED (domain) | T-13 | Domain, positive | `test_scheduled_appointment_can_be_cancelled`, project/tests/test_domain.py | Status becomes CANCELLED | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-06 Cancel appointment | AC-05.3 Repeated cancellation is rejected (domain), plus COMPLETED guard | T-14 | Domain, negative | `test_cancelled_appointment_cannot_be_cancelled_again`; `test_completed_appointment_cannot_be_cancelled`, project/tests/test_domain.py | ValueError for CANCELLED and COMPLETED; status unchanged | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-02 Patient search | AC-02.1 and AC-02.2 Known patient lookup succeeds; unknown lookup reports absence | T-15 | Service, positive and negative | `test_find_patient_returns_known_patient_and_rejects_unknown`, project/tests/test_services.py | Known ID returns the registered patient; unknown valid ID raises LookupError | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-02 Patient search | Revision 2 contract: a blank ID is invalid, not absent | T-16 | Service, boundary | `test_find_patient_rejects_blank_ids`, project/tests/test_services.py | ValueError (not LookupError) for empty and spaces-only IDs | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-03 Register practitioner | Supporting contract (practitioner lookup over registered FR-03 objects): a known ID returns that practitioner; an unknown valid ID raises LookupError | T-17 | Service, positive and negative | `test_find_practitioner_returns_known_and_rejects_unknown`, project/tests/test_services.py | Known ID returns the registered practitioner; unknown valid ID raises LookupError | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-05 Prevent practitioner conflict | AC-04.1 boundary: conflict applies to the exact datetime only | T-18 | Service, boundary | `test_booking_conflict_only_applies_to_exact_datetime`, project/tests/test_services.py | Same time rejected; one minute later accepted; rejected booking leaves state unchanged | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-05 Prevent practitioner conflict | Supporting contract (FR-05): a cancelled booking does not occupy the slot | T-19 | Service, positive | `test_cancelled_appointment_slot_can_be_reused`, project/tests/test_services.py | Rebooking the same practitioner and time succeeds after cancellation | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-06 Cancel appointment | AC-05.1 Cancelling a SCHEDULED appointment changes it to CANCELLED (service) | T-20 | Service, positive | `test_cancel_appointment_returns_cancelled_object`, project/tests/test_services.py | Same appointment object returned with status CANCELLED | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-07 Retain cancelled history | AC-05.2 Cancelled history remains retrievable in the current session | T-21 | Service, positive | `test_cancelled_appointment_remains_in_history`, project/tests/test_services.py | Cancelled appointment still found by ID and in the list, status CANCELLED | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-06 Cancel appointment | AC-05.3 Repeated cancellation is rejected (service), plus COMPLETED guard | T-22 | Service, negative | `test_repeated_and_completed_cancellation_are_rejected`, project/tests/test_services.py | ValueError for repeated or COMPLETED cancellation; state unchanged | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-06 Cancel appointment | Supporting contract (FR-06): a valid unknown appointment ID raises LookupError at the service boundary; blank IDs raise ValueError | T-23 | Service, boundary | `test_cancel_appointment_rejects_unknown_and_blank_ids`, project/tests/test_services.py | LookupError for unknown ID; ValueError for blank IDs; appointment and list unchanged | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-08 Appointment lookup | AC-06.1 A known appointment ID returns that appointment | T-24 | Service, positive | `test_find_appointment_returns_same_object`, project/tests/test_services.py | Returns the same appointment object | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-04 Book appointment | Supporting contract (FR-04): a duplicate appointment ID is rejected without overwriting | T-25 | Service, negative | `test_duplicate_appointment_preserves_original`, project/tests/test_starter.py | ValueError raised; original appointment and its date/time unchanged | Passed (full run: 37 passed; SHA 71ef3a4) | Supplied |
| FR-01 Register patient | Supporting contract (FR-01): a required patient name must not be blank | T-26 | Domain, negative | `test_patient_name_must_not_be_blank`, project/tests/test_domain.py | ValueError for empty and spaces-only patient names | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-01 Register patient | Revision 2 contract: IDs are case-sensitive | T-27 | Domain, boundary | `test_patient_id_preserves_case`, project/tests/test_domain.py | Patient ID "p1" is stored as "p1" and is not equal to "P1" | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-01 Register patient | Supporting contract: identity is read-only | T-28 | Domain, negative | `test_patient_id_cannot_be_changed`, project/tests/test_domain.py | Assigning to patient_id raises AttributeError | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-03 Register practitioner | Supporting contract (FR-03): practitioner details are trimmed | T-29 | Domain, positive | `test_practitioner_details_are_trimmed`, project/tests/test_domain.py | ID, name and specialty are stored with surrounding spaces removed | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-03 Register practitioner | Revision 2 contract: IDs are case-sensitive | T-30 | Domain, boundary | `test_practitioner_id_preserves_case`, project/tests/test_domain.py | Practitioner IDs keep their original case and differ from the swapped-case ID | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |
| FR-03 Register practitioner | Supporting contract: identity is read-only | T-31 | Domain, negative | `test_practitioner_id_cannot_be_changed`, project/tests/test_domain.py | Assigning to practitioner_id raises AttributeError | Passed (full run: 37 passed; SHA 71ef3a4) | Student-authored |

Results recorded from `python -m pytest -v` run in `project/` on `main` at commit 71ef3a41e142c6bd836b597f2c651fb844194c89 (Python 3.14.3, pytest 8.3.5): 37 passed in 0.13s. The same run covers the 8 supplied tests (8 rows) and 29 student-authored test functions (23 rows; T-10, T-12 and T-14 each cover several functions).

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
| ------- | ----------- | -------------------- | ------------------------------ | -------------- | -------------------------- | ------------------------------------ |
| T-08 | FR-01 Register patient | Revision 2 validation contract (not AC-01.2): blank or invalid ID raises ValueError | Negative and boundary | `test_patient_id_must_not_be_blank_or_invalid`: create a Patient with an empty ID, a spaces-only ID and None | ValueError raised each time | The supplied test only tries one blank ID (a single space). This adds the empty string and None. |
| T-09 | FR-01 Register patient | AC-01.1 (partial, domain evidence only) | Positive | `test_patient_details_are_trimmed`: create a Patient with " p1 " and " Test Patient " | patient_id is "p1" and name is "Test Patient" | Shows stored values are trimmed. Related tests (T-26, T-27, T-28) cover a blank name, ID case and a read-only ID. |
| T-10 | FR-03 Register practitioner | Supporting contract (FR-03): a practitioner needs a non-blank ID, name and specialty, otherwise ValueError | Negative | `test_practitioner_id_must_not_be_blank_or_invalid`, `test_practitioner_name_must_not_be_blank` and `test_practitioner_specialty_must_not_be_blank`: try an empty value, a spaces-only value and, for the ID, None | ValueError raised each time | The supplied test only checks a blank specialty. This adds blank and None IDs, blank names and spaces-only values. |
| T-11 | FR-04 Book appointment | AC-03.1 (partial, domain evidence only) | Positive | `test_new_appointment_is_scheduled`: create an Appointment without giving a status | status is AppointmentStatus.SCHEDULED | Checks the default starting status directly on the domain object. |
| T-12 | FR-04 Book appointment | Revision 2 contract: real Patient and Practitioner, minute-precision local datetime | Negative and boundary | `test_appointment_requires_valid_participants`, `test_appointment_requires_minute_precision`, `test_appointment_rejects_invalid_datetime` and `test_appointment_rejects_invalid_status`: pass text instead of objects, a time with seconds, a string instead of a datetime, and a string instead of a status | ValueError raised each time | Covers invalid participants, seconds in the time, a non-datetime and a non-enum status. The supplied tests check none of these. |
| T-13 | FR-06 Cancel appointment | AC-05.1 (domain) | Positive | `test_scheduled_appointment_can_be_cancelled`: create a SCHEDULED appointment and call cancel() | status becomes CANCELLED | Tests the domain rule on its own, with no services or data store. |
| T-14 | FR-06 Cancel appointment | AC-05.3 (domain), plus COMPLETED guard | Negative | `test_cancelled_appointment_cannot_be_cancelled_again` and `test_completed_appointment_cannot_be_cancelled`: cancel twice, and cancel a COMPLETED appointment | ValueError raised, and the status stays CANCELLED or COMPLETED | Adds the COMPLETED case and checks the status is unchanged after the rejection. |
| T-15 | FR-02 Patient search | AC-02.1 and AC-02.2 | Positive and negative | `test_find_patient_returns_known_patient_and_rejects_unknown`: look up P1, then look up P99 | P1 is returned with the right ID and name. P99 raises LookupError. | The supplied tests never call `find_patient`. This is the first test of the Stage 6 lookup. |
| T-16 | FR-02 Patient search | Revision 2 contract: a blank ID is invalid, not absent | Boundary | `test_find_patient_rejects_blank_ids`: look up an empty ID and a spaces-only ID | ValueError (not LookupError) | Separates "invalid input" from "not found". |
| T-17 | FR-03 Register practitioner | Supporting contract (practitioner lookup over registered FR-03 objects): a known ID returns that practitioner; an unknown valid ID raises LookupError | Positive and negative | `test_find_practitioner_returns_known_and_rejects_unknown`: look up D1, then D99 | D1 is returned with the right ID and name. D99 raises LookupError. | First test of `find_practitioner`, which the supplied tests never call. |
| T-18 | FR-05 Prevent practitioner conflict | AC-04.1 boundary: conflict applies to the exact datetime only | Boundary | `test_booking_conflict_only_applies_to_exact_datetime`: book D1 at 10:00, try 10:00 again, then book 10:01 | 10:00 rejected with ValueError, store unchanged, 10:01 accepted | Shows the conflict rule is exact, not a time range, and that a rejected booking changes nothing. |
| T-19 | FR-05 Prevent practitioner conflict | Supporting contract (FR-05): a cancelled booking does not occupy the slot | Positive | `test_cancelled_appointment_slot_can_be_reused`: book 10:00, cancel it, book 10:00 again | The second booking succeeds and is SCHEDULED | Shows a CANCELLED appointment does not cause a conflict. |
| T-20 | FR-06 Cancel appointment | AC-05.1 (service) | Positive | `test_cancel_appointment_returns_cancelled_object`: book A1, then cancel it through the service | The same appointment object is returned with status CANCELLED | First test of the service `cancel_appointment` (a Stage 6 target). It checks the same object is returned. |
| T-21 | FR-07 Retain cancelled history | AC-05.2 | Positive | `test_cancelled_appointment_remains_in_history`: cancel A1, then find it and list all appointments | A1 is found, CANCELLED, and still in the list | Proves cancellation keeps the record instead of deleting it. |
| T-22 | FR-06 Cancel appointment | AC-05.3 (service), plus COMPLETED guard | Negative | `test_repeated_and_completed_cancellation_are_rejected`: cancel A1, cancel A1 again, then cancel a COMPLETED appointment | The second cancel and the COMPLETED cancel raise ValueError; statuses stay CANCELLED and COMPLETED | Tests the guards through the service layer, not just the domain. |
| T-23 | FR-06 Cancel appointment | Supporting contract (FR-06): a valid unknown appointment ID raises LookupError; blank IDs raise ValueError | Boundary | `test_cancel_appointment_rejects_unknown_and_blank_ids`: cancel A99, then an empty and a spaces-only ID | LookupError for A99, ValueError for blank IDs, and the real appointment stays SCHEDULED | Checks the different error types and that failed attempts leave state unchanged. |
| T-24 | FR-08 Appointment lookup | AC-06.1 | Positive | `test_find_appointment_returns_same_object`: book A1, then find A1 | The same appointment object is returned | Confirms lookup returns the stored object, not a copy. |
| T-26 | FR-01 Register patient | Supporting contract (FR-01): a required patient name must not be blank | Negative | `test_patient_name_must_not_be_blank`: create a Patient with an empty name and a spaces-only name | ValueError raised each time | The supplied test only checks a blank patient ID and a blank practitioner specialty. This adds blank patient names. |
| T-27 | FR-01 Register patient | Revision 2 contract: IDs are case-sensitive | Boundary | `test_patient_id_preserves_case`: create a Patient with the ID "p1" | patient_id is "p1" and is not equal to "P1" | Shows the ID keeps its case. |
| T-28 | FR-01 Register patient | Supporting contract: identity is read-only | Negative | `test_patient_id_cannot_be_changed`: try to assign a new value to patient_id | AttributeError raised | Shows the identity cannot be reassigned after construction. |
| T-29 | FR-03 Register practitioner | Supporting contract (FR-03): practitioner details are trimmed | Positive | `test_practitioner_details_are_trimmed`: create practitioners with spaces around the ID, name and specialty | ID, name and specialty are stored without the surrounding spaces | The supplied tests never check trimming for practitioners. |
| T-30 | FR-03 Register practitioner | Revision 2 contract: IDs are case-sensitive | Boundary | `test_practitioner_id_preserves_case`: create practitioners with mixed-case IDs | Each ID keeps its case and differs from its swapped-case version | Shows practitioner IDs keep their case. |
| T-31 | FR-03 Register practitioner | Supporting contract: identity is read-only | Negative | `test_practitioner_id_cannot_be_changed`: try to assign a new value to practitioner_id | AttributeError raised | Shows the practitioner identity cannot be reassigned. |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
| ------- | ------- | --- | ------ | ----------------------------------------------- |
| T-08 | Invalid patient IDs: "", " " and None | Construct Patient(id, "Test Patient") for each | pytest.raises(ValueError) each time | Proves blank and invalid IDs are rejected; it would fail if the constructor accepted an empty or None ID |
| T-13 | Patient P1, practitioner D1, new SCHEDULED appointment A1 | Call appointment.cancel() | status is CANCELLED | Checks the domain transition on its own; it would fail if status did not change |
| T-14 | A1 cancelled once; separate appointment built as COMPLETED | Call cancel() again; call cancel() on the COMPLETED one | ValueError each time; status stays CANCELLED and COMPLETED | Proves illegal transitions are rejected and state is unchanged |
| T-15 | Fresh store with registered P1 "Test Patient" | find_patient("P1"); find_patient("P99") | Result has patient_id "P1" and name "Test Patient"; P99 raises LookupError | Proves the lookup returns the right patient and that an unknown ID is reported as absent |
| T-18 | A1 booked for P1/D1 at 2026-11-05 10:00 | Book A2 at 10:00; then book A3 at 10:01 | A2 raises ValueError; list is [A1], A1 SCHEDULED; A3 accepted and two appointments stored | Proves conflict is the exact datetime only and a rejected booking changes nothing |
| T-19 | A1 booked at 10:00 and cancelled | Book A2 for the same practitioner and time | A2 stored, id "A2", SCHEDULED | Proves a cancelled booking no longer blocks the slot |
| T-20 | A1 booked | cancel_appointment("A1") | Returned object is A1 itself with status CANCELLED | Identity check proves the same object is cancelled, not recreated |
| T-21 | A1 booked then cancelled | find_appointment("A1"); list_appointments() | Found object is A1, CANCELLED; list equals [A1] | Proves history is retained instead of deleted (FR-07) |
| T-22 | A1 booked and cancelled; a COMPLETED appointment A2 added through the store with registered participants | cancel_appointment("A1") again; cancel_appointment("A2") | ValueError each time; A1 stays CANCELLED, A2 stays COMPLETED | Proves service-level guards and unchanged state after rejection |
| T-23 | A1 booked | cancel_appointment("A99"), then "" and " " | LookupError for A99; ValueError for blank IDs; list equals [A1]; A1 SCHEDULED | Separates unknown IDs from invalid IDs and shows failed attempts change nothing |
| T-24 | A1 booked | find_appointment("A1") | Result is A1 itself | Identity check shows the stored object is returned |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
| ------- | --------- | ------------------ | ------ |
| T-01 | Blank patient ID and blank specialty rejected (supplied) | `test_required_fields`, project/tests/test_starter.py | Passed (37 passed on main, SHA 71ef3a4) |
| T-07 | Domain cancellation and repeated-cancel guard (supplied) | `test_domain_cancellation_and_guard`, project/tests/test_starter.py | Passed (37 passed on main, SHA 71ef3a4) |
| T-08 | Blank, spaces-only and None patient IDs rejected | `test_patient_id_must_not_be_blank_or_invalid`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-09 | Patient details trimmed | `test_patient_details_are_trimmed`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-10 | Practitioner ID, name and specialty must be non-blank | `test_practitioner_id_must_not_be_blank_or_invalid`; `test_practitioner_name_must_not_be_blank`; `test_practitioner_specialty_must_not_be_blank`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-11 | New appointment starts SCHEDULED | `test_new_appointment_is_scheduled`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-12 | Invalid participants, seconds in time, non-datetime and invalid status rejected | `test_appointment_requires_valid_participants`; `test_appointment_requires_minute_precision`; `test_appointment_rejects_invalid_datetime`; `test_appointment_rejects_invalid_status`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-13 | SCHEDULED appointment can be cancelled | `test_scheduled_appointment_can_be_cancelled`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-14 | Repeated and COMPLETED cancellation rejected | `test_cancelled_appointment_cannot_be_cancelled_again`; `test_completed_appointment_cannot_be_cancelled`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-26 | Blank patient name rejected | `test_patient_name_must_not_be_blank`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-27 | Patient ID is case-sensitive | `test_patient_id_preserves_case`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-28 | Patient ID is read-only | `test_patient_id_cannot_be_changed`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-29 | Practitioner details trimmed | `test_practitioner_details_are_trimmed`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-30 | Practitioner ID is case-sensitive | `test_practitioner_id_preserves_case`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |
| T-31 | Practitioner ID is read-only | `test_practitioner_id_cannot_be_changed`, project/tests/test_domain.py | Passed (SHA 71ef3a4) |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
| ------- | --------- | ----------------------- | ------------------ | ------ |
| T-15 | Known patient returns the registered object; unknown raises LookupError | FR-02, AC-02.1 and AC-02.2 | `test_find_patient_returns_known_patient_and_rejects_unknown`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-16 | Blank patient ID raises ValueError, not LookupError | FR-02, revision 2 contract | `test_find_patient_rejects_blank_ids`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-17 | Known practitioner returns the registered object; unknown raises LookupError | FR-03 supporting contract | `test_find_practitioner_returns_known_and_rejects_unknown`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-18 | Conflict only at the exact datetime | FR-05, AC-04.1 boundary | `test_booking_conflict_only_applies_to_exact_datetime`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-19 | Cancelled booking frees the slot | FR-05 supporting contract | `test_cancelled_appointment_slot_can_be_reused`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-20 | cancel_appointment returns the same object, CANCELLED | FR-06, AC-05.1 | `test_cancel_appointment_returns_cancelled_object`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-21 | Cancelled appointment remains retrievable and listed | FR-07, AC-05.2 | `test_cancelled_appointment_remains_in_history`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-22 | Repeated and COMPLETED cancellation rejected | FR-06, AC-05.3 | `test_repeated_and_completed_cancellation_are_rejected`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-23 | Unknown ID LookupError, blank ID ValueError, state unchanged | FR-06 supporting contract | `test_cancel_appointment_rejects_unknown_and_blank_ids`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-24 | find_appointment returns the stored object | FR-08, AC-06.1 | `test_find_appointment_returns_same_object`, project/tests/test_services.py | Passed (SHA 71ef3a4) |
| T-02, T-03, T-04, T-05, T-06, T-25 | Supplied service checks: duplicates rejected, booking, unknown participants, conflicts | FR-01, FR-03, FR-04, FR-05 | `test_duplicate_patient_preserves_original`; `test_duplicate_practitioner_preserves_original`; `test_registration_and_booking`; `test_unregistered_participants_rejected`; `test_conflict_rule_and_different_practitioner`; `test_duplicate_appointment_preserves_original`, project/tests/test_starter.py | Passed (supplied; SHA 71ef3a4) |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
| --------- | ---------------------- | --------------- | ------- |
| Patient registration | Empty, spaces-only or None patient ID | ValueError | T-08 |
| Patient registration | Empty or spaces-only name | ValueError | T-26 |
| Practitioner registration | Blank or None ID, blank name or specialty | ValueError | T-10 |
| Appointment construction | Time with seconds; non-datetime; invalid status; non-Patient or non-Practitioner | ValueError | T-12 |
| Patient lookup | Blank ID versus unknown valid ID | ValueError versus LookupError | T-16, T-15 |
| Practitioner lookup | Unknown valid ID | LookupError | T-17 |
| Booking conflict | Same time versus one minute later | Rejected, state unchanged; later accepted | T-18 |
| Booking after cancellation | Same practitioner and time as a cancelled appointment | Accepted | T-19 |
| Cancellation | Already CANCELLED; COMPLETED | ValueError, state unchanged | T-14, T-22 |
| Cancellation | Unknown ID; empty or spaces-only ID | LookupError; ValueError; nothing changes | T-23 |
| Duplicate IDs (supplied) | Existing patient, practitioner or appointment ID | ValueError, original unchanged | T-02, T-03, T-25 |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: FR-06 Cancel appointment. Cancellation is permitted only from SCHEDULED; repeated cancellation and cancellation from COMPLETED raise ValueError without changing state; an unknown valid appointment ID raises LookupError; a blank ID raises ValueError.

Acceptance criterion: "AC-05.3 Repeated cancellation is rejected."

Behaviour to test: After A1 has been cancelled once, calling cancel_appointment("A1") again raises ValueError and leaves A1 CANCELLED, still retrievable, and the only stored appointment.

Human-first test idea/categories: Valid: book and cancel A1 once, which succeeds. Invalid: cancel A1 a second time, expecting ValueError, status still CANCELLED and list_appointments() still [A1]. Boundary: cancelling a COMPLETED appointment is also rejected, an unknown ID (A99) gives LookupError (not ValueError), and a blank ID gives ValueError.

Prompt and purpose: Act as a software test-design assistant. Requirement: FR-06 Cancel appointment. Cancellation is permitted only from SCHEDULED; repeated cancellation and cancellation from COMPLETED raise ValueError without changing state; an unknown valid appointment ID raises LookupError; a blank ID raises ValueError. Acceptance criterion: AC-05.3 Repeated cancellation is rejected. Propose pytest test candidates covering a valid case, an invalid case and meaningful boundaries. For each candidate, state exactly which required behaviour it is intended to verify. Do not invent behaviour not stated in the requirement or criterion. Use observable outcomes rather than private implementation details. Use the current SmartCare public contracts and shared SmartCareDataStore. Do not introduce SQLite, repository abstractions or unrelated features. Do not claim that a proposed test has been executed. Purpose: get a second set of ideas to compare against my own human-first test design.

**Candidate 1: TC-FR06-01 (cancel a scheduled appointment)**
- Copilot test idea/candidate: Store a SCHEDULED appointment, cancel it, check no exception is raised, retrieve it and check its state is no longer SCHEDULED.
- What it claims to verify: Cancellation is permitted from SCHEDULED and the appointment remains retrievable.
- Requirement trace: FR-06, AC-05.1; FR-07, AC-05.2
- Assertion quality: Weak. "No longer SCHEDULED" would also pass if the status became COMPLETED. It does not name AppointmentStatus.CANCELLED, the returned object, or the list contents.
- Human critique: It looked reasonable but was the weakest candidate. The outcome must be the exact CANCELLED status, and the same object should be returned and retained.
- Decision: Modify
- Reason: Valid behaviour, but the assertion needed to be specific and use the real project API.
- Final test reference if accepted/modified: T-20 test_cancel_appointment_returns_cancelled_object and T-21 test_cancelled_appointment_remains_in_history, project/tests/test_services.py
- Actual verification result: The Copilot idea was not run as written. The final tests T-20 and T-21 passed (37 passed, SHA 71ef3a4).

**Candidate 2: TC-FR06-02 (repeated cancellation rejected)**
- Copilot test idea/candidate: Cancel a SCHEDULED appointment, record its state, cancel again, expect ValueError, and check the state is unchanged.
- What it claims to verify: A second cancellation raises ValueError and leaves state unchanged.
- Requirement trace: FR-06, AC-05.3
- Assertion quality: Mostly good (specific exception, state compared), but "state unchanged" is vague. It should assert CANCELLED and that the list is still [A1].
- Human critique: Right idea. It needed to name the status and check the stored list.
- Decision: Modify
- Reason: Correct criterion and exception, with assertions tightened.
- Final test reference if accepted/modified: T-22 test_repeated_and_completed_cancellation_are_rejected, project/tests/test_services.py (domain: T-14)
- Actual verification result: Not run as written. T-22 and T-14 passed (SHA 71ef3a4).

**Candidate 3: TC-FR06-03 (cancel from COMPLETED)**
- Copilot test idea/candidate: Store a COMPLETED appointment, cancel it, expect ValueError, and check it remains COMPLETED.
- What it claims to verify: A COMPLETED appointment cannot be cancelled and its state does not change.
- Requirement trace: FR-06 supporting contract (only SCHEDULED may be cancelled); AC-05.3 guard
- Assertion quality: Adequate. It uses the right exception and checks the state is unchanged.
- Human critique: It does not say how a COMPLETED appointment is created. In the project it must be built with that status at construction and added to the store with registered participants.
- Decision: Modify
- Reason: Valid, but it needed a concrete setup.
- Final test reference if accepted/modified: T-22 (service) and T-14 test_completed_appointment_cannot_be_cancelled (domain)
- Actual verification result: Not run as written. T-22 and T-14 passed (SHA 71ef3a4).

**Candidate 4: TC-FR06-04 (unknown valid ID)**
- Copilot test idea/candidate: Cancel an ID that is valid but not in the store and expect LookupError.
- What it claims to verify: An unknown valid appointment ID raises LookupError.
- Requirement trace: FR-06 supporting contract
- Assertion quality: Weak. It checks only the exception, not that stored data is unchanged.
- Human critique: It should use a concrete ID (A99) while a real appointment exists, and confirm that appointment is untouched.
- Decision: Modify
- Reason: Correct exception, but the state-unchanged check was missing.
- Final test reference if accepted/modified: T-23 test_cancel_appointment_rejects_unknown_and_blank_ids, project/tests/test_services.py
- Actual verification result: Not run as written. T-23 passed (SHA 71ef3a4).

**Candidate 5: TC-FR06-05 (blank ID)**
- Copilot test idea/candidate: Cancel with a blank ID ("") and expect ValueError.
- What it claims to verify: A blank appointment ID raises ValueError.
- Requirement trace: FR-06 supporting contract (Revision 2: blank IDs are invalid)
- Assertion quality: Partial. It covers only "", not a spaces-only ID, and it ignores state.
- Human critique: A spaces-only ID is the more likely real-world blank case and was missing.
- Decision: Modify
- Reason: Valid, but the boundary coverage was incomplete.
- Final test reference if accepted/modified: T-23 (covers "" and " ")
- Actual verification result: Not run as written. T-23 passed (SHA 71ef3a4).

**Candidate 6: TC-FR06-06 (repeated cancellation boundary)**
- Copilot test idea/candidate: Cancel once, immediately cancel again, and compare state before and after the rejected attempt.
- What it claims to verify: State is preserved after a rejected second cancellation.
- Requirement trace: FR-06, AC-05.3
- Assertion quality: Same as Candidate 2; it adds no stronger assertion.
- Human critique: It is essentially a duplicate of TC-FR06-02 with different wording and adds no new evidence.
- Decision: Reject
- Reason: Duplicate. Its intent is already covered by T-22.
- Final test reference if accepted/modified: Not retained
- Actual verification result: Not run. No result is claimed.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? TC-FR06-01, cancelling a scheduled appointment.

Why was it weak? It only required that the state was "no longer SCHEDULED". That would still pass if the status became COMPLETED or any other wrong value. It also named no real API, and it did not check that the same object was returned or that the list was unchanged.

How did you strengthen it? I asserted the exact AppointmentStatus.CANCELLED. I asserted that the returned object is A1 itself, that find_appointment("A1") returns the same object, and that list_appointments() equals [A1]. These became T-20 and T-21.

Accepted / modified / rejected test decisions and evidence: Candidates 1 to 5 were modified and Candidate 6 was rejected as a duplicate (see section H). No Copilot test was accepted unchanged. All final tests passed on main at 71ef3a4 (37 passed).

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
| ------- | ----------------- | -------- | ------ | ------ | --------------- | ----------------------------------------- | --------------------------- |
| `python -m pytest -v` | `project/` | 71ef3a41e142c6bd836b597f2c651fb844194c89 | 37 | 0 | None | None | Full suite on clean main after `git pull --ff-only` (Python 3.14.3, pytest 8.3.5): 8 supplied, 19 domain and 10 service tests, 37 passed in 0.13s. It shows the accumulated tests pass; it does not prove behaviour the tests do not check (see section K). |

Individual test runs and changed-order independence evidence: Run from `project/` on main at 71ef3a41e142c6bd836b597f2c651fb844194c89 (Python 3.14.3, pytest 8.3.5).

- `python -m pytest -v tests/test_domain.py`: 19 passed in 0.09s
- `python -m pytest -v tests/test_services.py`: 10 passed in 0.08s
- `python -m pytest -v tests/test_starter.py`: 8 passed in 0.04s (19 + 10 + 8 = 37, matching the full run)
- Three selected tests in one order (`tests/test_services.py::test_cancelled_appointment_remains_in_history`, `tests/test_domain.py::test_new_appointment_is_scheduled`, `tests/test_starter.py::test_required_fields`): 3 passed in 0.03s
- The same three tests in reverse order: 3 passed in 0.04s

Interpretation: each test builds its own fresh objects or data store, so results do not depend on test order or on other tests.

Optional tutor-led demonstration notes: Not used.

A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.

Requirement → test → failure/observation → diagnosis → change → verification: No test failed in the Stage 7 runs, so there was no diagnosis or change step. Each behaviour traces from requirement to a passing test through section B, for example FR-06 / AC-05.3 → T-14 and T-22 → passed on main at 71ef3a4.

## K What the Suite Still Does Not Prove

- **Tested Stage 7 main SHA:** 71ef3a41e142c6bd836b597f2c651fb844194c89
- **Full-suite result:** `python -m pytest -v` in project/: 37 passed, 0 failed (Python 3.14.3, pytest 8.3.5)
- **Coverage:** Not used. No coverage percentage is claimed, and a percentage alone would not show that the assertions are meaningful.
- **Honest limits of the suite:**
  - Among the student-authored tests, identity (`is`) is checked in T-15, T-17, T-20, T-21 and T-24. The supplied tests T-02, T-03 and T-04 also check it.
  - `parse_date_time` in console.py is not called by any test. Invalid console date input is not tested.
  - `format_appointment` and `run_demo` have no tests.
  - The optional `exclude_appointment_id` argument of `has_practitioner_conflict` is not tested (the starter documents it as ignored).
  - The Stage 9 operations (`appointment_sort_key`, `select_appointments`, `list_practitioner_appointments`, `run_menu`) are not implemented yet, so FR-09 and the query and console requirements are not tested.
  - COMPLETED appointments are only created directly in tests. There is no completion workflow to test.
- **Unresolved defects and effect on baseline:** None found by the Stage 7 suite
- **Clean working tree and integration evidence:** `git status` clean on main after `git pull --ff-only` before the run
- **Stage 8 handover status:** Stage 7 baseline complete; Stage 8 work is on a separate branch (debug/stage08)
- **All tutorial/formative responses and traceability/Copilot decisions complete:** Yes

## L Git and Review Evidence

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
| ---------- | ------ | -- | -------- | ------------ | ------- |
| Stage 7 domain tests (test_domain.py) | testing/domain | [PR #16](https://github.com/Blahuee/st1-assignment-3/pull/16) | None recorded on GitHub | No review comments recorded on PR #16 | Merged to main on 2026-11-03 (merge commit 2c99138) |
| Stage 7 service tests (test_services.py) | Not recorded (commit 8202f64 was not on a pushed feature branch) | None: reached main through merge commit 5134479 (Alicia, 2026-11-03), with no pull request | None recorded | No review recorded on GitHub. T-15 and T-17 were later updated by Aagney in commit 71ef3a4 | Service tests created in commit 8202f64 (2026-11-03); T-15 and T-17 updated in commit 71ef3a4, which is the tested main SHA |
| Stage 7 record (stage07/ sections A to O) | documentation/stage07 | [PR #17](https://github.com/Blahuee/st1-assignment-3/pull/17), opened by njlhazin (earlier Stage 7 activities merged in [PR #14](https://github.com/Blahuee/st1-assignment-3/pull/14)); final merge through [PR #22](https://github.com/Blahuee/st1-assignment-3/pull/22) | Aagney (review comments on PR #17 and PR #14) | Section C must cover T-26 to T-31 because Section B lists them as student-authored; Section C stopped at T-24 so B and C did not match | Feedback addressed (Section C now has T-26 to T-31); the record reached main through PR #22 (merge commit 7cd7eb2, 2026-11-09) |

## M Contribution Evidence

| Member | Actual contribution | Evidence link |
| ------ | ------------------- | ------------- |
| Alicia Hurst | Wrote the domain tests (T-08 to T-14, T-26 to T-31) and the first version of the service tests. Completed tutorial Activities 1 to 3. | Commits 0627016, 5a7a37a (domain tests, merged by PR #16), 8202f64 (service tests), 135f1b0 and 4a50d31 (tutorial activities) |
| Aagney Mani Sharma | Updated service tests T-15 and T-17 (the tested main SHA). Built the traceability matrix (Section B) and recorded the results. Wrote Sections D to I, J, K, N and O, ran the regression run, and applied the final corrections to the record. | Commits 71ef3a4, 7ee04dd, 32c4260, d9abf80, 2c1ec57, 49d46b9, feb6768, and the commits he pushed to documentation/stage07 in [PR #17](https://github.com/Blahuee/st1-assignment-3/pull/17) |
| Ngedup Jigme Lhazeen | Wrote the Part C test design table and the tutorial activity answers. Helped check the draft record for errors against the requirements, the code and the test results and reported the findings to Aagney, who applied the fixes. Opened PR #14 and PR #17 for the Stage 7 record. | Commits 4cebe49 and bf847b3; PR #14 and PR #17 (opened by njlhazin) |

## N Formative Questions

1. What question does verification answer?
Verification asks whether we built the product right, meaning it meets its specification.

2. What question does validation answer?
Validation asks whether we built the right product, meaning it meets what users actually need.

3. What is a unit test?
A unit test checks one small piece of behaviour, such as one function or class, in isolation with controlled setup.

4. What is a pytest fixture?
A pytest fixture is reusable setup code that pytest provides to tests, such as creating a fresh data store.

5. What is parametrisation in pytest?
Parametrisation runs one test function over several input sets, with each case reported separately.

6. What is regression testing?
Regression testing re-runs the accumulated tests after changes to check that earlier behaviour still works.

7. What does code coverage tell us, and what does it not prove?
Coverage tells us which lines or branches ran during tests. It doesn't prove the assertions are meaningful or the behaviour correct.

8. What makes an assertion weak?
An assertion is weak when it would still pass if the behaviour were wrong, for example assert True, is not None, or a test that never checks the result.

9. What is the appropriate role of GitHub Copilot as a test assistant?
Copilot is a test assistant that suggests candidates. Each must be checked against the requirement, the assertions and an actual run, and it can't replace human test design.

10. What is the Stage 7 engineering rule?
The Stage 7 engineering rule: every test traces to a real requirement, asserts specific required behaviour that could fail for the right reason, and counts as evidence only if it was actually run and recorded with its tested SHA.

## O Stage Completion

- **Tested Stage 7 main SHA:** 71ef3a41e142c6bd836b597f2c651fb844194c89
- **Full-suite result:** `python -m pytest -v` in project/: 37 passed, 0 failed (Python 3.14.3, pytest 8.3.5)
- **Unresolved defects and effect on baseline:** None found by the Stage 7 suite
- **Clean working tree and integration evidence:** `git status` clean on main after `git pull --ff-only` before the run
- **Stage 8 handover status:** Stage 7 baseline complete; Stage 8 work is on a separate branch (debug/stage08)
- **All tutorial/formative responses and traceability/Copilot decisions complete:** Yes