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
| 1         | [response]    | [response]               |
| 2         | [response]    | [response]               |
| 3         | [response]    | [response]               |
| 4         | [response]    | [response]               |
| 5         | [response]    | [response]               |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[response]

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
| ----------- | -------------------- | ------- | --------- | -------------------- | ------------------ | ------------------------ | ---------------------------- |
| FR-01 Register patient | Revision 2 validation contract (not AC-01.2): blank required values raise ValueError | T-01 | Domain, negative |  | Blank patient ID and blank practitioner specialty raise ValueError |  | Supplied |
| FR-01 Register patient | AC-01.2 Registration with an existing patient ID is rejected | T-02 | Service, negative |  | ValueError raised; original patient and name unchanged |  | Supplied |
| FR-03 Register practitioner | Supporting contract: duplicate practitioner ID is rejected | T-03 | Service, negative |  | ValueError raised; original practitioner unchanged |  | Supplied |
| FR-04 Book appointment | AC-03.1 Registered participants, unique ID and free time produce a stored SCHEDULED appointment | T-04 | Service, positive |  | Appointment found by ID, SCHEDULED and stored |  | Supplied |
| FR-04 Book appointment | AC-03.2 Booking an unknown patient or practitioner is rejected | T-05 | Service, negative |  | LookupError for unknown patient; nothing stored |  | Supplied |
| FR-05 Prevent practitioner conflict | AC-04.1 and AC-04.2 Same practitioner, exact time and SCHEDULED conflicts; another practitioner is allowed | T-06 | Service, positive and negative |  | Same practitioner and time rejected; different practitioner at same time allowed |  | Supplied |
| FR-06 Cancel appointment | AC-05.1 and AC-05.3 (domain evidence only) | T-07 | Domain, positive and negative |  | cancel() changes status to CANCELLED; second cancel raises ValueError |  | Supplied |
| FR-01 Register patient | Revision 2 validation contract: IDs are trimmed and non-blank; blank or invalid raises ValueError | T-08 | Domain, negative and boundary |  | ValueError for empty, spaces-only and tab-only patient IDs |  | Student-authored |
| FR-01 Register patient | AC-01.1 Valid required patient data is stored (partial: domain evidence only) | T-09 | Domain, positive |  | patient_id and name are stored trimmed |  | Student-authored |
| FR-03 Register practitioner | Supporting contract: practitioner requires ID, name and specialty | T-10 | Domain, negative |  | Blank name or blank specialty raises ValueError |  | Student-authored |
| FR-04 Book appointment | AC-03.1 (partial: domain evidence only) | T-11 | Domain, positive |  | New appointment status is SCHEDULED |  | Student-authored |
| FR-04 Book appointment | Revision 2 contract: local datetime at minute precision; real Patient and Practitioner required | T-12 | Domain, negative and boundary |  | ValueError for a non-Patient, non-Practitioner or a time with seconds |  | Student-authored |
| FR-06 Cancel appointment | AC-05.1 Cancelling a SCHEDULED appointment changes it to CANCELLED (domain) | T-13 | Domain, positive |  | Status becomes CANCELLED |  | Student-authored |
| FR-06 Cancel appointment | AC-05.3 Repeated cancellation is rejected (domain), plus COMPLETED guard | T-14 | Domain, negative |  | ValueError for CANCELLED and COMPLETED; status unchanged |  | Student-authored |
| FR-02 Patient search | AC-02.1 and AC-02.2 Known patient lookup succeeds; unknown lookup reports absence | T-15 | Service, positive and negative |  | Known ID returns the same Patient object; unknown valid ID raises LookupError |  | Student-authored |
| FR-02 Patient search | Revision 2 contract: a blank ID is invalid, not absent | T-16 | Service, boundary |  | ValueError (not LookupError) for blank and whitespace-only IDs |  | Student-authored |
| FR-03 Register practitioner | Supporting contract: practitioner lookup over registered objects | T-17 | Service, positive and negative |  | Known ID returns the same Practitioner; unknown valid ID raises LookupError |  | Student-authored |
| FR-05 Prevent practitioner conflict | AC-04.1 boundary: conflict applies to the exact datetime only | T-18 | Service, boundary |  | Same time rejected; one minute later accepted; rejected booking leaves state unchanged |  | Student-authored |
| FR-05 Prevent practitioner conflict | Supporting contract: a cancelled booking does not occupy the slot | T-19 | Service, positive |  | Rebooking the same practitioner and time succeeds after cancellation |  | Student-authored |
| FR-06 Cancel appointment | AC-05.1 Cancelling a SCHEDULED appointment changes it to CANCELLED (service) | T-20 | Service, positive |  | Same appointment object returned with status CANCELLED |  | Student-authored |
| FR-07 Retain cancelled history | AC-05.2 Cancelled history remains retrievable in the current session | T-21 | Service, positive |  | Cancelled appointment still found by ID and in the list, status CANCELLED |  | Student-authored |
| FR-06 Cancel appointment | AC-05.3 Repeated cancellation is rejected (service), plus COMPLETED guard | T-22 | Service, negative |  | ValueError for repeated or COMPLETED cancellation; state unchanged |  | Student-authored |
| FR-06 Cancel appointment | Supporting contract: unknown valid ID raises LookupError; blank ID raises ValueError | T-23 | Service, boundary |  | LookupError for unknown ID; ValueError for blank ID; nothing changes |  | Student-authored |
| FR-08 Appointment lookup | AC-06.1 A known appointment ID returns that appointment | T-24 | Service, positive |  | Returns the same appointment object |  | Student-authored |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID    | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
| ---------- | ----------- | -------------------- | ------------------------------ | -------------- | -------------------------- | ------------------------------------ |
| [complete] | [complete]  | [complete]           | [complete]                     | [complete]     | [complete]                 | [complete]                           |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID    | Arrange    | Act        | Assert     | Why meaningful / why assertion proves criterion |
| ---------- | ---------- | ---------- | ---------- | ----------------------------------------------- |
| [complete] | [complete] | [complete] | [complete] | [complete]                                      |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID    | Behaviour  | Test file/function | Result     |
| ---------- | ---------- | ------------------ | ---------- |
| [complete] | [complete] | [complete]         | [complete] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID    | Behaviour  | Requirement / criterion | Test file/function | Result     |
| ---------- | ---------- | ----------------------- | ------------------ | ---------- |
| [complete] | [complete] | [complete]              | [complete]         | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour  | Boundary/invalid input | Expected result | Test ID    |
| ---------- | ---------------------- | --------------- | ---------- |
| [complete] | [complete]             | [complete]      | [complete] |

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

| Command    | Working directory | Code SHA   | Passed     | Failed     | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
| ---------- | ----------------- | ---------- | ---------- | ---------- | --------------- | ----------------------------------------- | --------------------------- |
| [complete] | [complete]        | [complete] | [complete] | [complete] | [complete]      | [complete]                                | [complete]                  |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

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
[response]

2. What question does validation answer?
[response]

3. What is a unit test?
[response]

4. What is a pytest fixture?
[response]

5. What is parametrisation in pytest?
[response]

6. What is regression testing?
[response]

7. What does code coverage tell us, and what does it not prove?
[response]

8. What makes an assertion weak?
[response]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[response]

10. What is the Stage 7 engineering rule?
[response]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
