# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: Tue 1:30 - 3:30 Group 1
Members and UG/PG applicability: UG - Alicia Hurst - Blahuee, UG - Aagney Mani Sharma - Aagneyf1r3, UG - Ngedup Jigme Lhazeen - njlhazin. All UG, so this release is common scope only. Stages 10 and 11 stay unchanged as intentionally not applicable.


## A Release scope and starting SHA

Release label/version and requirements baseline: SmartCare A3 common release v1.0-common, requirements baseline Revision 2.
Common starting SHA / branch / applicable members: `351b6ca` / main / all three UG members. This was the original Stage 9 candidate (50 passed). At the 9 Nov 2026 11:59 pm deadline, main was at `161c84a`. The release candidate code is `4713c07` (10 Nov 2026), which adds the post-deadline corrections listed in H.
PG starting SHA / branch / applicable members or not applicable: Not applicable. UG-only group.
Working-state review and approved integration: Stage 9 code was integrated through PR #29 (`fecb697`), PR #30 (`8f7cec2`) and PR #31 (`351b6ca`), all authored by Alicia. PRs #29 and #30 were merged by Aagney and PR #31 by Ngedup. The Stage 9 record was merged in PR #32 (`7fc8a94`). The 10 Nov 2026 corrections were committed to main by Aagney without a PR review: `dc1c9e9` (Stage 8 regression tests), `149f3f9` (three query tests, saved console runs, project README) and `4713c07` (behaviour-preserving release tidy-up).
Protected common candidate and PG differences: Not applicable. UG-only group, so there is no PG extension to separate from the common candidate.
Feature freeze / owner / verifier: Features were frozen at `351b6ca` (9 Nov 2026). After that only tests, documentation and a behaviour-preserving tidy-up were added; no feature or production behaviour changed. This is shown by the full suite (55 passed) and by the saved UI-01 and UI-02 console scripts giving identical output before and after `4713c07`. Owner: Aagney. Independent verifier: Ngedup (fresh clone, Part F).


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: Do not release yet. Passing tests only show the tested behaviour works. Someone else could not reliably set the system up from the README, nobody has checked the dependency, and users would not be told about the limitation. All three are quick to fix, so the team should fix the README, review the dependency, document the limitation, recheck on the exact SHA and then release.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | FR-06, FR-07, AC-05.1 to AC-05.3, AC-06.1 (common). T-20 to T-24, `test_f8_02_cancelled_appointment_is_still_found`, workflow test, saved UI-01 run | `project/tests/test_services.py`, `test_regressions.py`, `test_workflows.py`, `stage09/evidence/ui01_output.txt` @ `4713c07`; repair `bb07074`; issue #20 | Aagney (ran regression); Ngedup (fresh clone) | Yes | None |
| Architecture responsibilities are appropriate | Domain holds rules; store holds records; services coordinate; queries are pure; only console and main print (common) | `project/smartcare/` @ `4713c07` | Aagney | Yes | None; stale docstrings corrected in `4713c07` |
| Rescheduling is safe — PG only | Not applicable. UG-only group | N/A | N/A | N/A | None |
| AI use is responsible — common recheck / PG assurance | Copilot decisions in Stages 6, 7, 8 and 9; Claude use on 10–11 Nov 2026 disclosed in Part E. PG assurance not applicable | `stage06/` H–I, `stage07/` H–I, `stage08/` F, `stage09/` E, Part E | Aagney | Partly | Tutor approval for the AI routes was not asked; the Stage 9 Copilot transcript was not saved |
| System is maintainable | 55 tests, requirement-to-test matrix, small separated modules, refactor `8a906fa`, docstrings on every function | `stage07/`; `project/` @ `4713c07` | Aagney | Mostly | `find_appointment` loops through all appointments; no pytest drives the console (Part G) |
| FR-01–03 register/find and validation | T-01 to T-03, T-08 to T-10, T-15 to T-17, T-26 to T-31, saved UI-01/UI-02 runs; AC-01.1, AC-01.2, AC-02.1, AC-02.2 | `project/tests/`, `stage09/evidence/` @ `4713c07` | Aagney (ran regression) | Yes | None |
| FR-04–05 booking/conflict rules | T-04 to T-06, T-11, T-12, T-18, T-19, T-25, `test_f8_01_same_practitioner_same_time_is_rejected`, workflow test, saved UI-01 run; AC-03.1, AC-03.2, AC-04.1, AC-04.2 | `project/tests/` @ `4713c07`; issue #19 | Aagney (ran regression) | Yes | None |
| FR-06–08 cancellation/history/find | T-07, T-13, T-14, T-20 to T-24, `test_f8_02_...`, workflow test, saved UI-01/UI-02 runs; AC-05.1 to AC-05.3, AC-06.1 | `project/tests/` @ `4713c07` | Aagney (ran regression) | Yes | None |
| FR-09 and QRY/FP listing/filter/order/purity | `tests/test_queries.py` (10 tests, including equal-time tie-break, no-match and empty/sorted input), 5 service listing tests, workflow test; QRY-01 to QRY-04, FP-01 to FP-03 | `project/smartcare/queries.py`, `services.py`, PRs #29 and #30, `149f3f9` @ `4713c07` | Aagney (ran regression) | Yes | None. The tie-break test fails if the ID is removed from `appointment_sort_key` |
| UI full console sequence and error recovery | Saved human runs UI-01 and UI-02 (Aagney, Windows); UI-01 repeated on a fresh clone (Ngedup, macOS) | `stage09/evidence/`, `project/smartcare/console.py` @ `4713c07` | Aagney, Ngedup | Yes | No pytest drives `run_menu` (accepted debt, Part G) |
| Session-only scope / FR-10 retired | In-memory store only; every saved run starts empty in a new process and ends with `Goodbye. Session data is discarded.` | `project/smartcare/data_store.py`, `project/README.md` @ `4713c07` | Aagney | Yes | None |
| PG RES and assurance integration | Not applicable. UG-only group | N/A | N/A | N/A | None |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common (release candidate) | Windows, Python 3.14.3, pytest 8.3.5 | `project/`, `python -m pytest -q` | `4713c07` | 55 passed, 0 failed | Run by Aagney, 10 Nov 2026 |
| Fresh clone by another member | macOS, Python 3.14.3, new venv, pytest 8.3.5 | `project/`, `python -m pytest -q` | `b38384d` (code identical to `4713c07`) | 55 passed in 0.09s | Run by Ngedup, 11 Nov 2026 (Part F) |
| Complete PG if applicable | Not applicable. UG-only group | N/A | N/A | N/A | N/A |
| Original Stage 9 candidate | Windows, Python 3.14.3, pytest 8.3.5 | `project/`, `python -m pytest -v` | `351b6ca` | 50 passed, 0 failed | Run by Aagney, 9 Nov 2026 |
| Affected focused checks before PR #29 merge | Windows, Python 3.14.3, pytest 8.3.5 | `project/`, `python -m pytest -vv -s` on `feature/stage9-queries` | `5f7e2c0` | 44 passed, 0 failed | Run by Aagney before PR #29 merge |
| Stage 8 regression tests, fail-to-pass | Windows, Python 3.14.3, pytest 8.3.5 | `project/`, `python -B -m pytest tests/test_regressions.py -v` with each commit's `data_store.py` | `b99a90f` / `ed76dc8` / `bb07074` stores | 2 failed / 1 failed 1 passed / 2 passed | `stage08/` G |
| Earlier integrated recheck | Linux, Python 3.13.18, pytest 9.1.1 | `project/`, `python -m pytest -q` | `351b6ca` | 50 passed, 0 failed | Run by Copilot on an extracted copy, 9 Nov 2026 |
Prior assertions preserved / reviewed test diff: `git diff --stat 351b6ca 4713c07 -- project/tests` shows 144 insertions and 0 deletions (new `test_regressions.py`, three new tests in `test_queries.py`), so no earlier assertion was removed or weakened. Earlier, `git diff --stat 71ef3a4 351b6ca -- project/tests` showed 3 deleted lines in `test_services.py` from PR #30: test data changed from "Dr Smith" to "Dr. Smith" and "General Practice" to "Specialty", with one name assertion updated to match. No behaviour check was weakened.
Remaining failure / limitation: No test failures at `4713c07`. Both member runs used Python 3.14.3 with the pinned pytest 8.3.5, not the README baseline Python 3.13.


## D Console and end to end demonstration

Observed results come from the saved human runs `stage09/evidence/ui01_output.txt` and `ui02_output.txt` (Aagney, Windows, Python 3.14.3, 10 Nov 2026), each started as a new process with `python main.py --interactive` and scripted input. The same UI-01 script gave the same output after `4713c07` (Aagney) and on Ngedup's fresh clone (macOS, 11 Nov 2026).

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | SmartCare replaces manual appointment handling. Stakeholders: reception/admin staff, patients, practitioners | Explains who needs it and why | Presenter: Aagney | Requirements baseline Revision 2 |
| Register and find Patient and two Practitioners | P1 Alex Example; D1 Taylor Example; D2 Jordan Example | FR-01, FR-02, FR-03 | All registered and found with correct details | `ui01_output.txt` |
| Invalid/unknown lookup recovering to a usable menu | Blank patient ID; P9; duplicate P1 "Replacement Name" | FR-01, FR-02, NFR-04 | `Error: Patient ID cannot be blank`; `Error: Patient not found`; `Error: Patient ID already exists`; find P1 still shows `Alex Example` | `ui02_output.txt` |
| Valid booking | A1, P1, D1, 2026-10-01 09:00 | FR-04, AC-03.1 | `Booked A1: P1 with D1, 2026-10-01 09:00, scheduled` | `ui01_output.txt` |
| Same practitioner exact-time conflict rejected | A-CONFLICT, P1, D1, same time | FR-05, AC-04.1 | `Error: Practitioner already has a SCHEDULED appointment at this time` | `ui01_output.txt` |
| Different practitioner same time allowed | A2, P1, D2, same time | FR-05, AC-04.2 | `Booked A2: P1 with D2, 2026-10-01 09:00, scheduled` | `ui01_output.txt` |
| Failed input does not create a partial appointment | Four failed bookings of A1 (unknown patient, unknown practitioner, bad format, impossible date), then find A1 | NFR-01 | Each booking gave an error, then `Error: Appointment not found`, so nothing was stored | `ui02_output.txt` |
| Cancel SCHEDULED and retain/find CANCELLED object | Cancel A1, then find A1 | FR-06, FR-07, FR-08, AC-05.1, AC-05.2 | `Cancelled A1 ...`, then find A1 shows `cancelled` | `ui01_output.txt` |
| Invalid/repeated cancellation rejected | Cancel A1 again; find A99 | FR-06, AC-05.3 | `Error: Only SCHEDULED appointments may be cancelled`, A1 still `cancelled`; `Error: Appointment not found` | `ui02_output.txt` |
| Default all-status listing | List D1 with blank status | FR-09: all statuses shown, including CANCELLED | A1 listed as cancelled | `ui01_output.txt` |
| Explicit filtering / empty vs unknown / deterministic order | Filter D1 by `scheduled`; book A3 in the freed slot; list D1; list D9; blank practitioner ID | FR-09, QRY-02 to QRY-04 | `No matching appointments.` (known, empty); A3 booked; list shows A1 then A3 at the same time (ID order); D9 gives `Error: Practitioner not found`; blank gives `Error: Practitioner ID cannot be blank`. Ordering across different times and the equal-time tie-break are proved by `test_queries.py` | `ui01_output.txt`, `ui02_output.txt`, `project/tests/test_queries.py` |
| Invalid date/status/menu recovery and continued operation | Menu `9`; `01/10/2026 09:00`; `2026-02-30 09:00`; status `pending`; then find P1 | NFR-04, UI-02 | `Unknown choice...`; `Error: Use date/time format YYYY-MM-DD HH:MM`; `Error: Invalid calendar date/time...`; `Error: Status must be scheduled, cancelled or completed`; find P1 still works | `ui02_output.txt` |
| Session-only limitation and normal exit | Exit with 0; each run starts a new process | FR-10 retired: data lost on exit | `Goodbye. Session data is discarded.`; each new run starts with an empty store (UI-02 begins with `Patient not found`) | `ui01_output.txt`, `ui02_output.txt` |
| One meaningful requirement-linked pytest test explained | `test_cancelled_appointment_remains_in_history` (T-21) and `test_f8_02_cancelled_appointment_is_still_found` | FR-07, AC-05.2: same object still found, CANCELLED and in the list | Both failed with the F8-02 fault (`b99a90f`) and pass after repair (`bb07074`) | `project/tests/test_services.py`, `test_regressions.py`; `stage08/` G |
| Architecture and one actual AI decision / known limitation | Appointment.cancel holds the rule; the service finds the record and calls it. AI decision: Stage 7 H, Copilot's "no longer SCHEDULED" test modified to assert `CANCELLED` and identity. Limitation: exact-time conflicts only | Design and AI evidence can be explained | Presenter: Aagney | `stage07/` H, I |
| PG reschedule identity/participants/time and no-op | Not applicable. UG-only group | N/A | N/A | N/A |
| PG conflict/invalid status/failure non-mutation | Not applicable. UG-only group | N/A | N/A | N/A |
| PG old slot / current lookup/list ordering / assurance risks | Not applicable. UG-only group | N/A | N/A | N/A |
Stable demo owner / fresh process / command: Demo owner Aagney. From `project/`, in a fresh process: `python main.py --interactive`, or replay a saved script with `Get-Content ..\stage09\evidence\ui01_input.txt | python main.py --interactive`.
PG demonstrations through service/tests or not applicable: Not applicable. UG-only group.


## E Final code quality and AI review

Reviewed at `4713c07`.

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | `project/smartcare/` | No finding. `select_appointments` reads only its arguments, uses `sorted` and does no input/output. Services return objects or raise errors. Only `console.py` and `main.py` print | No change |
| PascalCase and snake_case naming | `project/smartcare/`, `project/tests/` | No finding | No change |
| Useful type hints and meaningful docstrings | `console.py`, `data_store.py`, `services.py`, `main.py` | Finding at `351b6ca`: 8 console command helpers, `find_appointment` and `has_practitioner_conflict` had no docstrings; stale starter text and the typo "Return's" remained in `services.py`, `run_menu` and `main.py`. Tests have no type hints | Corrected in `4713c07` (docstrings only). Rechecked: 55 passed and identical UI-01/UI-02 output. Test type hints accepted as minor |
| Four-space indentation and imports/layout | `project/smartcare/`, `project/main.py` | One trailing-whitespace line in `console.py` and inconsistent blank lines between top-level definitions | Corrected in `4713c07` |
| Focused methods / duplication / dead or commented code | `data_store.py`, `main.py` | The `NotImplementedError` handler in `main.py` was dead code. `find_appointment` loops through every appointment. No commented-out code | Handler removed in `4713c07`. Loop accepted as minor debt (Part G) |
| Globals / leakage / unnecessary inheritance or frameworks | `project/smartcare/` | No global state. No inheritance beyond `Enum`, no frameworks. `MENU_TEXT` is a constant | No change |
| No SQLite/persistence/repository ABCs/speculative features | `project/smartcare/` | No finding | No change |
| Synthetic data / secrets / dependencies / provenance | `project/requirements-dev.txt`, `.gitignore`, tracked files | No secrets found by word scan. Example data is synthetic. Only dev dependency is `pytest==8.3.5`; runtime is standard library. The `prepare_debugging.py` ignore line was removed in Stage 8 (`b99a90f`) | Ignore line restored in `b38384d`. `git ls-files` shows no Stage 8 tool |
| Significant common Copilot contributions and human verification | `stage06/` H, I; `stage07/` H, I; `stage08/` F; `stage09/` E | Copilot reviewed PR #15, proposed Stage 7 test candidates, ranked causes for F8-01 and F8-02 and reviewed Stage 9. Humans checked each against code and test runs | No change |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | N/A | Not applicable. UG-only group | N/A |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| Copilot: PR #15 meets AC-05.1 to AC-05.3 | FR-06, FR-07; `cancel_appointment` | Ngedup compared it with the code at `5244ad3` and saw that no test at merge time called the method | Modify. Code supported the results, but Copilot had no test evidence | Stage 7 tests T-20 to T-23 later added direct evidence |
| Copilot: F8-01 is caused by `!=` instead of `==` in the conflict check; two other causes ranked lower | FR-05, AC-04.1; `has_practitioner_conflict` | Inspected code and reran the failing tests | Accept first cause, reject the other two, as the evidence did not support them | Repaired in `ed76dc8`; focused tests passed |
| Copilot: F8-02 is caused by a cancelled-status filter in `find_appointment`; two other causes ranked lower | FR-07, AC-05.2, AC-06.1; `find_appointment` | Inspected code and reran the failing tests | Accept first cause, reject the other two, as the evidence did not support them | Repaired in `bb07074`; focused tests passed |
| Copilot: PR #29 tie-break test does not prove ID ordering, because A1 is already before A4 in the source list | QRY-03; `tests/test_queries.py` | Removed the ID from the key in a scratch copy: the old sort test still passed | Accept | Added `test_select_appointments_breaks_equal_time_ties_by_appointment_id` (`149f3f9`); it fails when the ID is removed from the key |
| Copilot: drafted parts of this Stage 12 record from the repo and ran a console script | Stage 12 record | Aagney checked the entries against the repo and Git output | Modify. Entries were kept where supported by repo evidence; unconfirmed reviews and approvals were removed | The Copilot console run was replaced as evidence by saved human runs (`stage09/evidence/`) |
| Claude (Anthropic), 10–11 Nov 2026: checked stage records against GitHub history; drafted `test_regressions.py`, three query tests, the release docstrings, both READMEs and record text | Stage 6–9 and 12 records; `project/tests/`; `project/smartcare/` docstrings | Aagney ran every test himself, including on the faulty and partly repaired Stage 8 data stores; Ngedup reran the suite on a fresh clone | Modify. Record claims were changed where GitHub disagreed (merge titles saying "Approved" were not approvals); tests were kept only after they failed on faulty code and passed on repaired code | 52, then 55 passed; identical console output before and after the tidy-up |
Access route or approved equivalent / limitations: GitHub Copilot is the nominated assistant and was used in Stages 6 to 9 and for this record. Claude (Anthropic) was also used on 10–11 Nov 2026 for the post-deadline corrections; it is not a teaching-team confirmed route and is disclosed here. Tutor approval for either route was not asked.
Available AI evidence and missing evidence honestly disclosed: Stage 6 H and I, Stage 7 H and I, the Stage 8 prompts and Stage 9 part E are available. The Stage 6 Copilot review was done after merge, on 9 Nov 2026. The Stage 9 Copilot transcript was not saved. Stage 6 PRs #8, #9 and #10 record no Copilot use. Earlier reviews were weak: PRs #8 and #9 have no recorded approval.


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | `README.md`, `project/README.md` | Aagney; Ngedup (fresh clone) | Present. `project/README.md` rewritten in `149f3f9`; root README updated with release label and scope after Ngedup's check |
| Out-of-scope capabilities and known limitations | `project/README.md`, Part G | Aagney | Present: session-only data, no authentication, conflicts, completion workflow or rescheduling. Wider exclusions in Part G |
| Confirmed teaching Python version and dependency installation | `README.md`, `project/README.md`, `project/requirements-dev.txt` | Ngedup | Baseline is Python 3.13. Ngedup's new venv used Python 3.14.3; `pip install -r requirements-dev.txt` installed pytest 8.3.5 |
| Working directory / demo / interactive / test commands | `README.md`, `project/README.md` | Ngedup | Worked from `project/`. On macOS the environment needs `python3 -m venv .venv` and `source .venv/bin/activate`; this note was added to the root README |
| Repository structure and architecture responsibilities | `project/README.md` | Aagney; Ngedup | Present: domain, store, services, queries and console responsibilities |
| Responsible AI summary / synthetic-data rule | `README.md` "Scope, data and AI use" | Aagney | Present |
| Release label/version and SHA links | `README.md` group index | Aagney | Present: v1.0-common, verified code SHA `4713c07` |
Root README index and project/README verified: `project/README.md` commands were reproduced by Ngedup. The root README group index was completed in the commit after his clone, so its wording was not part of that check.
Fresh clone or extracted ZIP / candidate identity: Ngedup ran `git clone https://github.com/Blahuee/st1-assignment-3` on his own Mac, 11 Nov 2026. `git rev-parse HEAD` gave `b38384d`. Its code is identical to `4713c07`: `git diff 4713c07 b38384d` changes only `.gitignore` and the Stage 9 record.
Verifier and clean environment / actual version: Ngedup Jigme Lhazeen, macOS, Python 3.14.3, new virtual environment, pytest 8.3.5. He did not author the 10 Nov changes.
Setup/run/test commands and observed results: From `project/`: `pip install -r requirements-dev.txt` installed pytest 8.3.5; `python main.py` printed `A1: P1 with DR1, 2026-10-01 09:00, scheduled` and the session-only message; `python -m pytest -q` gave `55 passed in 0.09s`; replaying `stage09/evidence/ui01_input.txt` gave `Booked A1`, the conflict error, `Booked A2`, `Booked A3` and `Goodbye`, matching Aagney's saved run.
Missing local file or setup gap / remedy and recheck: No missing files; the clone needed nothing from the author's machine. Gap: macOS commands differ from the Windows-style commands; a macOS note was added to the root README.


## G Known limitations debt and release notes

Delivered features: Register and find patients and practitioners; book with exact-time practitioner conflict checks; find appointments; cancel while keeping history; list a practitioner's appointments with optional status filter and deterministic order; interactive console menu with error recovery.
Important fixes: F8-01 practitioner conflict check corrected (`ed76dc8`, issue #19). F8-02 cancelled appointments can be found again (`bb07074`, issue #20). Dedicated regression tests for both faults added after the deadline (`dc1c9e9`).
Architecture/quality improvements: Conflict check uses `AppointmentStatus.SCHEDULED` instead of a raw string (`8a906fa`). Pure queries are separated from services and console. Docstrings corrected and completed and dead code removed (`4713c07`). Tests grew from 8 supplied to 55.
Known limitations: Data lasts for one session only. Conflicts are exact-time only because appointments have no duration. No patient-conflict, age or past-date rules. Console only.
AI-assisted development note: GitHub Copilot was used for review, test ideas and ranking possible defect causes. Claude (Anthropic) was used on 10–11 Nov 2026 to check records against Git history and draft tests, docstrings and documentation. People ran and verified every change and remain responsible for the code and its verification.

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| `find_appointment` loops through all appointments | Slower with many records; inconsistent with other lookups | Low | Use a dictionary lookup | Yes. Correct at teaching scale |
| No pytest calls `parse_date_time`, `parse_status` or `run_menu` directly | Console errors are protected only by saved scripted runs, not automated tests | Medium | Add console tests that feed scripted input | Yes for this release. Saved UI-01/UI-02 runs are reproducible |
| Tests have no type hints | Slightly less readable | Low | Add hints to helper functions | Yes |
| Exact-time conflict only, no duration | Overlapping appointments would be allowed if durations existed | Medium | Add duration and overlap rules if required | Yes, in line with the baseline: no duration rules apply |
| No persistence | Data is lost on exit | Medium for real use | Add storage in a future production version | Yes, FR-10 is retired |
| Weak or missing review: Stage 6 PRs #8, #9, #12; Stage 9 PRs #29, #30; 10 Nov corrections committed without a PR | Less confidence in those merges | Medium | Require an approved PR before every merge | Offset by full-suite reruns and Ngedup's independent fresh-clone check |
Session-only synthetic data and minute-precision local time: All data is synthetic and kept in memory for one session. Times are naive local datetimes at minute precision; the console accepts exactly `YYYY-MM-DD HH:MM`.
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: None of these are included. They are out of scope for this teaching release.
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: One user, one process, no concurrency handling, no timezone policy, no logging or monitoring, and a basic console with no accessibility testing.
Difference between accepted scope limit and unresolved required behaviour: A scope limit is something the requirements leave out, such as persistence. Unresolved required behaviour is something the requirements ask for that does not work. No unresolved required behaviour was found at `4713c07`.
PG assurance residual risks / owner / status or not applicable: Not applicable. UG-only group.


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| FR-09, QRY/FP, console menu | At `c900456` the menu and listing raised `NotImplementedError` | High, was a release blocker | Alicia implemented; resolved | PRs #29, #30, #31, ending at `351b6ca` | 50 passed at `351b6ca` | None |
| Stage 8 regression tests in `test_regressions.py` | The Stage 8 handout requires the file; it was missing in every branch | Medium (evidence) | Aagney; resolved after the deadline | `dc1c9e9` | 2 failed on `b99a90f` store, 2 passed on `bb07074` store; full 52 passed | Added after the repairs and without review |
| QRY-02 no-match, QRY-03 equal-time tie-break, FP-02 empty/sorted input untested | The old sort test still passed with the ID removed from the key | Medium | Aagney; resolved after the deadline | `149f3f9` | `test_queries.py` 10 passed; full 55 passed | None |
| UI-01/UI-02 only shown by a Copilot run and a partial hand run | No saved human console evidence | Medium | Aagney; resolved after the deadline | `149f3f9` (`stage09/evidence/`) | Re-ran on `4713c07` and on Ngedup's fresh clone: same output | No pytest drives the console |
| README accurate and reproducible | Group index had `[complete]` placeholders; `project/README.md` described the Stage 6 starter | High for submission | Aagney; resolved after the deadline | `149f3f9` (project README); root README in the final commit | Ngedup's fresh clone ran the commands successfully | None |
| Docstrings and dead code | Stale starter text, "Return's", 10 missing docstrings, unused `NotImplementedError` handler | Low | Aagney; resolved after the deadline | `4713c07` | 55 passed; UI-01/UI-02 output identical before and after | None |
| Stage 8 tool exclusion | `b99a90f` removed `prepare_debugging.py` from `.gitignore` | Low | Aagney; resolved | `b38384d` | `git ls-files` shows no tool file | None |
| Python version evidence | README baseline is Python 3.13; members used 3.14.3 | Low | Recorded | No code change needed | 55 passed on 3.14.3 (Windows and macOS) | Not rerun on 3.13 with pytest 8.3.5 |
Justified no-change conclusion if no defect found: Not applicable. Findings were corrected as listed.
Release blockers still open / status: None. All corrections above were made after the 9 Nov 2026 deadline (main was then at `161c84a`) and are dated in the commit history.


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: PR #29 https://github.com/Blahuee/st1-assignment-3/pull/29 (`5f7e2c0`); PR #30 https://github.com/Blahuee/st1-assignment-3/pull/30 (`e64579b`); PR #31 https://github.com/Blahuee/st1-assignment-3/pull/31 (`c3bace9`); PR #32 https://github.com/Blahuee/st1-assignment-3/pull/32. Earlier: issues #1, #3, #19, #20; PRs #8, #9, #10, #15, #21. Post-deadline commits: `dc1c9e9`, `149f3f9`, `4713c07`, `b38384d` and the README/Stage 12 record commit.
Independent reviewer / feedback / response: Alicia authored the three Stage 9 code PRs. PRs #29 and #30 were merged by Aagney with no formal approval recorded on GitHub. PR #31 shows as Approved on GitHub and was merged by Ngedup. The 10 Nov corrections were committed directly by Aagney without a PR review; Ngedup's fresh-clone run (Part F) is the independent check of the release candidate.
Integration commit / full recheck: `4713c07`; 55 passed on Aagney's computer (Windows) and on Ngedup's fresh clone (macOS).
Tracked and untracked file inspection / cleanliness: `git ls-files` lists only `README.md`, `.gitignore`, `project/` (source, tests, README, `main.py`, `requirements-dev.txt`), the seven stage folders and `stage09/evidence/`. `git status` was clean before each commit. No caches, environments or Stage 8 utility files are tracked.
Secrets/staff material/caches/tool-metadata exclusion check: Word scan found no secrets, and `.gitignore` covers environments, caches, `.env`, Stage 8 folders and `prepare_debugging.py`. No staff material was found in tracked file names.
Candidate recovery plan / known-good SHA: Release code: `4713c07` (55 passed). Deadline state: `161c84a`. Original Stage 9 candidate: `351b6ca` (50 passed). To recover, make a branch from one of these or use `git revert`; do not rewrite shared history.
Named substantive contributions: Alicia: lookup and cancellation services, Stage 8 repairs and refactor, Stage 9 queries, listing, menu and tests. Aagney: Stage 7 matrix and tests, review of PR #21, merges of PRs #21, #29 and #30, Stage 12 regression run and record, and the 10 Nov corrections (regression and query tests, console evidence, READMEs, tidy-up). Ngedup: Stage 6 records, Copilot review of PR #15, review of PR #21, Stage 9 Parts A, B and G, merges of PRs #31 and #32, and the independent fresh-clone check.


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: READY WITH DOCUMENTED LIMITATIONS.
Approver / date / rationale and evidence: Aagney Mani Sharma, 11 Nov 2026, after Ngedup's independent fresh-clone check. Evidence: 55 tests pass on two members' machines and operating systems (C), saved console runs cover UI-01 and UI-02 (D), a fresh clone reproduced setup, demo, tests and menu without the author's environment (F), and every release finding is corrected or accepted (H).
What risks remain / conditions / owners: No pytest drives the console (accepted debt); PRs #29 and #30 and the 10 Nov corrections had no formal review; the corrections were made after the 9 Nov deadline (state at deadline `161c84a`). Owner for all: Aagney.
Can the team explain the system: Each member can explain the parts they built or reviewed (I). A full group walk-through is still to be done before the team viva.
Can a change be recovered: Yes. `4713c07`, `161c84a` and `351b6ca` are known commits, and changes can be undone with `git revert`.
Common decision / PG decision where different: Common decision as above. PG not applicable.


## K Final tested release SHA

Exact common tested SHA: 4713c0732be02600c5e068b6d288642a900976a0
Exact PG tested SHA or not applicable: Not applicable. UG-only group.
Final submitted SHA / repository URL: The repository link was submitted on Canvas before the deadline. At the deadline (9 Nov 2026, 11:59 pm), main was at 161c84a4b6afb2274a2eee94509551315a4a63d0. The current final commit is the one that adds this record and the root README; a file cannot contain its own commit SHA, so see the latest commit on main. Repository: https://github.com/Blahuee/st1-assignment-3
Evidence-only later commit and difference explanation: `b38384d` and the final README/record commit change only `.gitignore`, `README.md` and stage records. `git diff 4713c07 <final SHA> -- project` shows no changes.
Executable changes after testing and re-verification: None after `4713c07`. `4713c07` itself was re-verified (55 passed; identical console output).
Source ZIP name / SHA correspondence / extracted comparison: The Canvas route takes a repository link only, so no ZIP was uploaded. On 9 Nov 2026 a local `smartcare-submission.zip` was made with `git archive` at `351b6ca`; it predates the corrections and is not the release candidate. If a ZIP of the release is requested, it can be made with `git archive --format=zip --output=../SmartCare-release.zip <final SHA>` from the repository root.


## L Submission package verification

- [x] Feature freeze and scoped requirements traced. (Features frozen at `351b6ca`; only tests, documentation and a behaviour-preserving tidy-up after.)
- [x] Applicable full regressions, integrated demo and invalid paths verified.
- [x] Architecture/code quality and final AI/dependency checks complete.
- [x] Root README and project/README reproduced by another verifier. (Ngedup reproduced the `project/README.md` commands on a fresh clone; the root README group index was completed in the following commit.)
- [x] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded. (Partly: independent fresh-clone check and decision recorded; PRs #29, #30 and the 10 Nov corrections had no PR review.)
- [x] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore. (Canvas takes a link only; the only ZIP made was a local one at `351b6ca`, before the corrections.)
- [x] project/ source and all accumulated applicable tests included.
- [x] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP. (No release ZIP; tracked files checked instead, Part I.)
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP. (No release ZIP; tracked files checked instead, Part I.)
- [x] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately. (In progress at the time of writing.)

Confirmed assessment item/upload route: Repository link submitted on Canvas before the deadline. No ZIP route.
Deadline/timezone: 9 Nov 2026, 11:59 pm, Australia/Sydney. Changes from 10 Nov 2026 are after the deadline.
Repository access arrangement: Public repository: https://github.com/Blahuee/st1-assignment-3
Mixed-candidate upload arrangement: Not applicable. All members are UG.
Oral/video recording/accessibility arrangements: Not confirmed at the time of writing.
Remaining administration or release dependency: An email to the tutor disclosing the post-deadline changes and the deadline commit `161c84a` was prepared by Aagney. Group reflection, peer forms and team viva are handled separately.


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

Strongest evidence SmartCare is ready: The two Stage 8 faults. `test_regressions.py` fails on the faulty data store (`b99a90f`) and passes after the repairs (`bb07074`), and the full suite of 55 tests passes on a fresh clone on another member's Mac (Part F). This shows the tests detect real defects and the release does not depend on one person's machine.
Weakest area: Review discipline. Several PRs (#8, #9, #12, #29, #30) and the 10 Nov corrections were merged without a formal approval, and the console has no automated test.
How AI use changed from Stage 1 to Stage 12: Early on, Copilot output was accepted on code-reading alone (the Stage 6 review of PR #15 said "Met" with no test run). By Stage 8 we wrote our own hypotheses first and used Copilot only to rank causes we then checked. By Stage 12 every AI-drafted test was accepted only after we saw it fail on faulty code and pass on repaired code. Stage 1 material is not available for comparison.
Start doing — engineering and AI use: Engineering: require an approved PR before every merge, and write the regression test before making the fix. AI: save prompts and transcripts at the time.
Stop doing — engineering and AI use: Engineering: merging our own PRs, and typing "Approved" into merge titles when no approval exists. AI: treating a confident AI review as evidence without running the tests.
Continue doing — engineering and AI use: Engineering: tracing every test to an FR/AC and recording the exact SHA and result of each run. AI: recording Accept/Modify/Reject with a reason for each significant suggestion.
What worked / caused rework / future delivery improvement: The Stage 7 traceability matrix worked well and made later gaps easy to find. Rework came from records that claimed more than GitHub showed and from late tests added after the deadline. Next time we would fill each stage record from the PR and test output on the day the work is done.
One paragraph — If AI can write code why do we still need software engineers: AI can produce code and tests quickly, but it does not know which requirement matters, whether a passing test proves anything, or whether a record matches what really happened. In this project Copilot proposed a cancellation test that would pass with the wrong status, and a confident review that had no test evidence. Engineers decide what to build, design tests that can fail for the right reason, check AI output against the code and the requirements, and take responsibility for what is released.

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | Staff need to book and cancel appointments without double-booking practitioners and without losing history. Stakeholders are staff, patients and practitioners. |
| Two requirements and acceptance criteria | FR-05: a practitioner cannot have two SCHEDULED appointments at the same time (AC-04.1), but a different practitioner can (AC-04.2). FR-07: a cancelled appointment stays retrievable (AC-05.2). See `stage07/` matrix. |
| Domain model and architecture | Patient, Practitioner, Appointment and AppointmentStatus are in `domain.py`. `SmartCareDataStore` holds records, services coordinate work, queries select and sort, and the console handles input and output. |
| Design trade-off | In-memory dictionaries keep the design simple and fit the session-only scope, but data is lost on exit. |
| Meaningful test and its limits / 100 percent coverage | T-21 proves cancelled appointments are retained. It does not prove the console works. 100 percent coverage only shows lines ran, not that the assertions or requirements are right. |
| Diagnosed defect and verification | F8-02: `find_appointment` skipped cancelled records. Tests T-21 and T-22 failed with `LookupError`; the filter was removed in `bb07074` and the focused tests then passed. `test_f8_02_cancelled_appointment_is_still_found` now protects it (`stage08/` G). |
| Shared store and session-state/query responsibilities | All three services share one store, so they see the same records in a session. The service gets a fresh list from the store and passes it to the pure `select_appointments`, which depends only on its arguments. |
| What would break if session-state lookup/query responsibilities changed? | If each service had its own store, booking could not see registered patients. If lookup hid cancelled records, FR-07 would break, which is what F8-02 did. If the query sorted its source in place, it would change the caller's list. |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | Cancel only needs the appointment's own status, so the rule sits on Appointment. A conflict needs other appointments, so the service asks the store, which can see them all. |
| FR-07 retained history test | `test_cancelled_appointment_remains_in_history`, `project/tests/test_services.py` @ `4713c07`. |
| Actual AI change rejected/modified or honestly accepted with verification | Stage 6 H: Copilot's review of PR #15 was modified, because it could not provide test evidence that AC-05.1 to AC-05.3 were met; Stage 7 tests T-20 to T-23 later supplied it. Stage 7 H: Copilot's "no longer SCHEDULED" test was modified to assert `CANCELLED` and object identity, and duplicate candidate TC-FR06-06 was rejected. |
| Personal contributions | Alicia: services, Stage 8 repairs and refactor, Stage 9 queries, listing and menu. Aagney: Stage 7 matrix and tests, Stage 12 regression runs, post-deadline tests, console evidence and READMEs. Ngedup: Stage 6 records, Copilot review of PR #15, Stage 9 Parts A, B and G, fresh-clone check. Details in Part I. |
| Limitation to address next / before real deployment | Next: automated console tests and a required approved PR for every merge. Before any real deployment: persistent storage, authentication and roles, appointment durations and overlap rules, and real privacy and security review. |