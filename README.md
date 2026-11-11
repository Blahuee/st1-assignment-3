# Software Technology 1 Assignment 3

One group repository and one evolving SmartCare application.
Release: **SmartCare A3 common release v1.0-common** (UG scope), requirements baseline 2026 revision 2.

## Group index

- **Group and tutorial:** Tue 1:30 - 3:30 Group 1
- **Member names, GitHub usernames and UG/PG cohorts:**
  - Alicia Hurst (Blahuee) - UG
  - Aagney Mani Sharma (Aagneyf1r3) - UG
  - Ngedup Jigme Lhazeen (njlhazin) - UG
- **Shared repository URL:** [Github Repo](https://github.com/Blahuee/st1-assignment-3)
- **Latest completed stage:** Stage 12 (UG pathway 6 → 7 → 8 → 9 → 12; Stages 10 and 11 are PG-only and left unchanged)
- **Verified code SHA:** `4713c0732be02600c5e068b6d288642a900976a0` (last commit that changed code)
- **Test command, working directory and observed result:**
  - **Test Command:** `python -m pytest -q`
  - **Working Directory:** `project/`
  - **Observed Result:** 55 passed, 0 failed (Windows, Python 3.14.3, pytest 8.3.5, 10 Nov 2026; repeated on a fresh clone on macOS, 11 Nov 2026)
- **Final submitted SHA, if different from tested code SHA:** The latest commit on `main`. Commits after `4713c07` change only `.gitignore`, this README and the stage records, not code. See Stage 12 Part K.
- **Deadline note:** The repository link was submitted before the 9 Nov 2026 11:59 pm deadline, when `main` was at `161c84a`. Corrections made from 10 Nov 2026 onward are listed in Stage 12 Parts H and K and are dated in the commit history.

Do not put student IDs, private peer ratings, credentials or personal contact details here.

## Application and evidence

- [Application setup, menu, structure and limitations](project/README.md)
- [Stage 6 activities and evidence](stage06/stage06_activities_and_evidence.md)
- [Stage 7 activities and evidence](stage07/stage07_activities_and_evidence.md)
- [Stage 8 activities and evidence](stage08/stage08_activities_and_evidence.md)
- [Stage 9 activities and evidence](stage09/stage09_activities_and_evidence.md) (console runs in [stage09/evidence](stage09/evidence))
- [Stage 10 PG activities and evidence](stage10_pg/stage10_activities_and_evidence.md) (PG only, not applicable to this UG group)
- [Stage 11 PG activities and evidence](stage11_pg/stage11_activities_and_evidence.md) (PG only, not applicable to this UG group)
- [Stage 12 activities and evidence](stage12/stage12_activities_and_evidence.md)

Git commands run from this root. Application commands run from `project/`:

```sh
cd project
python -m pip install -r requirements-dev.txt
python main.py
python main.py --interactive
python -m pytest -q
cd ..
```

On macOS/Linux, create the environment with `python3 -m venv .venv` and activate it with `source .venv/bin/activate`.

## Scope, data and AI use

- **Included (common scope):** register and find patients and practitioners; book appointments with exact-time practitioner conflict checks; find and cancel appointments while keeping cancelled history; list a practitioner's appointments with an optional status filter in date/time then ID order; a repeating console menu with error recovery.
- **Not included:** PG rescheduling and assurance (Stages 10–11), persistence after exit (FR-10 retired), authentication, notifications, billing and clinical rules. See `project/README.md` and Stage 12 Part G.
- **Data:** synthetic only, kept in memory for one session and lost on exit.
- **Environment:** the supplied baseline was verified with Python 3.13 and pytest 8.3.5; this group ran Python 3.14.3 with pytest 8.3.5. The runtime uses only the standard library.
- **AI use:** GitHub Copilot was used for code review (Stage 6), test ideas (Stage 7), ranking defect causes (Stage 8) and a query/console review (Stage 9). Claude (Anthropic) was used on 10–11 Nov 2026 to check records against Git history and draft tests, docstrings and documentation. Every significant suggestion was checked by group members against the code, requirements and test runs, and recorded as Accept, Modify or Reject in the stage records. The group is responsible for all submitted work.

The Stage 8 preparation utility is a staff teaching asset. It is not in this repository and is excluded by `.gitignore`.
