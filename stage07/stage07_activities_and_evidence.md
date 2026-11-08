# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement                         | Positive test                                                                               | Negative test                                                                                                                                     | Key assertion                                                                                                                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FR-01 Register patient              | Register a patient with a unique ID and required name, then check they are stored correctly | Attempt to register another patient using an existing patient ID                                                                                  | Check the patient is stored with the correct details and that duplicate registration raises ValueError without overwriting the original patient             |
| FR-05 Prevent practitioner conflict | Schedule an appointment for a practitioner at a particular date and time.                   | Attempt to schedule another appointment for the same practitioner at the exact same date and time while the first appointment is still SCHEDULED. | Check that the first appointment is retained, the second booking raises ValueError, and a booking with a different practitioner at the same time is allowed |
| FR-06 Cancel appointment            | Cancel a scheduled appointment                                                              | Attempt to cancel an already cancelled appointment                                                                                                | Check that the status becomes CANCELLED for the valid cancellation and that a second cancellation raises ValueError                                         |
| FR-07 Retain cancelled history      | Cancel an appointment and then retrieve it from the appointment history                     | Attempt to cancel an appointment and check that it is not deleted from the history                                                                | Check that the same appointment remains retrievable with its original ID and CANCELLED status after cancellation                                            |

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
For each input/state, expected result and supporting contract: [response]

| Boundary/Edge Case             | Input/State                                                                                                                    | Output                                                                                             | Contract Supporting Expectation                                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Blank Identifier               | Register patient with ID `""` (empty string)                                                                                   | `ValueError('Expected a Patient object')`                                                          | Revision 2 FR-01                                                                                                          |
| White-Space Only Name          | Register patient with name `""` (empty string)                                                                                 | `ValueError(Patient Name cannot be blank')`                                                        | Revision 2 FR-01                                                                                                          |
| Same-Time Practitioner Booking | Book two appointments with the same practitioner at exactly 10:00 on the same date, with the first appointment still SCHEDULED | Reject the second booking and raise ValueError                                                     | FR-05, AC-04.1: a practitioner cannot have conflicting scheduled appointments at the same date and time                   |
| Cancelled Appointment          | Cancel an appointment, then check its status and retrieve it from the store                                                    | Its status becomes CANCELLED, and the appointment remains available in the current-session history | FR-06, AC-05.1, and FR-07, AC-05.2                                                                                        |
| Invalid Status Transition      | Cancel an appointment that is already CANCELLED, or one that is COMPLETED                                                      | Reject the cancellation and raise ValueError; the existing status must remain unchanged            | FR-06, AC-05.3 covers repeated cancellation. The domain contract should define which other status transitions are invalid |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
| --------- | ------------- | ------------------------ |
| 1 | It only asserts that the registered patient is not none. This passes even if the ID or name is wrong or empty, so it does not prove FR-01 (register patient) | Register patient P1 "Alexander Stewart," then check the data store returns that same patient with ID P1 and name 'Alexander Stewart". |
| 2 | Only asserts that the booked appointemnt is not None. It would pass with the wrong patient, practitioner, time or status, so it does not prove booking works. | Book Appointment1 (A1) for Patient1 (p1) with Practitioner1 (D1) at a fixed time, then check the stored appointment has that patient, that practitioner, that time and the status SCHEDULED. |
| 3 | Assert True always passes whatever the code does. It tests nothing and give false confidence | Cancel appotintment A1 and check its status is AppointmentStatus.CANCELLED (FR-06). Check the appointment is still in the data store (FR-07). |
| 4 | Assume an SMS is sent after booking. SMS is not in the requirements baseline and the project has no notification code, so the test checks a feature that does not exist. | Test a real rule instead. A second booking for the same practitioner at the same time is rejected with ValueError, and the store still holds only the first appointment (FR-05)|
| 5 | It assumes an SMS cancellation message is sent. Thos is also an unrequested feature, so it would need fake code just to pass | test the cancellation rules, cancelling an appointment twixe is rejected with ValueError, and the appointmentstays CANCELLED and unchanged.  |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[response]

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

Results recorded from `python -m pytest -v` run in `project/` on `main` at commit 71ef3a41e142c6bd836b597f2c651fb844194c89 (Python 3.14.3, pytest 8.3.5): 37 passed in 0.13s. The same run covers the eight supplied tests and the 29 student-authored tests listed above.

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID    | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
| ---------- | ----------- | -------------------- | ------------------------------ | -------------- | -------------------------- | ------------------------------------ |
| T-08 | FR-01 Register patient | Revision 2 validation contract (not AC-01.2): blank or invalid ID raises ValueError           | Negative and boundary                     | test_patient_id_must_not_be_blank_or_invalid: create a Patient with an empty ID, a spaces-only ID and None   | ValueError raised each time                 | The supplied test only tries one blank ID (a single space). This adds the empty string and None    |
| T-09 | FR-01 Register Patient  | AA-0.01 (partial, domain evidence only)           | Positive                     | test_patient_details_are_trimmed: create a Patient with " p1 " and " Test Patient "     | patient_id is "p1" and name is "Test Patient"                 | Shows stored values are trimmed. Companion tests also check the ID keeps its case and cannot be reassigned.                           |
| T-10 | FR-03 Register practitioner  | Supporting contract: ID, name and specialty are required  | Negative                     | test_practitioner_name_must_not_be_blank and test_practitioner_specialty_must_not_be_blank: try an empty and a spaces-only value  | ValueError raised each time | The supplied test only checks a blank specialty. This adds a blank name and spaces-only values. |
| T-11 | FR-04 Book appointment  | AC-03.1 (partial, domain evidence only) | Positive | test_new_appointment_is_scheduled: create an Appointment without giving a status | status is AppointmentStatus.SCHEDULED| Checks the default starting status directly in the domain object.  |
| T-12 | FR-04 Book appointment  | Revision 2 contract: real Patient and Practitioner, minute-precision local datetime| Negative and boundary | test_appointment_requires_valid_participants, test_appointment_requires_minute_precision, test_appointment_rejects_invalid_datetime and test_appointment_rejects_invalid_status: pass text instead of objects, a time with seconds, a string instead of a datetime, and a string instead of a status     | ValueError raised each time                 | Covers invalid participants, seconds in the time, a non-datetime and a non-enum status, none of which the supplied tests check.                           |
| T-13 | FR-06 Cancel appointment| AC-05.1 (domain)| Positive                     | test_scheduled_appointment_can_be_cancelled: create a SCHEDULED appointment and call cancel()| status becomes CANCELLED| Tests the domain rule on its own, with no services or data store.|
| T-14 | FR-06 Cancel appointment  | AC-05.3 (domain), plus COMPLETED guard| Negative| test_cancelled_appointment_cannot_be_cancelled_again and test_completed_appointment_cannot_be_cancelled: cancel twice, and cancel a COMPLETED appointment | ValueError raised, and the status stays CANCELLED or COMPLETED | Adds the COMPLETED case and checks the status is unchanged after the rejection.                           |
| T-15 | FR-02 Patient search  | AC-02.1 and AC-02.2 | Positive and negative                     | test_find_patient_returns_known_patient_and_rejects_unknown: look up P1, then look up P99 | P1 is returned with the right ID and name. P99 raises LookupError.| The supplied tests never call find_patient. This is the first test of the Stage 6 lookup. |
| T-16 | FR-02 Patient search  | Revision 2 contract: a blank ID is invalid, not absent| Boundary| test_find_patient_rejects_blank_ids: look up an empty ID and a spaces-only ID     | ValueError (not LookupError)| Separates "invalid input" from "not found".|
| T-17 | FR-03 Register practitioner  | Supporting contract: practitioner lookup | Positive and negative | test_find_practitioner_returns_known_and_rejects_unknown: look up D1, then D99 | D1 is returned with the right ID and name. D99 raises LookupError. | First test of find_practitioner, which the supplied tests never call.                          |
| T-18 | FR-05 Prevent practitioner conflict  | AC-04.1 boundary: conflict applies to the exact datetime only | Boundary                     | test_booking_conflict_only_applies_to_exact_datetime: book D1 at 10:00, try 10:00 again, then book 10:01     | 10:00 rejected with ValueError, store unchanged, 10:01 accepted | Shows the conflict rule is exact, not a time range, and that a rejected booking changes nothing. |
| T-19 | FR-05 Prevent practitioner conflict  | Supporting contract: a cancelled booking does not occupy the slot | Positive | test_cancelled_appointment_slot_can_be_reused: book 10:00, cancel it, book 10:00 again | The second booking succeeds and is SCHEDULED | shows only SCHEDULED appointments cause conflicts.                           |
| T-20 | FR-06 Cancel appointment  | AC-05.1 (service) | Positive | test_cancel_appointment_returns_cancelled_object: book A1, then cancel it through the service  | The same appointment object is returned with status CANCELLED | First test of the service cancel_appointment (a Stage 6 target). |
| T-21 | FR-07 Retain cancelled history  | AC-05.2 | Positive | test_cancelled_appointment_remains_in_history: cancel A1, then find it and list all appointments | A1 is found, CANCELLED, and still in the list | Proves cancellation keeps the record instead of deleting it. |
| T-22 | FR-06 Cancel appointment  | AC-05.3 (service), plus COMPLETED guard | Negative | test_repeated_and_completed_cancellation_are_rejected: cancel A1 twice, then cancel a COMPLETED appointment  | ValueError each time, with the status unchanged | Tests the guards through the service layer, not just the domain. |
| T-23 | FR-06 Cancel appointment | Supporting contract: unknown ID gives LookupError, blank ID gives ValueError | Boundary | test_cancel_appointment_rejects_unknown_and_blank_ids: cancel A99, then an empty and a spaces-only ID  | LookupError for A99, ValueError for blank IDs, and the real appointment stays SCHEDULED | Checks the different error types and that failed attempts leave state unchanged. |
| T-24 | FR-08 Appointment lookup  | AC-06.1 | Positive | test_find_appointment_returns_same_object: book A1, then find A1 | The same appointment object is returned | Confirms lookup returns the stored object, not a copy.  |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
| ------- | ------- | --- | ------ | ----------------------------------------------- |
| T-08 | Invalid patient IDs: "", " " and None | Construct Patient(id, "Test Patient") for each | pytest.raises(ValueError) each time | Proves blank and invalid IDs are rejected; it would fail if the constructor accepted an empty or None ID |
| T-13 | Patient P1, practitioner D1, new SCHEDULED appointment A1 | Call appointment.cancel() | status is CANCELLED | Checks the domain transition on its own; it would fail if status did not change |
| T-14 | A1 cancelled once; separate appointment built as COMPLETED | Call cancel() again; call cancel() on the COMPLETED one | ValueError each time; status stays CANCELLED and COMPLETED | Proves illegal transitions are rejected and state is unchanged |
| T-15 | Fresh store with registered P1 "Test Patient" | find_patient("P1"); find_patient("P99") | Result is the store's registered object, ID and name match; P99 raises LookupError | Identity check proves the actual registered object is returned, not a copy or replacement |
| T-18 | A1 booked for P1/D1 at 2026-11-05 10:00 | Book A2 at 10:00; then book A3 at 10:01 | A2 raises ValueError; list is [A1], A1 SCHEDULED; A3 accepted and two appointments stored | Proves conflict is the exact datetime only and a rejected booking changes nothing |
| T-19 | A1 booked at 10:00 and cancelled | Book A2 for the same practitioner and time | A2 stored, id "A2", SCHEDULED | Proves a cancelled booking no longer blocks the slot |
| T-20 | A1 booked | cancel_appointment("A1") | Returned object is A1 itself with status CANCELLED | Identity check proves the same object is cancelled, not recreated |
| T-21 | A1 booked then cancelled | find_appointment("A1"); list_appointments() | Found object is A1, CANCELLED; list equals [A1] | Proves history is retained instead of deleted (FR-07) |
| T-22 | A1 booked and cancelled; a COMPLETED appointment A2 added through the store with registered participants | cancel_appointment("A1") again; cancel_appointment("A2") | ValueError each time; A1 stays CANCELLED, A2 stays COMPLETED | Proves service-level guards and unchanged state after rejection |
| T-23 | A1 booked | cancel_appointment("A99"), then "" and " " | LookupError for A99; ValueError for blank IDs; list equals [A1]; A1 SCHEDULED | Separates unknown IDs from invalid IDs and shows failed attempts change nothing |
| T-24 | A1 booked | find_appointment("A1") | Result is A1 itself | Identity check shows the stored object is returned |                                    |

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

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
| ------- | ----------------- | -------- | ------ | ------ | --------------- | ----------------------------------------- | --------------------------- |
| `python -m pytest -v` | `project/` | 71ef3a41e142c6bd836b597f2c651fb844194c89 | 37 | 0 | None | None | Full suite on clean main after `git pull --ff-only` (Python 3.14.3, pytest 8.3.5): 8 supplied, 19 domain and 10 service tests, 37 passed in 0.13s. It shows the accumulated tests pass; it does not prove behaviour the tests do not check (see section K). |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? It does not test Stage 9 behaviour (query functions, the console menu), the main.py demo, or that data is lost at the end of a session. Within Stages 6-7 it also has no test for timezone-aware datetimes, for trimmed duplicate IDs such as registering " P1 " when P1 exists, for a COMPLETED appointment not blocking a slot, or for a blank appointment ID at booking.
Coverage if used: Not used.
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? The untested edge cases above are contract rules, so a defect there would pass the suite unnoticed. Coverage only counts lines executed, so a test with a weak or missing assertion still raises the percentage without detecting a wrong result.
Optional fixtures/parametrisation used and why, if any: A plain helper function, create_test_services(), builds a fresh data store and services for each test so setup is independent. pytest fixtures and parametrisation were not used. Loops over several invalid inputs stop at the first failure, whereas parametrisation would report each case separately.

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch     | PR         | Reviewer   | Key feedback | Outcome    |
| ---------- | ---------- | ---------- | ---------- | ------------ | ---------- |
| [complete] | [complete] | [complete] | [complete] | [complete]   | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member     | Actual contribution | Evidence link |
| ---------- | ------------------- | ------------- |
| [complete] | [complete]          | [complete]    |

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
Coverage tells us which lines or branches ran during tests. It doesn’t prove the assertions are meaningful or the behaviour correct.

8. What makes an assertion weak?
An assertion is weak when it would still pass if the behaviour were wrong, for example assert True, is not None, or a test that never checks the result.

9. What is the appropriate role of GitHub Copilot as a test assistant?
Copilot is a test assistant that suggests candidates. Each must be checked against the requirement, the assertions and an actual run, and it can’t replace human test design.

10. What is the Stage 7 engineering rule?
The Stage 7 engineering rule: every test traces to a real requirement, asserts specific required behaviour that could fail for the right reason, and counts as evidence only if it was actually run and recorded with its tested SHA.

## O Stage Completion

Tested Stage 7 main SHA: 71ef3a41e142c6bd836b597f2c651fb844194c89  Full-suite result: `python -m pytest -v` in project/: 37 passed, 0 failed (Python 3.14.3, pytest 8.3.5)  Unresolved defects and effect on baseline: None found by the Stage 7 suite  Clean working tree and integration evidence: `git status` clean on main after `git pull --ff-only` before the run  Stage 8 handover status: Stage 7 baseline complete; Stage 8 work is on a separate branch (debug/stage08)  All tutorial/formative responses and traceability/Copilot decisions complete: [confirm only after sections H and I are done]
