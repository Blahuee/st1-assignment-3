# SmartCare (Assignment 3, common UG scope)

Requirements baseline: SmartCare A3 2026 revision 2. Runtime uses only the Python standard library; tests use pytest 8.3.5 (`requirements-dev.txt`). Verified with Python 3.14.3 on Windows.

## Run

From this `project/` directory:

```sh
python -m pip install -r requirements-dev.txt   # first time only
python main.py                    # short synthetic demo
python main.py --interactive      # full menu
python -m pytest -q               # full test suite
```

## Menu

| Choice | Action |
|---|---|
| 1 / 2 | Register patient (ID, name) / find patient by ID |
| 3 / 4 | Register practitioner (ID, name, specialty) / find practitioner by ID |
| 5 | Book appointment (appointment ID, patient ID, practitioner ID, `YYYY-MM-DD HH:MM`) |
| 6 / 7 | Cancel appointment / find appointment by ID |
| 8 | List a practitioner's appointments; status blank = all, or `scheduled` / `cancelled` / `completed` |
| 0 | Exit (session data is discarded) |

Invalid input, unknown or duplicate IDs, booking conflicts, repeated cancellation and invalid status show an `Error:` message and return to the menu without changing stored records.

## Structure

- `smartcare/domain.py`: Patient, Practitioner, Appointment and AppointmentStatus; Appointment owns the guarded cancellation.
- `smartcare/data_store.py`: one in-memory store per session (add, find, list).
- `smartcare/services.py`: registration, lookup, booking with practitioner-conflict check, cancellation and validated practitioner listing.
- `smartcare/queries.py`: pure `select_appointments` and named `appointment_sort_key` (date/time, then appointment ID).
- `smartcare/console.py`: menu input/output only; converts status text to the enum and calls the services.
- `tests/`: supplied starter checks plus domain, service, regression, query and workflow tests.

## Scope and limitations

- Data lasts only for the current session and is lost on exit. FR-10 restart persistence is retired; there is no database or file storage.
- Use synthetic data only.
- Not implemented (out of scope): authentication, patient conflicts, duration overlaps, past-date or clinic-hours rules, appointment completion workflow, rescheduling (PG only).
- The console is checked by scripted runs (`stage09/evidence/`), not by an automated console test.