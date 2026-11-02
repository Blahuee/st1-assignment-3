from datetime import datetime
import pytest
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)

from smartcare.console import parse_date_time

def test_blank_fields_and_trimmed_case_sensitive_identity():
    patients: list[tuple] = [
        ("", "Name"),
        ("P", " "),
        (None, "Name")
        ]
    for patient_id, name in patients:
        with pytest.raises(ValueError):
            Patient(patient_id, name)

    practitioners: list[tuple] = [
        ("", "","")
    ]