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


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: [complete]
- Baseline test command / working directory / observed result / evidence: [complete]
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint                                     | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
| ---------------------------------------------- | ------------------------ | ----------------------------- | ------------------------------------ |
| F8-01 before repair                            | [complete]               | [complete]                    | [complete]                           |
| F8-01 after repair                             | [complete]               | [complete]                    | [complete]                           |
| F8-02 before repair                            | [complete]               | [complete]                    | [complete]                           |
| F8-02 after repair                             | [complete]               | [complete]                    | [complete]                           |
| Full suite after both repairs, before refactor | [complete]               | [complete]                    | [complete]                           |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

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
