# Stage 6 activities and evidence
Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Tue 1:30 - 3:30 Group 1
- Members, GitHub usernames and cohorts: UG - Alicia Hurst - Blahuee, UG - Aagney Mani Sharma - Aagneyf1r3, UG - Ngedup Jigme Lhazeen - njlhazin
- Repository URL: https://github.com/Blahuee/st1-assignment-3
- Starting SHA: `78e45fe`

## Requirement to Issue Activities

### FR-02 Patient Search
- **Title:** Implement patient lookup by patient ID (FR-02)
- **Context:** SmartCare needs the ability to retrieve existing patient records so that other workflows can identify the correct patient. The current starter implementation in `PatientService.find_patient()` is incomplete.
- **Requirement:** Implement patient lookup by patient ID. The method must return the existing stored `Patient` object when the ID is valid and exists. It must also raise `ValueError` for a blank or invalid ID, and raise  `LookupError` when the patient does not exist. It must not create a replacement patient.
- **Acceptance criteria:** 
  - A valid existing patient ID returns the corresponding stored patient object
  - A blank or invalid patient ID raises `ValueError`
  - A valid ID that does not exist raises `LookupError`
  - Looking up a patient does not register, replace, or modify patient records
  - Existing patient records remain unchanged when a lookup fails.
- **Scope:** Implement `PatientService.find_patient()` in project/smartcare/services.py using the existing data store.
-  Add or update focused tests for successful lookup, invalid IDs, missing patients, and preservation of existing records. Do not change patient registration or introduce new storage mechanisms.
- **Definition of Done:**
  - Implementation meets the requirement and acceptance criteria
  - Relevant automated tests pass
  - Changes are committed on a feature branch and submitted through a pull request linked to this issue
  - Another group member reviews the actual diff, feedback is addressed, and approval is recorded before merging
  - The merged code is verified and the issue is closed
- **Owner:** Alicia
- **Actual issue link:** https://github.com/Blahuee/st1-assignment-3/issues/3#issue-5829342862

### FR-06 Appointment Cancellation with FR-07 retained history
- **Title:** Add Appointment Cancellation with retained history (FR-06 and FR-07) 
- **Context:** Clinic staff should cancel any appointments that are not supposed to happen, and they must keep a record of those cancellations for the rest of the session. Right now, the AppointmentService.cancel_appointment method is still a TODO in the starter code, which means cancellation isn't possible through the service layer yet.
  
- **Requirement:**
  -  FR-06 - Appointment cancellation
  - FR-07 - Retaining the appointment cancellation history 

- **Acceptance criteria:**
  - Cancelling a SCHEDULED appointment changes its status to CANCELLED and after the cancellation the same appointment can still be found by the IDs with status cancellation. Therefore, the schedule is not deleted and stored in the object. 
  - A blank or invalid ID raises a ValueError. 

- **Scope:**
  - Including the cancellation of appointment code into the code and also for retaining the memory then adding tests for it. 
  - Not included practitioner and patient lookup, rescheduling and deleting appointments. 

- **Definition of Done:**
  - Cancel appointment meets all the requirements 
  - Tests cover cancellation successfully and history is retained after cancelling. 

- **Owner:** Ngedup
- **Actual issue link:** https://github.com/Blahuee/st1-assignment-3/issues/1#issue-5828750575 

## B Commit quality
| Original example                               | Strong or Weak | Reason                                                                                              |
| ---------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------- |
| Changes                                        | Weak           | Does not describe what was changed, this makes it difficult to understand the purpose of the commit |
| Final version                                  | Weak           | Does not explain what was finalised or what changes were made                                       |
| Add patient search by ID                       | Strong         | Clearly describes what feature was worked on                                                         |
| Fix stuff                                      | Weak           | Vague and does not indicate what was fixed                                                          |
| Prevent cancellation of completed appointments | Strong         | Clearly describes the behaviour being changed                                                       |

## C Over scoped PR review
A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: The PR includes unrelated changes that could increase the complexity and make it harder to review the appointment cancellation feature
- Responsibility and architecture concerns: Renaming and restructuring unrelated code could break existing functionality. Cancellation should use the existing appointment service and domain logic where applicable.
- Testing and review concerns: Any code changes must be tested again before merging. Unrelated changes increase the testing required and passing tests do not guarantee that all changes are necessary or that the code is well designed.
- Changes to remove or separate, with reasons: Keep the changes needed for appointment cancellation. Remove unrelated patient field renaming and code restructuring, or move them into separate PR's. Remove the dependency if its unnecessary. After making these changes, rerun the relevant tests and review the final code before merging.

## D Challenge a weak Copilot review
GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: The comment doesn’t say which requirement or acceptance criteria were checked, or which code changes were reviewed. It gives no test command, folder or result, so “tests pass” is just a claim and Copilot hasn’t actually run the tests. It also doesn’t say whether the tests check anything meaningful, whether error cases were looked at, whether there are unrelated changes, or what wasn’t checked.
- Follow-up review question 1: Which requirement and acceptance criteria did you compare the changes against and which ones are met?
- Follow-up review question 2: What exact command ran the tests, in which folder and on which commit and what was the result?
- Follow-up review question 3: Do the test assertions check specific values or errors and would they fail if the code behaved incorrectly?
- Follow-up review question 4: What happens with a blank, invalid or unknown ID, or an invalid appointment state and does the stored data stay unchanged afterwards?
- Follow-up review question 5: Does the change include anything unrelated to the issue and does each part of the code (service, domain object, data store) keep its own job?
- Additional questions if useful: What did you not check and how could someone verify your conclusion independently?

## E Team workflow agreement
| Practice                            | Team agreement |
| ----------------------------------- | -------------- |
| Branch naming                       | Use descriptive names with prefixes, such as feature/patient-search, feature/appointment-cancellation and documentation/stage06. Each member works on their own branch rather than directly on main. |
| Commit message convention           | Use short, descriptive messages that explain what changed, such as Implement patient search by ID or Add appointment cancellation tests. Avoid vague messages such as updates or final version. |
| PR size                             | Keep pull requests focused on one issue or feature you are assigned. Avoid unrelated changes to other features/areas. |
| Another-member review requirement   | Every PR must be reviewed by at least one other group member. The reviewer checks the code diff, tests and acceptance criteria, and provides feedback before approval. |
| Merge rule                          | Merge into main only after the PR has been reviewed, feedback addressed and relevant tests passed. Do not push directly to main. Resolve conflicts and retest before merging. Add comments going over review and merge approval in PR |
| Significant Copilot disclosure rule | Record significant Copilot assistance in the assignment evidence document, including what it suggested, how the team evaluated it, what was accepted or changed, and how the result was verified. Team members remain responsible for their submitted code. |

## F Issue and backlog index
Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner      | Acceptance criteria or precise link | Status     |
| ---------- | ----------- | ---------- | ----------------------------------- | ---------- |
| [Implement patient lookup by patient ID (FR-02)](https://github.com/Blahuee/st1-assignment-3/issues/3#issue-5829342862)  | Implement patient lookup by patient ID. The method must return the existing stored Patient object when the ID is valid and exists. It also must raise ValueError for a blank or invalid ID LookupError when the patient does not exist. It must not create a replacement patient.  | Alicia |  A valid existing patient ID returns the corresponding stored patient object. A blank or invalid patient ID raises ValueError. A valid ID that does not exist raises LookupError. Looking up a patient does not register, replace, or modify patient records. Existing patient records remain unchanged when lookup fails.                          |Completed |
| [Add Appointment Cancellation with retained history (FR-06 and FR-07)](https://github.com/Blahuee/st1-assignment-3/issues/1#issue-5828750575)  | FR-06 - Appointment cancellation. FR-07 - Retaining the appointment cancellation history  | Ngedup | Cancelling a SCHEDULED appointment changes its status to CANCELLED and after the cancellation the same appointment can still be found by the IDs with status cancellation. Therefore, the schedule is not deleted and stored in the object. A blank or invalid ID raises a ValueError. | Completed |

## G Pull request evidence
- **PR link and title:** https://github.com/Blahuee/st1-assignment-3/pull/8, "Implement Patient Search by ID"
- **Linked issue and requirement:** Issue #3 (https://github.com/Blahuee/st1-assignment-3/issues/3), FR-02 Patient Search
- **Feature branch:** feature/patient-search
- **Changed behaviour:** The commit implements the `find_patient()` method by replacing the `NotImplementedError` placeholder with a call to the data store. It returns the existing patient when found and raises a `LookupError` when the patient does not exist. This allows the service to retrieve patients without creating replacement records.
- **Meaningful commits:** https://github.com/Blahuee/st1-assignment-3/commit/e514dda
- **Test command, directory and observed result:** From `project/`, ran `python main.py` successfully. Then ran `python -m pytest`, which reported 8 passed.
- **Another-member reviewer:** Aagney (over video call) but pushed/merged by Alicia
- **Human observations recorded before Copilot:** None recorded.
- **Requirement, responsibilities, test assertions and unrelated-scope checks:** The PR diff was limited to services.py, with no unrelated files changed. Although Aagney provided informal feedback during a video call, no documented requirement-to-test mapping, dedicated patient lookup assertions or explicit unrelated-scope review was recorded. The eight baseline tests passed but did not verify the Stage 6 service TODOs.
- **Key feedback:** None recorded.
- **Author response/change and verification:** Not applicable.
- **Reviewer recheck and approval:** No approval recorded; the author merged the PR.
- **Merge outcome and SHA:** Merged into main on 2026-10-20, b5ddb1760ac109c6d742b2c485906e4e55d615df
- **Significant Copilot assistance:** None recorded.
- **Linked issue closure:** Issue #3 Closed
- **Each member updated main:**
  - Alicia: Confirmed, updated successfully
  - Aagney: Confirmed, updated successfully
  - Ngedup: Confirmed, updated successfully
- **Integrated verification after merge:** e514dda244cfbf256642a0eed7fe8d9bcf9f45d0

- **PR link and title:** https://github.com/Blahuee/st1-assignment-3/pull/9, "Implement Practitoner Search by ID"
- **Linked issue and requirement:** Linked on the PR to issue #1 (FR-06/FR-07). The PR implements practitioner lookup, which has no separate issue yet.
- **Feature branch:** feature/appointment-cancellation
- **Changed behaviour:** The commit implements the `find_practitioner()` method by replacing the `NotImplementedError` placeholder with a call to the data store. It returns the existing practitioner when found and raises a `LookupError` when the practitioner does not exist. This allows the service to retrieve practitioners without creating replacement records.
- **Meaningful commits:** https://github.com/Blahuee/st1-assignment-3/commit/82f2b21
- **Test command, directory and observed result:** None recorded on the PR.
- **Another-member reviewer:** None. The PR shows no reviews (author: Blahuee).
- **Human observations recorded before Copilot:** None recorded.
- **Requirement, responsibilities, test assertions and unrelated-scope checks:** None recorded on the PR.
- **Key feedback:** None recorded.
- **Author response/change and verification:** Not applicable.
- **Reviewer recheck and approval:** No approval recorded; the author merged the PR.
- **Merge outcome and SHA:** Merged into main on 2026-10-20, c99841ef7c2899ec677090ec2f9814dd69411db0
- **Significant Copilot assistance:** None recorded.
- **Linked issue closure:** Issue #1 remains open; this PR does not implement cancellation.
- **Each member updated main:**
  - Alicia: Confirmed, updated successfully
  - Aagney: Confirmed, updated successfully
  - Ngedup: Confirmed, updated successfully
- **Integrated verification after merge:** e514dda244cfbf256642a0eed7fe8d9bcf9f45d0

- **PR link and title:** https://github.com/Blahuee/st1-assignment-3/pull/10, "Stage 06 F issue and backlog index"
- **Linked issue and requirement:** None linked. Section F (issue and backlog index) of the Stage 6 record, which supports the issue-to-PR traceability requirement.
- **Feature branch:** documentation/stage06
- **Changed behaviour:** None. Documentation only (2 commits, 1 file, +2/−2).
- Meaningful commits: https://github.com/Blahuee/st1-assignment-3/commit/d2fb1b3 and https://github.com/Blahuee/st1-assignment-3/commit/d6c248d ("issue link updated")
- **Test command, directory and observed result:** Not applicable (documentation only).
- **Another-member reviewer:** Aagneyf1r3 (author: njlhazin). Blahuee was also requested and did not submit a review.
- **Human observations recorded before Copilot:** Aagneyf1r3 submitted a review requesting changes on the PR https://github.com/Blahuee/st1-assignment-3/pull/10#pullrequestreview-5580903010. No Copilot was used.
- **Requirement, responsibilities, test assertions and unrelated-scope checks:** The review checked that the backlog table linked to the actual GitHub issues.
- **Key feedback:** "put the issue links https://github.com/Blahuee/st1-assignment-3/pull/10#pullrequestreview-5580903010".
- **Author response/change and verification:** njlhazin pushed commit d6c248d "issue link updated".
- **Reviewer recheck and approval:** No re-review or formal approval recorded after the update; Aagneyf1r3 merged the PR after the update.
- **Merge outcome and SHA:** Merged into main on 2026-10-20, f5725d7f5621dbd684133bb2e4235e9d09894027
- **Significant Copilot assistance:** None recorded.
- **Linked issue closure:** Not applicable.
- **Each member updated main:**
  - Alicia: Confirmed, updated successfully
  - Aagney: Confirmed, updated successfully
  - Ngedup: Confirmed, updated successfully
- **Integrated verification after merge:** f5725d7f5621dbd684133bb2e4235e9d09894027

- **PR link and title:** PR #15 – Add Appointment Cancellation
- **Linked issue and requirement:** Issue #1 – Add Appointment Cancellation with retained history. FR-06 (Appointment Cancellation) and FR-07 (retained appointment history).
- **Feature branch:** feature/appointment-cancellation (merged into main).
- **Changed behaviour:** Implemented AppointmentService.cancel_appointment() to cancel an existing appointment and return the cancelled appointment object. Unknown appointment IDs raise LookupError. Invalid cancellation transitions raise ValueError without changing the appointment's existing state.
- **Test command, directory and observed result:** Run from the project/ directory:
  - **Command:** python -m pytest
  - **Expected verification:** tests pass, including appointment cancellation, unknown appointment IDs and invalid cancellation transitions.
- **Another-member reviewer:** Aagneyf1r3 commented "All good" on the PR. GitHub shows no formal review submission.
- **Human observations recorded before Copilot:** The cancellation service needed to delegate the operation to the existing appointment/domain logic, return the cancelled object and preserve the appointment's history. Unknown IDs and invalid state transitions needed separate handling.
- **Requirement, responsibilities, test assertions and unrelated-scope checks:** The change addresses FR-06 and FR-07. The service is responsible for locating the appointment and delegating cancellation. Assertions should verify the returned appointment, its cancelled status, `LookupError` for unknown IDs, `ValueError` for invalid transitions and unchanged state after a failed cancellation. Unrelated patient and practitioner functionality should remain unchanged.
- **Key feedback:** The reviewer responded "All good". No formal review comments or requested code changes are visible on GitHub.
- **Author response/change and verification:** The author implemented the requested appointment cancellation behaviour in `AppointmentService.cancel_appointment()`. The PR description confirms the expected exception handling and that invalid transitions leave the appointment state unchanged. The PR was subsequently merged.
- **Reviewer recheck and approval:** Aagneyf1r3 commented "All good". No formal GitHub approval review is recorded.
- **Merge outcome and SHA:** Merged into main on 3 November 2026. Merge commit: 5244ad3.
- **Significant Copilot assistance:** None recorded
- **Linked issue closure:** Issue #1 was automatically linked to the PR and is now closed.
- **Each member updated main:**
  - Alicia: Confirmed, updated successfully
  - Aagney: Confirmed, updated successfully
  - Ngedup: Confirmed, updated successfully
- **Integrated verification after merge:** Needs confirmation that the group ran python -m pytest from project/ against the updated main branch and recorded the results.

## H Copilot collaboration record
Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: Ngedup Jigme Lhazeen, retrospective Copilot review of the PR #15 diff (commit 0522007, `AppointmentService.cancel_appointment()` in services.py), run on 9 Nov 2026 after the PR was merged.
- Prompt/purpose and relevant issue/diff: Asked Copilot to review the diff against issue #1 (FR-06 cancel appointment and FR-07 retained history) and to give a Met / Partially met / Not met result for AC-05.1, AC-05.2 and AC-05.3, flag unrelated changes and not claim tests passed. I pasted the diff, the unchanged `Appointment.cancel()` method and a description of `find_appointment()`. The purpose was a second opinion after the human review.
- Summary of output: Copilot rated AC-05.1, AC-05.2 and AC-05.3 as Met and all FR-06 and FR-07 points as Met. It found no unrelated functional change (only a docstring wording cleanup). It noted two minor points: the service relies on the data store to reject blank IDs, and the docstring does not mention blank IDs. It stated it reviewed code only and did not run tests.
- Human check against actual code, requirements and tests: I checked the claims against the real code at merge commit 5244ad3. The service calls `data_store.find_appointment()`, raises LookupError if the result is None, calls `appointment.cancel()` and returns the same object. `Appointment.cancel()` raises ValueError unless the status is SCHEDULED and leaves state unchanged. `find_appointment()` returns None for an unknown ID and raises ValueError for a blank ID, so Copilot's reading was correct. The PR changed only services.py. The 8 supplied tests do not call `cancel_appointment()` directly, so no test covered it when the PR was merged. Copilot's "Met" results are code-reading conclusions, based on the code I pasted.
- Decision — Accept / Modify / Reject: Modify
- Reason: I accepted Copilot's acceptance-criteria results, because the code supports them. I did not act on the docstring point, because the behaviour is correct and the blank-ID rule is already documented in the data store. I added what Copilot could not give: test evidence.
- Verification/evidence: `python -m pytest` from `project/` at merge commit 5244ad3: 8 passed (these did not call `cancel_appointment()` directly). Later, Stage 7 tests T-20 to T-23 in test_services.py check this method directly (cancel returns the same CANCELLED object, history is retained, repeated and COMPLETED cancellation raise ValueError, unknown ID raises LookupError, blank ID raises ValueError). The full suite passed 37 tests on main.
  
## I Human versus Copilot review comparison
- Human reviewer noticed before consulting Copilot: The service must delegate to the domain method, return the cancelled object and keep the appointment in history. Unknown IDs and invalid transitions need separate handling. The diff touches only services.py.
- Copilot noticed: All acceptance criteria were met by the diff. It also noticed that the service relies on the data store to reject blank IDs, and that the docstring does not mention blank IDs raising ValueError.
- Overlap: Both reviews found that the service delegates to the domain, returns the same stored object, raises LookupError for an unknown ID, and has no unrelated functional change.
- What did the human reviewer notice that Copilot did not: That the 8 supplied tests do not call `cancel_appointment()` directly, so none of the acceptance criteria were tested by an assertion at merge time. Copilot reviewed only the code.
- What did Copilot identify that the human reviewer initially missed: The docstring wording point (blank IDs are not mentioned). It is minor and does not change behaviour.
- Unsupported or incorrect Copilot suggestion: None identified. One limitation is that Copilot could only use the code I pasted, so its "Met" results for AC-05.2 and the blank-ID rule were inferred from my description of the data store, not from running anything.
- Human judgement accepted, modified or rejected, and why: Modified. I accepted the acceptance-criteria results and the lack of unrelated changes. I did not change the docstring, because behaviour is already correct and documented elsewhere. I added test evidence.
- Which evidence justified merge approval: Aagney's "All good" comment on PR #15, the diff limited to services.py, and 8 passed at merge commit 5244ad3. No formal approval review is recorded.

## J Contributions
Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

## J Contributions
Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: Alicia Hurst (Blahuee)
- Implementation: Implemented patient lookup (commit e514dda, PR #8), practitioner lookup (82f2b21, PR #9), the cancellation service (0522007, PR #15) and the docstring cleanup (d5c2465, PR #12), all in services.py.
- Testing: Ran `python main.py` and `python -m pytest` for PR #8 (8 passed).
- Review: Merged PRs #8, #9, #12 and #13. PRs #8, #9 and #12 have no recorded review. Requested as a reviewer on PR #10, but no review was submitted.
- Issue refinement: Created the FR-02 patient search issue (commit 6ad1408).
- Design and responsibility discussion: Wrote the Section C review of an over-scoped PR, which separates service, domain and data store responsibilities (cancellation should use the existing service and domain logic, and unrelated changes belong in separate PRs). Also wrote Section E, the team workflow agreement on branching, PR size, review and merge rules (commit "Completed questions in section B, C and E").
- Debugging or integration: Merged and integrated PRs #8, #9 and #12 into main.
- Documentation or team support: Completed tutorial Sections B, C and E (commit "Completed questions in section B, C and E") and updated Section G with push and merge information (commit 31546b5).

- Member: Aagney Mani Sharma (Aagneyf1r3)
- Implementation: Not applicable (no project code in Stage 6)
- Testing: Not applicable
- Review: Reviewed PR #8 informally on a video call. Requested changes on PR #10 (the backlog needed the issue links). Commented "All good" on PR #15.
- Issue refinement: Not applicable
- Design and responsibility discussion: Not applicable
- Debugging or integration: Merged PRs #4, #7, #10, #11 and #15 into main.
- Documentation or team support: Wrote Section D (Copilot review challenge, commit fabd0b5) and the first draft of Section G (commit 45d409e).

- Member: Ngedup Jigme Lhazeen (njlhazin)
- Implementation: Not applicable. Issue #1 lists Ngedup as owner, but the cancellation code was committed by Alicia (0522007).
- Testing: Not applicable
- Review: Not applicable (no recorded review in Stage 6)
- Issue refinement: Wrote the issue #1 entry (FR-06 and FR-07, commit 3609a6b) and the issue and backlog index in Section F (commits d2fb1b3, d6c248d, 6f62835, 1d32cd5).
- Design and responsibility discussion: Not applicable
- Debugging or integration: Opened PR #10 and PR #11, and updated main after the merges.
- Documentation or team support: Fixed typos and completed parts of the Stage 6 record (commit 1d32cd5).
- 
## K Exit question
**Why is a high commit count not necessarily evidence of strong contribution?**\
A high commit count only shows how often someone saved changes, not how useful those changes were. Someone can make many tiny, cosmetic or repeated commits and look busy, while another person makes one precise review comment or test that prevents a serious bug. Real contribution includes implementation, testing, debugging, reviewing, design discussion,helping teammates and each should be backed by links to actual diffs, assertions or comments.

## L Stage 6 formative questions
1. **What is version control?**\
A system that records changes to files over time. It lets a team see the history, compare versions, recover earlier work and collaborate without overwriting each other.

2. **Why is a feature branch useful?**\
It keeps one focused change separate from "main" while it’s being built and reviewed. That protects the shared working version and makes each change easy to review.

3. **What makes a commit a good engineering commit?**\
It’s one coherent change with a clear message that says what and why. It’s tested, contains no unrelated edits or secrets, and is small enough to review.

4. **What is a pull request?**\
A request on GitHub to merge one branch into another, such as a feature branch into "main". It’s where the change is described, linked to an issue, discussed and reviewed before merging.

5. **What is the purpose of code review?**\
To have another person check the actual change against the requirement. They look for defects, weak tests, unrelated changes and responsibility problems, and the review also spreads understanding of the code across the team.

6. **What does a Git diff show?**\
The exact lines added and removed between two versions, such as the working tree versus the last commit, or a branch versus "main". It lets you check that every change has a purpose.

7. **What is a Definition of Done?**\
A checklist of what must be true before a piece of work counts as finished. Here that means the criteria are met, the tests pass, another member has reviewed and approved it, and it’s merged and verified.

8. **What is the appropriate role of GitHub Copilot in pull-request review?**\
It’s a support tool that gives a second opinion after the human review. Its suggestions must be checked against the code, requirements and tests, and each is accepted, modified or rejected with a reason. It can’t approve a PR or replace the review by another member.

9. **Why should individual contribution not be judged only by commit count?**\
Commit count ignores quality and the kind of work. Reviewing, testing, debugging, design and mentoring don’t always produce many commits, and counts can be inflated with trivial commits.

10. **What is the Stage 6 engineering rule?**\
The rule is that every change is traceable and evidence-based. A requirement goes into an issue, gets built on a focused branch with meaningful tests, then is reviewed on the actual diff by a different member and is merged only after approval from another member. Then everyone verifies the integrated main. Nothing, including Copilot’s output, counts as correct without evidence being checked properly.

## M Completion and handover
- Starting SHA: `78e45fe`
- Final Stage 6 code SHA: `5244ad3d03d6d49cd7146af7edd06a7134f3ac31` (merge of PR #15, the last Stage 6 code change)
- Test command: `python -m pytest`
- Working directory: `project/`
- Observed result: 8 passed (run retrospectively on 9 Nov 2026 at 5244ad3; the supplied starter tests)
- PR and another-member reviewer: PR #15 (https://github.com/Blahuee/st1-assignment-3/pull/15), Aagney commented "All good" with no formal review; PR #10 (https://github.com/Blahuee/st1-assignment-3/pull/10), Aagney reviewed and requested changes; PR #8 (https://github.com/Blahuee/st1-assignment-3/pull/8), informal review by Aagney on a video call. PRs #9 and #12 have no recorded review.
- Unresolved issue or none: PRs #8, #9 and #12 were merged by the author without a recorded review, which did not follow the Section E agreement. Practitioner lookup (PR #9) has no issue of its own and was linked to issue #1. The Copilot comparison was done retrospectively after the merge. The supplied tests did not call the three service methods directly; Stage 7 tests T-15, T-17 and T-20 to T-24 now cover them.
- Stage 7 handover status: ready. The Stage 7 record was merged to main in PR #22.
- Final submitted SHA if later than tested SHA: Later commits changed only documentation (the Stage 7 and Stage 8 records); the Stage 6 service code is unchanged since 5244ad3.

- [x] Three Stage 6 service targets completed and checked.
- [x] Original supplied tests retained and passing.
- [x] At least two focused issues link requirements and acceptance criteria.
- [x] Feature work reviewed by another member using the actual diff.
- [x] Human-first review and required Copilot comparison recorded.
- [x] Feedback resolved and approval recorded before merge.
- [x] Everyone pulled main and integrated checks passed.
- [x] Required activities, quiz responses and contribution notes completed.
- [x] Only synthetic data included; confidential peer material kept out.
- [x] Tutor can trace a requirement through issue, code, tests, PR and checkpoint

**Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.**