# Stage 6 activities and evidence
Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Tue 1:30 - 3:30 Group 1
- Members, GitHub usernames and cohorts: UG - Alicia Hurst - Blahuee, UG - Aagney Mani Sharma - Aagneyf1r3, UG - Ngedup Jigme Lhazeen - njlhazin
- Repository URL: https://github.com/Blahuee/st1-assignment-3
- Starting SHA: `78e45fe`

## A Requirement to issue activities

### FR-02 Patient Search
- **Title:** Implement patient lookup by patient ID (FR-02)
- **Context:** SmartCare needs to have the ability to retrieve existing patient records so other workflows can identify the correct patient. The current starter implementation in `PatientService.find_patient()` is incomplete
- **Requirement:** Implement patient lookup by patient ID. The method must return the existing stored `Patient` object when the ID is valid and exists. It also must raise `ValueError` for a blank or invalid ID `LookupError` when the patient does not exist. It must not create a replacement patient.
- **Acceptance criteria:** 
  - A valid existing patient ID returns the corresponding stored patient object
  - A blank or invalid patient ID raises `ValueError`
  - A valid ID that does not exist raises `LookupError`
  - Looking up a patient does not register, replace, or modify patient records
  - Existing patient records remain unchanged when lookup fails
- **Scope:** Implement `PatientService.find_patient()` in `project/smartcare/services.py` by using project/smartcare/services.py using the existing data store. Add or update focused tests for successful lookup, invalid IDs, missing patients, and preservation of existing records. Do not change patient registration or introduce new storage mechanisms
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
| changes                                        | Weak           | Does not describe what was changed, this makes it difficult to understand the purpose of the commit |
| final version                                  | Weak           | Does not explain what was finalised or what changes were made                                       |
| Add patient search by ID                       | Strong         | Clearly descibes what feature was worked on                                                         |
| fix stuff                                      | Weak           | Vague and does not indicate what was fixed                                                          |
| Prevent cancellation of completed appointments | Strong         | Clearly describes the behaviour being changed                                                       |

## C Over scoped PR review
A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: The PR includes unrelated changes that could increase the complexity and make it harder to review the appointment cancellation feature
- Responsibility and architecture concerns: Renaming and restructuring unrelated code could break existing functionality. Cancellation should use the existing appointment service and domain logic where applicable.
- Testing and review concerns: Any code changes must be tested again before merging. Unrelated changes increase the testing required and passing tests do not guarantee that all changes are necessary or that the code is well designed.
- Changes to remove or separate, with reasons: Keep the changes needed for appointment cancellation. Remove unrelated patient field renaming and code restructuring, or move them into separate PR's. Remove the dependency if its unnecessary. After making these changes, rerun the relevant tests and review the final code before merging.

## D Challenge a weak Copilot review
GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: [response]
- Follow-up review question 1: [response]
- Follow-up review question 2: [response]
- Follow-up review question 3: [response]
- Follow-up review question 4: [response]
- Follow-up review question 5: [response]
- Additional questions if useful: [response]

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
| [issue 1]  | [response]  | [response] | [response]                          | [response] |
| [issue 2]  | [response]  | [response] | [response]                           | [response] |

## G Pull request evidence
Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record
Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison
- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions
Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

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
- Final Stage 6 code SHA:
- Test command: `python -m pytest`
- Working directory: `project/`
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint

**Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.**