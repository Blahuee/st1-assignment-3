# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Tue 1:30 - 3:30 Group 1
Members and UG/PG applicability: UG - Alicia Hurst - Blahuee, UG - Aagney Mani Sharma - Aagneyf1r3, UG - Ngedup Jigme Lhazeen - njlhazin. All UG, so this release is common scope only. Stages 10 and 11 stay unchanged as intentionally not applicable.


## A Release scope and starting SHA

Release label/version and requirements baseline: SmartCare A3 common release, requirements baseline Revision 2. [TO DO group: agree the version label, e.g. v1.0-common]
Common starting SHA / branch / applicable members: [TO DO after Stage 9: SHA of main once Stage 9 is merged] / main / all three UG members. Pre-Stage 9 reference point: `c900456`.
PG starting SHA / branch / applicable members or not applicable: Not applicable. UG-only group.
Working-state review and approved integration: [TO DO after Stage 9: confirm Stage 9 PR reviewed and merged, then link it]. Stage 8 was integrated through PR #21 (`a8c7d01`), reviewed by Ngedup and Aagney: https://github.com/Blahuee/st1-assignment-3/pull/21
Protected common candidate and PG differences: Not applicable. UG-only group, so there is no PG extension to separate from the common candidate.
Feature freeze / owner / verifier: [TO DO group: freeze time after Stage 9 merge, owner and a verifier who did not write the Stage 9 code]


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: Do not release yet. Passing tests only show the tested behaviour works. Someone else could not reliably set the system up from the README, nobody has checked the dependency, and users would not be told about the limitation. All three are quick to fix, so the team should fix the README, review the dependency, document the limitation, recheck on the exact SHA and then release.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | FR-06, FR-07, AC-05.1 to AC-05.3, AC-06.1 (common). T-20 to T-24; F8-02 repair restored lookup of cancelled appointments | `project/tests/test_services.py` @ `c900456`; repair `bb07074`; issue #20 | [TO DO group: name] | Yes at service level | [TO DO after Stage 9: show it through the menu and confirm CANCELLED appears in default listing] |
| Architecture responsibilities are appropriate | Domain holds rules and guarded cancel; store holds three dictionaries; services coordinate; no input/output in domain, store or services (common) | `project/smartcare/` @ `c900456` | [TO DO group: name] | Partly | [TO DO after Stage 9: check queries stay pure and input/output stays in console] |
| Rescheduling is safe — PG only | Not applicable. UG-only group | N/A | N/A | N/A | None |
| AI use is responsible — common recheck / PG assurance | Common recheck: Copilot review of PR #15 in Stage 6 H and I; Copilot cause ranking for F8-01 and F8-02 in Stage 8. PG assurance not applicable | `stage06/` and `stage08/` records @ `c900456` | [TO DO group: name] | Partly | Stage 9 AI use and this Stage 12 draft must be recorded in Part E |
| System is maintainable | 37 tests, requirement-to-test matrix, small separated modules, Stage 8 status-enum refactor `8a906fa` | `stage07/` record; `project/` @ `c900456` | [TO DO group: name] | Partly | Fix stale docs and missing docstrings in Part H |
| FR-01–03 register/find and validation | T-01 to T-03, T-08 to T-10, T-15 to T-17, T-26 to T-31; AC-01.2, AC-02.1, AC-02.2 | `project/tests/` @ `c900456`, matrix in `stage07/` | [TO DO group: name] | Yes at service/domain level | [TO DO after Stage 9: console run] |
| FR-04–05 booking/conflict rules | T-04 to T-06, T-11, T-12, T-18, T-19, T-25; AC-03.1, AC-03.2, AC-04.1, AC-04.2; F8-01 repair `ed76dc8` | `project/tests/` @ `c900456`; issue #19 | [TO DO group: name] | Yes at service/domain level | [TO DO after Stage 9: console run] |
| FR-06–08 cancellation/history/find | T-07, T-13, T-14, T-20 to T-24; AC-05.1 to AC-05.3, AC-06.1 | `project/tests/` @ `c900456` | [TO DO group: name] | Yes at service/domain level | [TO DO after Stage 9: console run] |
| FR-09 and QRY/FP listing/filter/order/purity | [TO DO after Stage 9] Not implemented at `c900456` | `project/smartcare/queries.py`, `services.py` | [TO DO group: name] | No | **Release blocker** until Stage 9 is merged and tested |
| UI full console sequence and error recovery | [TO DO after Stage 9] `run_menu` not implemented at `c900456` | `project/smartcare/console.py` | [TO DO group: name] | No | **Release blocker** until Stage 9 is merged and run |
| Session-only scope / FR-10 retired | Store is three in-memory dictionaries; no file or database code; demo prints the session-only message; `project/README.md` says FR-10 is retired | `project/smartcare/data_store.py`, `project/README.md` @ `c900456` | [TO DO group: name] | Yes | Recheck on final SHA |
| PG RES and assurance integration | Not applicable. UG-only group | N/A | N/A | N/A | None |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [TO DO after Stage 9: Python and pytest versions] | `project/`, `python -m pytest -v` | [TO DO after Stage 9] | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Complete PG if applicable | Not applicable. UG-only group | N/A | N/A | N/A | N/A |
| Affected focused checks after correction | [TO DO after Stage 9] | `project/`, [TO DO after Stage 9: focused command] | [TO DO after Stage 9] | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Full integrated recheck | [TO DO after Stage 9] | `project/`, `python -m pytest -v` | [TO DO after Stage 9] | [TO DO after Stage 9] | [TO DO after Stage 9] |
Prior assertions preserved / reviewed test diff: The test files at `c900456` are identical to the Stage 7 tested commit `71ef3a4` (`git diff 71ef3a4 c900456 -- project/tests` is empty). [TO DO after Stage 9: repeat this diff against the final SHA and confirm Stage 9 only adds tests]
Remaining failure / limitation: Interim only, not the final result: 37 passed at `c900456` on 9 Nov 2026 (Python 3.13.18, pytest 9.1.1, run by Claude on a copy, and pytest differs from the pinned 8.3.5). None of the 37 tests call the Stage 9 functions. [TO DO after Stage 9: replace this line]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | SmartCare replaces manual appointment handling. Stakeholders: reception/admin staff, patients, practitioners | Explains who needs it and why | [TO DO group: presenter] | Requirements baseline Revision 2 |
| Register and find Patient and two Practitioners | P1 Alex Example; D1 and D2 Example practitioners | FR-01, FR-02, FR-03 | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Valid booking | A1, P1, D1, 2026-12-01 09:00 | FR-04, AC-03.1 | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Same practitioner exact-time conflict rejected | A2, P1, D1, 2026-12-01 09:00 | FR-05, AC-04.1 | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Different practitioner same time allowed | A3, P1, D2, 2026-12-01 09:00 | FR-05, AC-04.2 | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Cancel SCHEDULED and retain/find CANCELLED object | Cancel A1, then find A1 | FR-06, FR-07, FR-08, AC-05.1, AC-05.2 | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Invalid/repeated cancellation rejected | Cancel A1 again; cancel unknown A99 | FR-06, AC-05.3 | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Default all-status listing | List D1 with no status filter | FR-09: all statuses shown, including CANCELLED | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Explicit filtering / empty vs unknown / deterministic order | Filter D1 by SCHEDULED; list D2 with no matching status; list unknown D99 | FR-09: empty list for known practitioner, error for unknown, sorted by date/time then ID | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Invalid date/status/menu/lookup recovery and continued operation | `2026-13-40 09:00`; status `BAD`; menu choice `99`; patient `P99` | Clear error and menu keeps running | [TO DO after Stage 9] | [TO DO after Stage 9] |
| Session-only limitation and normal exit | Exit, restart, look for P1 | FR-10 retired: data lost on exit | [TO DO after Stage 9] | [TO DO after Stage 9] |
| One meaningful requirement-linked pytest test explained | `test_cancelled_appointment_remains_in_history` (T-21): book A1, cancel it, find it again | FR-07, AC-05.2: same object is still found, is CANCELLED and is still in the list | Failed in Stage 8 while F8-02 was present (`b99a90f`) and passed after repair (`bb07074`), so it really detects the bug | `project/tests/test_services.py` line 174 @ `c900456` |
| Architecture and one actual AI decision / known limitation | Appointment.cancel holds the rule; the service finds the record and calls it. AI decision: Stage 6 H Copilot review of PR #15, decision Modify. Limitation: exact-time conflicts only | Design and AI evidence can be explained | [TO DO group: presenter] | `stage06/` part H |
| PG reschedule identity/participants/time and no-op | Not applicable. UG-only group | N/A | N/A | N/A |
| PG conflict/invalid status/failure non-mutation | Not applicable. UG-only group | N/A | N/A | N/A |
| PG old slot / current lookup/list ordering / assurance risks | Not applicable. UG-only group | N/A | N/A | N/A |
Stable demo owner / fresh process / command: [TO DO group: owner]. From `project/`, in a fresh process: `python main.py --interactive`.
PG demonstrations through service/tests or not applicable: Not applicable. UG-only group.


## E Final code quality and AI review

Reviewed at `c900456`. [TO DO after Stage 9: re-review `queries.py`, the listing service and `run_menu`.]

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | `project/smartcare/domain.py`, `data_store.py`, `services.py` | No finding so far. Only `console.py` and `main.py` print. Pure query cannot be checked until Stage 9 | [TO DO after Stage 9: recheck `queries.py`] |
| PascalCase and snake_case naming | `project/smartcare/`, `project/tests/` | No finding | No change |
| Useful type hints and meaningful docstrings | `data_store.py`, `services.py`, `main.py`, `project/tests/` | Finding: `find_appointment` and `has_practitioner_conflict` have no docstrings. Stale text says the starter raises `NotImplementedError`, plus the typo "Return's". Student tests have no type hints | [TO DO group: fix docstrings; rerun full tests. Test hints can stay as an accepted minor gap] |
| Four-space indentation and imports/layout | `project/smartcare/`, `project/main.py` | No tabs or odd indentation found by scan | No change |
| Focused methods / duplication / dead or commented code | `data_store.py` | Finding: `find_appointment` loops through every appointment, while the other lookups use the dictionary directly. No commented-out code found | Behaviour is correct. Accept as minor debt (Part G) or change to a dictionary lookup and rerun tests |
| Globals / leakage / unnecessary inheritance or frameworks | `project/smartcare/` | No global variables, no inheritance beyond `Enum`, no frameworks. Identity and appointment state are read-only properties | No change |
| No SQLite/persistence/repository ABCs/speculative features | `project/smartcare/` | No finding. Imports are only `re`, `datetime`, `enum`, `argparse` and project modules | No change |
| Synthetic data / secrets / dependencies / provenance | `project/requirements-dev.txt`, tracked files | No secrets found by word scan. Example data is synthetic. Only dev dependency is `pytest==8.3.5`; runtime is standard library | Recheck on final SHA |
| Significant common Copilot contributions and human verification | `stage06/` parts H, I; `stage08/` Copilot sections | Copilot reviewed PR #15 and ranked causes for F8-01 and F8-02. Humans checked each against code and tests | [TO DO after Stage 9: add Stage 9 AI contributions] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | N/A | Not applicable. UG-only group | N/A |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| Copilot: PR #15 meets AC-05.1 to AC-05.3 | FR-06, FR-07; `cancel_appointment` | Ngedup compared it with the code at `5244ad3` and saw that no test at merge time called the method | Modify. Code supported the results, but Copilot had no test evidence | Stage 7 tests T-20 to T-23 later added direct evidence |
| Copilot: F8-01 is caused by `!=` instead of `==` in the conflict check; two other causes ranked lower | FR-05, AC-04.1; `has_practitioner_conflict` | Inspected code and reran the failing tests | Accept first cause, reject the other two, as the evidence did not support them | Repaired in `ed76dc8`; focused tests passed |
| Copilot: F8-02 is caused by a cancelled-status filter in `find_appointment`; two other causes ranked lower | FR-07, AC-05.2, AC-06.1; `find_appointment` | Inspected code and reran the failing tests | Accept first cause, reject the other two, as the evidence did not support them | Repaired in `bb07074`; focused tests passed |
| Claude: drafted parts of this Stage 12 record from the repo | Stage 12 record | [TO DO group: check each entry against the repo] | [TO DO group: Accept/Modify/Reject and reason] | [TO DO group] |
Access route or approved equivalent / limitations: GitHub Copilot is the nominated assistant. Claude was also used on 9 Nov 2026 to draft parts of this record. [TO DO group: confirm this use is allowed or ask the tutor, and add any Stage 9 tool use]
Available AI evidence and missing evidence honestly disclosed: Stage 6 H and I and the Stage 8 prompts are available. The Stage 6 Copilot review was done after merge, on 9 Nov 2026. Stage 6 PRs #8, #9 and #10 record no Copilot use. Earlier reviews were weak: PRs #8 and #9 have no recorded approval.


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | `README.md`, `project/README.md` | [TO DO group] | Gap: `project/README.md` is still titled "Stage 6 starter" and the root README says it is the Stage 6 starter |
| Out-of-scope capabilities and known limitations | `project/README.md` last paragraphs | [TO DO group] | Partly there. Session-only and FR-10 are covered. Add auth, portal, notifications, billing, clinical AI and timezone limits |
| Confirmed teaching Python version and dependency installation | `README.md`, `project/README.md`, `project/requirements-dev.txt` | [TO DO group] | Gap: README says Python 3.13, but Stage 6 and 7 runs used Python 3.14.3. Rerun on 3.13 or state the difference |
| Working directory / demo / interactive / test commands | `README.md`, `project/README.md` | [TO DO group] | Partly there. Add `python main.py --interactive` |
| Repository structure and architecture responsibilities | `project/README.md` | [TO DO group] | Partly there. Remove old TODO text and add `queries.py` and console responsibilities |
| Responsible AI summary / synthetic-data rule | `README.md` last paragraph | [TO DO group] | Partly there. Add a short responsible-AI summary with links |
| Release label/version and SHA links | `README.md` group index | [TO DO group] | Gap: every group index line still says `[complete]` |
Root README index and project/README verified: Not yet. [TO DO group: fix the gaps above, then verify]
Fresh clone or extracted ZIP / candidate identity: [TO DO after Stage 9]
Verifier and clean environment / actual version: [TO DO group: someone other than the Stage 9 author]
Setup/run/test commands and observed results: [TO DO after Stage 9]
Missing local file or setup gap / remedy and recheck: [TO DO after Stage 9]


## G Known limitations debt and release notes

## G Known limitations debt and release notes

Delivered features: Register and find patients and practitioners; book with exact-time practitioner conflict checks; find appointments; cancel while keeping history. [TO DO after Stage 9: add practitioner listing, filtering, ordering and the interactive menu]
Important fixes: F8-01 practitioner conflict check corrected (`ed76dc8`, issue #19). F8-02 cancelled appointments can be found again (`bb07074`, issue #20).
Architecture/quality improvements: Conflict check uses `AppointmentStatus.SCHEDULED` instead of a raw string (`8a906fa`). 29 student-written test functions were added in Stage 7, for 37 tests in total.
Known limitations: Data lasts for one session only. Conflicts are exact-time only because appointments have no duration. No patient-conflict, age or past-date rules. Console only.
AI-assisted development note: GitHub Copilot was used for review and ranking possible defect causes. People checked its output against code, requirements and tests, and the team stays responsible for the code. Claude helped draft parts of this record. [TO DO after Stage 9: add Stage 9 AI use]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| `find_appointment` loops through all appointments | Slower with many records; inconsistent with other lookups | Low | Use a dictionary lookup | [TO DO group: accept or fix] Correct at teaching scale |
| No test calls `parse_date_time` directly at `c900456` | Bad date input is not proven to be rejected | Medium | [TO DO after Stage 9: add tests with the menu work] | [TO DO group: fix if time allows] |
| Two store methods lack docstrings | Harder to maintain | Low | Add docstrings | [TO DO group: fix before release, it is quick] |
| Exact-time conflict only, no duration | Overlapping appointments would be allowed if durations existed | Medium | Add duration and overlap rules if required | Yes, in line with the baseline: no duration rules apply |
| No persistence | Data is lost on exit | Medium for real use | Add storage in a future production version | Yes, FR-10 is retired |
| Stage 6 PRs had weak or no formal review | Less confidence in those early merges | Low now | Require formal review before merge | Offset later by Stage 7 tests and the PR #21 review |
Session-only synthetic data and minute-precision local time: All data is synthetic and kept in memory for one session. Times are naive local datetimes at minute precision; the console accepts exactly `YYYY-MM-DD HH:MM`.
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: None of these are included. They are out of scope for this teaching release.
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: One user, one process, no concurrency handling, no timezone policy, no logging or monitoring, and a basic console with no accessibility testing.
Difference between accepted scope limit and unresolved required behaviour: A scope limit is something the requirements leave out, such as persistence. Unresolved required behaviour is something the requirements ask for that does not work. At `c900456`, FR-09 and the interactive menu are unresolved required behaviour, not scope limits, so they must be finished.
PG assurance residual risks / owner / status or not applicable: Not applicable. UG-only group.

## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| FR-09, QRY/FP, console menu | `python main.py --interactive` prints "Stage 9 interactive menu is not yet completed" at `c900456`; four functions raise `NotImplementedError` | High, release blocker | Ngedup, finish Stage 9 | [TO DO after Stage 9] | [TO DO after Stage 9] | [TO DO after Stage 9] |
| README accurate and reproducible | Group index has `[complete]` placeholders; `project/README.md` still describes the Stage 6 starter | High for submission | [TO DO group: owner] update both | [TO DO group] | [TO DO group: fresh-clone check] | None expected |
| Python version evidence | README says 3.13; Stage 6 and 7 runs used 3.14.3 | Medium | [TO DO group: owner] rerun on 3.13 or disclose | [TO DO group] | [TO DO group] | [TO DO group] |
| Docstrings accurate and present | Stale `NotImplementedError` text and "Return's" in `services.py`; two store methods have none; `main.py` still says the menu is incomplete | Low | [TO DO group: owner] fix | [TO DO group] | [TO DO group: full tests] | None expected |
Justified no-change conclusion if no defect found: Not applicable. Defects were found.
Release blockers still open / status: Open at `c900456`: Stage 9 code, tests and record; README gaps. [TO DO after Stage 9: update status]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [TO DO after Stage 9: Stage 9 and Stage 12 PRs]. Earlier: issues #1, #3, #19, #20; PRs #8, #9, #10, #15, #21.
Independent reviewer / feedback / response: [TO DO after Stage 9]
Integration commit / full recheck: [TO DO after Stage 9]
Tracked and untracked file inspection / cleanliness: At `c900456` tracked files include no caches, environments or Stage 8 utility files. [TO DO after Stage 9: repeat with `git status` and `git ls-files`]
Secrets/staff material/caches/tool-metadata exclusion check: Word scan of Python files found no secrets at `c900456`, and `.gitignore` covers environments, caches, `.env` and Stage 8 folders. [TO DO group: repeat on final SHA and confirm no staff material]
Candidate recovery plan / known-good SHA: Known-good pre-Stage 9 commit: `c900456` (37 tests pass). To recover, make a branch from the known-good SHA or use `git revert`; do not rewrite shared history. [TO DO after Stage 9: replace with candidate SHA]
Named substantive contributions: Alicia: lookup and cancellation services, Stage 8 repairs and refactor. Aagney: Stage 7 matrix and tests, review and merge of PR #21. Ngedup: Stage 6 records, Copilot review of PR #15, review of PR #21, Stage 9 work. [TO DO group: each member checks and updates their own]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? A specific tested version, identified by an exact commit, that could become the release if it passes the final checks.

2. What is feature freeze and why is it used? A point where no new features are added and only fixes and checks are allowed. It keeps the code stable so testing results stay true.

3. What is regression testing in a release context? Rerunning all the existing tests on the release candidate to prove that recent changes did not break things that used to work.

4. What is a known limitation? Something the system does not do or does not handle, which the team knows about and states openly. For SmartCare, data is lost on exit.

5. What is technical debt? Shortcuts or weak spots left in the system that work now but make future changes harder or riskier unless they are fixed later.

6. What are release notes? A short summary for readers of what is in a release: features, fixes, known limitations and anything else they should know.

7. What is software maintenance? Work done after release to keep software useful: fixing bugs, adapting to changes, improving the code and adding what is needed.

8. What is the purpose of the individual demonstration/viva? To check that each person understands the system and their own contribution, and can explain and change it without relying on AI or teammates.

9. What should the final responsible-AI check establish before release? That significant AI output was reviewed and tested by people, its use is honestly recorded, only synthetic data was shared, no secrets or unreviewed dependencies came in, and people accept responsibility for the result.

10. What is the main course conclusion about AI and the role of the software engineer? AI can speed up the work, but engineers still decide what to build, check whether it is correct and stay accountable for it.


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | Staff need to book and cancel appointments without double-booking practitioners and without losing history. Stakeholders are staff, patients and practitioners. |
| Two requirements and acceptance criteria | FR-05: a practitioner cannot have two SCHEDULED appointments at the same time (AC-04.1), but a different practitioner can (AC-04.2). FR-07: a cancelled appointment stays retrievable (AC-05.2). See `stage07/` matrix. |
| Domain model and architecture | Patient, Practitioner, Appointment and AppointmentStatus are in `domain.py`. `SmartCareDataStore` holds records, services coordinate work and the console handles input and output. |
| Design trade-off | In-memory dictionaries keep the design simple and fit the session-only scope, but data is lost on exit. |
| Meaningful test and its limits / 100 percent coverage | T-21 proves cancelled appointments are retained. It does not prove the console works. 100 percent coverage only shows lines ran, not that the assertions or requirements are right. |
| Diagnosed defect and verification | F8-02: `find_appointment` skipped cancelled records. Tests T-21 and T-22 failed with `LookupError`; the filter was removed in `bb07074` and the focused tests then passed. |
| Shared store and session-state/query responsibilities | All three services share one store, so they see the same records in a session. [TO DO after Stage 9: add the query part] |
| What would break if session-state lookup/query responsibilities changed? | If each service had its own store, booking could not see registered patients. If lookup hid cancelled records, FR-07 would break, which is what F8-02 did. [TO DO after Stage 9: add the listing effect] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | Cancel only needs the appointment's own status, so the rule sits on Appointment. A conflict needs other appointments, so the service asks the store, which can see them all. |
| FR-07 retained history test | `test_cancelled_appointment_remains_in_history`, `project/tests/test_services.py` line 174 @ `c900456`. |
| Actual AI change rejected/modified or honestly accepted with verification | Stage 6 H: Copilot's review of PR #15 was modified, because it could not provide test evidence. |
| Unresolved limitation / future production work | No persistence, no login or roles, and exact-time conflicts only. |
| Personal implementation contribution | [TO DO group: each member, with link] |
| Personal test/review/design/integration contribution | [TO DO group: each member, with link] |
| PG agentic change and rescheduling verification | Not applicable. UG-only group. |
| PG responsible-AI risk/remediation or supported no finding | Not applicable. UG-only group. |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
