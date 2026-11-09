# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Tue 1:30 - 3:30 Group 1
Members and UG/PG applicability: UG - Alicia Hurst - Blahuee, UG - Aagney Mani Sharma - Aagneyf1r3, UG - Ngedup Jigme Lhazeen - njlhazin. All UG, so this release is common scope only. Stages 10 and 11 stay unchanged as intentionally not applicable.


## A Release scope and starting SHA

Release label/version and requirements baseline: SmartCare A3 common release v1.0-common, requirements baseline Revision 2.
Common starting SHA / branch / applicable members: `351b6ca` / main / all three UG members.
PG starting SHA / branch / applicable members or not applicable: Not applicable. UG-only group.
Working-state review and approved integration: Stage 9 code was integrated through PR #29 (`fecb697`), PR #30 (`8f7cec2`) and PR #31 (`351b6ca`), all authored by Alicia. PRs #29 and #30 were merged by Aagney and PR #31 by Ngedup. The Stage 9 record was merged in PR #32 (`7fc8a94`).
Protected common candidate and PG differences: Not applicable. UG-only group, so there is no PG extension to separate from the common candidate.
Feature freeze / owner / verifier: No formal freeze was declared. Code has not changed since `351b6ca`, merged 9 Nov 2026. Regression verifier: Aagney, who did not author the Stage 9 code.


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: Do not release yet. Passing tests only show the tested behaviour works. Someone else could not reliably set the system up from the README, nobody has checked the dependency, and users would not be told about the limitation. All three are quick to fix, so the team should fix the README, review the dependency, document the limitation, recheck on the exact SHA and then release.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | FR-06, FR-07, AC-05.1 to AC-05.3, AC-06.1 (common). T-20 to T-24, workflow test, menu demo | `project/tests/test_services.py`, `test_workflows.py` @ `351b6ca`; repair `bb07074`; issue #20 | Aagney (ran regression) | Yes | None |
| Architecture responsibilities are appropriate | Domain holds rules; store holds records; services coordinate; queries are pure; only console and main print (common) | `project/smartcare/` @ `351b6ca` | Aagney | Yes | Minor documentation items in Part H |
| Rescheduling is safe — PG only | Not applicable. UG-only group | N/A | N/A | N/A | None |
| AI use is responsible — common recheck / PG assurance | Common recheck: Copilot evidence in Stages 6, 8 and 9; Claude use disclosed in Part E. PG assurance not applicable | `stage06/`, `stage08/`, `stage09/`, Part E @ `7fc8a94` | Aagney | Partly | Tutor approval for Claude was not asked |
| System is maintainable | 50 tests, requirement-to-test matrix, small separated modules, refactor `8a906fa` | `stage07/`; `project/` @ `351b6ca` | Aagney | Partly | Stale docstrings and README gaps remain (Part H) |
| FR-01–03 register/find and validation | T-01 to T-03, T-08 to T-10, T-15 to T-17, T-26 to T-31, menu demo; AC-01.2, AC-02.1, AC-02.2 | `project/tests/` @ `351b6ca` | Aagney (ran regression) | Yes | None |
| FR-04–05 booking/conflict rules | T-04 to T-06, T-11, T-12, T-18, T-19, T-25, workflow test, menu demo; AC-03.1, AC-03.2, AC-04.1, AC-04.2 | `project/tests/` @ `351b6ca`; issue #19 | Aagney (ran regression) | Yes | None |
| FR-06–08 cancellation/history/find | T-07, T-13, T-14, T-20 to T-24, workflow test, menu demo; AC-05.1 to AC-05.3, AC-06.1 | `project/tests/` @ `351b6ca` | Aagney (ran regression) | Yes | None |
| FR-09 and QRY/FP listing/filter/order/purity | `tests/test_queries.py` (7 tests), 5 service listing tests, workflow test, menu demo; QRY-01 to QRY-04, FP-01 to FP-03 | `project/smartcare/queries.py`, `services.py`, PRs #29 and #30 @ `351b6ca` | Aagney (ran regression) | Mostly | Tie-break test does not prove ID ordering; empty and already-sorted inputs not tested (Part H) |
| UI full console sequence and error recovery | `run_menu` scripted demo in Part D; UI-01, UI-02 | `project/smartcare/console.py`, PR #31 @ `351b6ca` | Aagney | Mostly | Demo run by Claude on a copy. No pytest test calls `run_menu` |
| Session-only scope / FR-10 retired | In-memory store only; a fresh process could not find P1 | `project/smartcare/data_store.py`, `project/README.md` @ `351b6ca` | Aagney | Yes | None |
| PG RES and assurance integration | Not applicable. UG-only group | N/A | N/A | N/A | None |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | Windows, Python 3.14.3, pytest 8.3.5 | `project/`, `python -m pytest -v` | `351b6ca` | 50 passed, 0 failed | Run by Aagney, 9 Nov 2026 |
| Complete PG if applicable | Not applicable. UG-only group | N/A | N/A | N/A | N/A |
| Affected focused checks after correction | Windows, Python 3.14.3, pytest 8.3.5 | `project/`, `python -m pytest -vv -s` on `feature/stage9-queries` | `5f7e2c0` | 44 passed, 0 failed | Run by Aagney before PR #29 merge |
| Full integrated recheck | Linux, Python 3.13.18, pytest 9.1.1 | `project/`, `python -m pytest -q` | `351b6ca` | 50 passed, 0 failed | Run by Claude on an extracted copy, 9 Nov 2026 |
Prior assertions preserved / reviewed test diff: `git diff --stat 71ef3a4 351b6ca -- project/tests` shows 433 insertions and 3 deletions. The 3 deleted lines are in `test_services.py` from PR #30: test data changed from "Dr Smith" to "Dr. Smith" and "General Practice" to "Specialty", with one name assertion updated to match. No behaviour check was weakened.
Remaining failure / limitation: No test failures at `351b6ca`. The team's own run used Python 3.14.3 rather than the README's 3.13. The Python 3.13 run used pytest 9.1.1 rather than the pinned 8.3.5.


## D Console and end to end demonstration

Observed results below come from one scripted run of `python main.py --interactive` at `351b6ca`, by Claude on an extracted copy (Linux, Python 3.13.18), 9 Nov 2026.

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | SmartCare replaces manual appointment handling. Stakeholders: reception/admin staff, patients, practitioners | Explains who needs it and why | Presenter: Aagney | Requirements baseline Revision 2 |
| Register and find Patient and two Practitioners | P1 Alex Example; D1 Taylor Example; D2 Jordan Example | FR-01, FR-02, FR-03 | All registered and found with correct details | Scripted run @ `351b6ca` |
| Valid booking | A1, P1, D1, 2026-12-01 09:00 | FR-04, AC-03.1 | `Booked A1: P1 with D1, 2026-12-01 09:00, scheduled` | Scripted run @ `351b6ca` |
| Same practitioner exact-time conflict rejected | A2, P1, D1, 2026-12-01 09:00 | FR-05, AC-04.1 | `Error: Practitioner already has a SCHEDULED appointment at this time` | Scripted run @ `351b6ca` |
| Different practitioner same time allowed | A3, P1, D2, 2026-12-01 09:00 | FR-05, AC-04.2 | `Booked A3: P1 with D2, 2026-12-01 09:00, scheduled` | Scripted run @ `351b6ca` |
| Cancel SCHEDULED and retain/find CANCELLED object | Cancel A1, then find A1 | FR-06, FR-07, FR-08, AC-05.1, AC-05.2 | A1 cancelled, then found with status cancelled | Scripted run @ `351b6ca` |
| Invalid/repeated cancellation rejected | Cancel A1 again; cancel unknown A99 | FR-06, AC-05.3 | `Error: Only SCHEDULED appointments may be cancelled`; `Error: Appointment not found` | Scripted run @ `351b6ca` |
| Default all-status listing | List D1 with blank status | FR-09: all statuses shown, including CANCELLED | A1 listed as cancelled | Scripted run @ `351b6ca` |
| Explicit filtering / empty vs unknown / deterministic order | Filter D1 by scheduled before rebooking; book A4 at the freed 09:00 and A5 at 08:00; list D1; list D2 by cancelled; list unknown D99 | FR-09: empty for known practitioner, error for unknown, sorted by date/time then ID | Filter showed `No matching appointments.`; A4 booked in freed slot; order was A5, A1, A4; D2 showed `No matching appointments.`; D99 gave `Error: Practitioner not found` | Scripted run @ `351b6ca` |
| Invalid date/status/menu/lookup recovery and continued operation | `2026-13-40 09:00`; `tomorrow`; status `BAD`; menu `99`; patient `P99`; blank patient ID; duplicate P1 | Clear error and menu keeps running | Each gave a clear error or unknown-choice message. A1 was still found unchanged afterwards | Scripted run @ `351b6ca` |
| Session-only limitation and normal exit | Exit with 0, start a new process, find P1 | FR-10 retired: data lost on exit | `Goodbye. Session data is discarded.`; new process gave `Error: Patient not found` | Scripted run @ `351b6ca` |
| One meaningful requirement-linked pytest test explained | `test_cancelled_appointment_remains_in_history` (T-21): book A1, cancel it, find it again | FR-07, AC-05.2: same object is still found, is CANCELLED and is still in the list | Failed in Stage 8 while F8-02 was present (`b99a90f`) and passed after repair (`bb07074`), so it really detects the bug | `project/tests/test_services.py` @ `351b6ca` |
| Architecture and one actual AI decision / known limitation | Appointment.cancel holds the rule; the service finds the record and calls it. AI decision: Stage 6 H Copilot review of PR #15, decision Modify. Limitation: exact-time conflicts only | Design and AI evidence can be explained | Presenter: Aagney | `stage06/` part H |
| PG reschedule identity/participants/time and no-op | Not applicable. UG-only group | N/A | N/A | N/A |
| PG conflict/invalid status/failure non-mutation | Not applicable. UG-only group | N/A | N/A | N/A |
| PG old slot / current lookup/list ordering / assurance risks | Not applicable. UG-only group | N/A | N/A | N/A |
Stable demo owner / fresh process / command: Demo owner Aagney. From `project/`, in a fresh process: `python main.py --interactive`.
PG demonstrations through service/tests or not applicable: Not applicable. UG-only group.


## E Final code quality and AI review

Reviewed at `351b6ca`.

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | `project/smartcare/` | No finding. `select_appointments` reads only its arguments, uses `sorted` and does no input/output. Services return objects or raise errors. Only `console.py` and `main.py` print | No change |
| PascalCase and snake_case naming | `project/smartcare/`, `project/tests/` | No finding | No change |
| Useful type hints and meaningful docstrings | `console.py`, `data_store.py`, `services.py`, `main.py` | Finding: 8 console command helpers, `find_appointment` and `has_practitioner_conflict` have no docstrings. Stale docstrings remain in `services.py`, `run_menu` and `main.py`, plus the typo "Return's". Tests have no type hints | Not corrected at `351b6ca`. Accepted as low-priority debt (Part G) |
| Four-space indentation and imports/layout | `project/smartcare/`, `project/main.py` | No tabs or odd indentation found. One trailing-whitespace line in `console.py` line 70 | Accepted as minor |
| Focused methods / duplication / dead or commented code | `data_store.py`, `main.py` | Finding: `find_appointment` loops through every appointment, and the `NotImplementedError` handler in `main.py` is now unused. No commented-out code found | Behaviour is correct. Accepted as minor debt (Part G) |
| Globals / leakage / unnecessary inheritance or frameworks | `project/smartcare/` | No global state. No inheritance beyond `Enum`, no frameworks. `MENU_TEXT` is a constant | No change |
| No SQLite/persistence/repository ABCs/speculative features | `project/smartcare/` | No finding | No change |
| Synthetic data / secrets / dependencies / provenance | `project/requirements-dev.txt`, tracked files | No secrets found by word scan. Example data is synthetic. Only dev dependency is `pytest==8.3.5`; runtime is standard library | No change |
| Significant common Copilot contributions and human verification | `stage06/` parts H, I; `stage08/` Copilot sections; `stage09/` part E | Copilot reviewed PR #15, ranked causes for F8-01 and F8-02, and was used for Stage 9 as recorded in `stage09/` part E. Humans checked the Stage 6 and 8 findings against code and tests | No change |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | N/A | Not applicable. UG-only group | N/A |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| Copilot: PR #15 meets AC-05.1 to AC-05.3 | FR-06, FR-07; `cancel_appointment` | Ngedup compared it with the code at `5244ad3` and saw that no test at merge time called the method | Modify. Code supported the results, but Copilot had no test evidence | Stage 7 tests T-20 to T-23 later added direct evidence |
| Copilot: F8-01 is caused by `!=` instead of `==` in the conflict check; two other causes ranked lower | FR-05, AC-04.1; `has_practitioner_conflict` | Inspected code and reran the failing tests | Accept first cause, reject the other two, as the evidence did not support them | Repaired in `ed76dc8`; focused tests passed |
| Copilot: F8-02 is caused by a cancelled-status filter in `find_appointment`; two other causes ranked lower | FR-07, AC-05.2, AC-06.1; `find_appointment` | Inspected code and reran the failing tests | Accept first cause, reject the other two, as the evidence did not support them | Repaired in `bb07074`; focused tests passed |
| Claude: PR #29 tie-break test does not prove ID ordering, because A1 is already before A4 in the source list | QRY-03; `tests/test_queries.py` | No formal review of this finding is recorded on GitHub | Accept. Recorded as a non-blocking follow-up | Not fixed at `351b6ca`; recorded in Parts G and H |
| Claude: drafted parts of this Stage 12 record from the repo and ran the Part D script | Stage 12 record | Aagney checked the entries against the repo and Git output | Modify. Entries were kept where supported by repo evidence; unconfirmed reviews and approvals were removed | PR review claims changed to match GitHub; unknown items marked not recorded |
Access route or approved equivalent / limitations: GitHub Copilot is the nominated assistant and was used for Stage 9. Claude was also used on 9 Nov 2026 to check PRs #29 and #30, draft parts of this record and run the Part D script. Tutor approval for Claude was not asked.
Available AI evidence and missing evidence honestly disclosed: Stage 6 H and I, the Stage 8 prompts and Stage 9 part E are available. The Stage 6 Copilot review was done after merge, on 9 Nov 2026. Stage 6 PRs #8, #9 and #10 record no Copilot use. Earlier reviews were weak: PRs #8 and #9 have no recorded approval.


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | `README.md`, `project/README.md` | Claude review, Aagney | Gap: `project/README.md` is still titled "Stage 6 starter" |
| Out-of-scope capabilities and known limitations | `project/README.md` | Claude review, Aagney | Partly there. Session-only and FR-10 covered. Auth, portal, notifications, billing, clinical AI and timezone limits are recorded in Part G only |
| Confirmed teaching Python version and dependency installation | `README.md`, `project/README.md`, `project/requirements-dev.txt` | Aagney | README says Python 3.13. Team run used 3.14.3; 50 tests also passed on 3.13.18 with pytest 9.1.1 |
| Working directory / demo / interactive / test commands | `README.md`, `project/README.md` | Claude review, Aagney | Partly there. `python main.py --interactive` is missing from both READMEs |
| Repository structure and architecture responsibilities | `project/README.md` | Claude review, Aagney | Partly there. Old TODO text remains; console and query responsibilities are not described |
| Responsible AI summary / synthetic-data rule | `README.md` last paragraph | Claude review, Aagney | Partly there. Synthetic-data rule present; AI summary is in Part G only |
| Release label/version and SHA links | `README.md` group index | Claude review, Aagney | Gap: group index still has `[complete]` placeholders |
Root README index and project/README verified: Not fully. The gaps above are open at `351b6ca`.
Fresh clone or extracted ZIP / candidate identity: Extracted copy of `351b6ca` made with `git archive` by Claude. No human fresh-clone check was completed.
Verifier and clean environment / actual version: Claude, Linux, Python 3.13.18, pytest 9.1.1. Not an independent human verifier.
Setup/run/test commands and observed results: From `project/`: `python main.py` printed the A1 booking and session-only message. `python -m pytest -q`: 50 passed.
Missing local file or setup gap / remedy and recheck: No missing files found. Remedy still needed: update the READMEs and repeat a human fresh-clone check.


## G Known limitations debt and release notes

Delivered features: Register and find patients and practitioners; book with exact-time practitioner conflict checks; find appointments; cancel while keeping history; list a practitioner's appointments with optional status filter and deterministic order; interactive console menu with error recovery.
Important fixes: F8-01 practitioner conflict check corrected (`ed76dc8`, issue #19). F8-02 cancelled appointments can be found again (`bb07074`, issue #20).
Architecture/quality improvements: Conflict check uses `AppointmentStatus.SCHEDULED` instead of a raw string (`8a906fa`). Pure queries are separated from services and console. Tests grew from 8 supplied to 50.
Known limitations: Data lasts for one session only. Conflicts are exact-time only because appointments have no duration. No patient-conflict, age or past-date rules. Console only.
AI-assisted development note: GitHub Copilot was used for review, ranking possible defect causes and Stage 9 work. Claude helped check PRs #29 and #30, drafted parts of this record and ran the demo script. People remain responsible for the code and its verification.

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| `find_appointment` loops through all appointments | Slower with many records; inconsistent with other lookups | Low | Use a dictionary lookup | Yes. Correct at teaching scale |
| Query tie-break test does not prove ID ordering; empty and already-sorted inputs untested | A broken tie-break could go unnoticed | Medium | Add a reversed-source test and the two missing cases | Yes for this release. The menu demo and code inspection support the behaviour |
| No test calls `parse_date_time`, `parse_status` or `run_menu` directly | Console errors are not protected by automated tests | Medium | Add console tests | Yes for this release. Covered by the scripted demo only |
| Missing and stale docstrings; unused handler in `main.py` | Harder to maintain | Low | Add or correct docstrings and remove the handler | Yes for this release |
| Exact-time conflict only, no duration | Overlapping appointments would be allowed if durations existed | Medium | Add duration and overlap rules if required | Yes, in line with the baseline: no duration rules apply |
| No persistence | Data is lost on exit | Medium for real use | Add storage in a future production version | Yes, FR-10 is retired |
| Stage 6 PRs had weak or no formal review | Less confidence in those early merges | Low now | Require formal review before merge | Offset later by Stage 7 tests and PR #21 review |
Session-only synthetic data and minute-precision local time: All data is synthetic and kept in memory for one session. Times are naive local datetimes at minute precision; the console accepts exactly `YYYY-MM-DD HH:MM`.
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: None of these are included. They are out of scope for this teaching release.
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: One user, one process, no concurrency handling, no timezone policy, no logging or monitoring, and a basic console with no accessibility testing.
Difference between accepted scope limit and unresolved required behaviour: A scope limit is something the requirements leave out, such as persistence. Unresolved required behaviour is something the requirements ask for that does not work. No unresolved required behaviour was found at `351b6ca`. The README gaps are submission gaps, not behaviour defects.
PG assurance residual risks / owner / status or not applicable: Not applicable. UG-only group.


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| FR-09, QRY/FP, console menu | At `c900456` the menu and listing raised `NotImplementedError` | High, was a release blocker | Alicia implemented; resolved | PRs #29, #30, #31, ending at `351b6ca` | 50 passed at `351b6ca`; scripted menu demo passed | Tie-break test gap; no direct console tests |
| README accurate and reproducible | Group index has `[complete]` placeholders; `project/README.md` still describes the Stage 6 starter | High for submission | Open, no owner assigned | Not done at `351b6ca` | Not done | Open |
| Python version evidence | README says 3.13; team run used 3.14.3 | Medium | Aagney and Claude runs recorded | No code change needed | 50 passed on 3.14.3 and on 3.13.18 | Pinned pytest 8.3.5 was not used on 3.13 |
| Docstrings accurate and present | Missing docstrings and stale text in `console.py`, `data_store.py`, `services.py`, `main.py` | Low | Accepted as debt | None | Not applicable | Open as debt |
Justified no-change conclusion if no defect found: Not applicable. Defects were found.
Release blockers still open / status: No behaviour blocker is open. The Stage 9 record was merged in PR #32 (`7fc8a94`). README corrections and an independent fresh-clone check are still open.


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: PR #29 https://github.com/Blahuee/st1-assignment-3/pull/29 (`5f7e2c0`); PR #30 https://github.com/Blahuee/st1-assignment-3/pull/30 (`e64579b`); PR #31 https://github.com/Blahuee/st1-assignment-3/pull/31 (`c3bace9`); PR #32 https://github.com/Blahuee/st1-assignment-3/pull/32. Earlier: issues #1, #3, #19, #20; PRs #8, #9, #10, #15, #21.
Independent reviewer / feedback / response: Alicia authored the three Stage 9 code PRs. PRs #29 and #30 were merged by Aagney with no formal approval recorded on GitHub. PR #31 shows as Approved on GitHub and was merged by Ngedup. Findings from the informal checks of #29 and #30 (tie-break test gap and changed older test data) are recorded in Parts C, G and H.
Integration commit / full recheck: `351b6ca`; 50 passed on Aagney's computer. Stage 9 record merged in PR #32 (`7fc8a94`) with no project code changes.
Tracked and untracked file inspection / cleanliness: `git status` at `351b6ca` was clean. Tracked files include no caches, environments or Stage 8 utility files.
Secrets/staff material/caches/tool-metadata exclusion check: Word scan found no secrets at `351b6ca`, and `.gitignore` covers environments, caches, `.env` and Stage 8 folders. No staff material was found in tracked file names.
Candidate recovery plan / known-good SHA: Known-good code commit: `351b6ca` (50 tests pass). To recover, make a branch from that SHA or use `git revert`; do not rewrite shared history.
Named substantive contributions: Alicia: lookup and cancellation services, Stage 8 repairs and refactor, Stage 9 queries, listing, menu and tests. Aagney: Stage 7 matrix and tests, review of PR #21, merges of PRs #21, #29 and #30, Stage 12 regression run and record. Ngedup: Stage 6 records, Copilot review of PR #15, review of PR #21, Stage 9 Parts A, B and G, merges of PRs #31 and #32.


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: NOT YET READY as a complete package. The code at `351b6ca` meets the tested common requirements, but README corrections and an independent fresh-clone check are incomplete, and PRs #29 and #30 have no formal approval recorded.
Approver / date / rationale and evidence: Aagney Mani Sharma, 9 Nov 2026, recording the release state alone before the deadline; not a full group decision. Evidence: Parts C, D and H.
What risks remain / conditions / owners: README gaps (no owner assigned); no human fresh-clone check; no ZIP uploaded; tie-break and console test gaps (accepted debt).
Can the team explain the system: Not confirmed as a group at submission.
Can a change be recovered: Yes. `351b6ca` is a known-good commit, and changes can be undone with `git revert`.
Common decision / PG decision where different: Common decision as above. PG not applicable.


## K Final tested release SHA

Exact common tested SHA: 351b6ca334415e52054d8a29ef9dab4bed175a2a
Exact PG tested SHA or not applicable: Not applicable. UG-only group.
Latest commit on main; it changes records only, and the code was tested at 351b6ca
Evidence-only later commit and difference explanation: PR #32 (`7fc8a94`) and the Stage 12 record merge changed records only. `git diff --stat 351b6ca 7fc8a94 -- project` shows no changes.
Executable changes after testing and re-verification: None.
Source ZIP name / SHA correspondence / extracted comparison: The repository link was submitted. No ZIP was uploaded. A local `smartcare-submission.zip` was made with `git archive` at `351b6ca`, before the records were merged.


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [x] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [x] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [x] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [x] project/ source and all accumulated applicable tests included.
- [x] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [x] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: Repository link submitted. No ZIP uploaded.
Deadline/timezone: Not recorded here. Australia/Sydney time.
Repository access arrangement: Public repository: https://github.com/Blahuee/st1-assignment-3
Mixed-candidate upload arrangement: Not applicable. All members are UG.
Oral/video recording/accessibility arrangements: Not confirmed at submission.
Remaining administration or release dependency: No source ZIP uploaded. Human fresh-clone check and README corrections not done.


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

Strongest evidence SmartCare is ready: Not recorded at submission.
Weakest area: Not recorded at submission.
How AI use changed from Stage 1 to Stage 12: Not recorded at submission.
Start doing — engineering and AI use: Not recorded at submission.
Stop doing — engineering and AI use: Not recorded at submission.
Continue doing — engineering and AI use: Not recorded at submission.
What worked / caused rework / future delivery improvement: Not recorded at submission.
One paragraph — If AI can write code why do we still need software engineers: Not recorded at submission.

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | Staff need to book and cancel appointments without double-booking practitioners and without losing history. Stakeholders are staff, patients and practitioners. |
| Two requirements and acceptance criteria | FR-05: a practitioner cannot have two SCHEDULED appointments at the same time (AC-04.1), but a different practitioner can (AC-04.2). FR-07: a cancelled appointment stays retrievable (AC-05.2). See `stage07/` matrix. |
| Domain model and architecture | Patient, Practitioner, Appointment and AppointmentStatus are in `domain.py`. `SmartCareDataStore` holds records, services coordinate work, queries select and sort, and the console handles input and output. |
| Design trade-off | In-memory dictionaries keep the design simple and fit the session-only scope, but data is lost on exit. |
| Meaningful test and its limits / 100 percent coverage | T-21 proves cancelled appointments are retained. It does not prove the console works. 100 percent coverage only shows lines ran, not that the assertions or requirements are right. |
| Diagnosed defect and verification | F8-02: `find_appointment` skipped cancelled records. Tests T-21 and T-22 failed with `LookupError`; the filter was removed in `bb07074` and the focused tests then passed. |
| Shared store and session-state/query responsibilities | All three services share one store, so they see the same records in a session. The service gets a fresh list from the store and passes it to the pure `select_appointments`, which depends only on its arguments. |
| What would break if session-state lookup/query responsibilities changed? | If each service had its own store, booking could not see registered patients. If lookup hid cancelled records, FR-07 would break, which is what F8-02 did. If the query sorted its source in place, it would change the caller's list. |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | Cancel only needs the appointment's own status, so the rule sits on Appointment. A conflict needs other appointments, so the service asks the store, which can see them all. |
| FR-07 retained history test | `test_cancelled_appointment_remains_in_history`, `project/tests/test_services.py` @ `351b6ca`. |
| Actual AI change rejected/modified or honestly accepted with verification | Stage 6 H: Copilot's review of PR #15 was modified, because it could not provide