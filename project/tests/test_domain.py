from datetime import datetime
import pytest
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.console import parse_date_time

# PATIENT TESTS

# Check that blank or invalid patient IDs are rejected
def test_patient_id_must_not_be_blank_or_invalid():
    patient_ids: list = [
        "",
        " ",
        None,
    ]

    for patient_id in patient_ids:
        with pytest.raises(ValueError):
            Patient(patient_id, "Test Patient")

# Check that blank patient names are rejected
def test_patient_name_must_not_be_blank():
    names: list = [
        "",
        " ",
    ]

    for name in names:
        with pytest.raises(ValueError):
            Patient("P1", name)

# Check that spaces are removed from patient details
def test_patient_details_are_trimmed():
    patient = Patient(" p1 ", " Test Patient ")

    assert patient.patient_id == "p1"
    assert patient.name == "Test Patient"

# Check that patient IDs preserve their case
def test_patient_id_preserves_case():
    patient = Patient("p1", "Test Patient")

    assert patient.patient_id == "p1"
    assert patient.patient_id != "P1"

# Check that the patient ID cannot be changed
def test_patient_id_cannot_be_changed():
    patient = Patient("P1", "Test Patient")

    with pytest.raises(AttributeError):
        patient.patient_id = "replacement"

# PRACTITIONER TESTS

# Check that blank or invalid practitioner IDs are rejected
def test_practitioner_id_must_not_be_blank_or_invalid():
    practitioner_ids: list = [
        "",
        " ",
        None,
    ]

    for practitioner_id in practitioner_ids:
        with pytest.raises(ValueError):
            Practitioner(
                practitioner_id,
                "Dr Smith",
                "General Practice"
            )

# Check that blank practitioner names are rejected
def test_practitioner_name_must_not_be_blank():
    names: list = [
        "",
        " ",
    ]

    for name in names:
        with pytest.raises(ValueError):
            Practitioner("D1", name, "General Practice")

# Check that blank practitioner specialties are rejected
def test_practitioner_specialty_must_not_be_blank():
    specialties: list = [
        "",
        " ",
    ]

    for specialty in specialties:
        with pytest.raises(ValueError):
            Practitioner("D1", "Dr Smith", specialty)

# Check that spaces are removed from practitioner details
def test_practitioner_details_are_trimmed():
    practitioners: list[tuple] = [
        (" D1 ", " Name ", " Specialty "),
        (" D2 ", " Name ", " Specialty "),
        (" D3 ", " Name ", " Specialty ")
    ]

    for practitioner_id, name, specialty in practitioners:
        practitioner = Practitioner(
            practitioner_id,
            name,
            specialty
        )

        assert practitioner.practitioner_id == practitioner_id.strip()
        assert practitioner.name == name.strip()
        assert practitioner.specialty == specialty.strip()

# Check that practitioner IDs preserve their case
def test_practitioner_id_preserves_case():
    practitioners: list[tuple] = [
        ("d1", "Name", "specialty "),
        ("D2", "NaMe", "SPECIALTY "),
        ("d3", "name", "Specialty ")
    ]

    for practitioner_id, name, specialty in practitioners:
        practitioner = Practitioner(
            practitioner_id,
            name,
            specialty
        )

        assert practitioner.practitioner_id == practitioner_id
        assert practitioner.practitioner_id != practitioner_id.swapcase()

# Check that the practitioner ID cannot be changed
def test_practitioner_id_cannot_be_changed():
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    with pytest.raises(AttributeError):
        practitioner.practitioner_id = "replacement"

# APPOINTMENT CONSTRUCTION TESTS

# Check that a new appointment starts as SCHEDULED
def test_new_appointment_is_scheduled():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 2, 10, 0)
    )

    assert appointment.status == AppointmentStatus.SCHEDULED

# Check that an appointment requires valid participant objects
def test_appointment_requires_valid_participants():
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")
    patient = Patient("P1", "Test Patient")
    appointment_time = datetime(2026, 11, 2, 10, 0)

    with pytest.raises(ValueError):
        Appointment("A1", "P1", practitioner, appointment_time)

    with pytest.raises(ValueError):
        Appointment("A2", patient, "D1", appointment_time)

# Check that an appointment requires minute precision
def test_appointment_requires_minute_precision():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    with pytest.raises(ValueError):
        Appointment(
            "A1",
            patient,
            practitioner,
            datetime(2026, 11, 2, 10, 30, 15)
        )

# Check that an appointment rejects a non-datetime value
def test_appointment_rejects_invalid_datetime():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    with pytest.raises(ValueError):
        Appointment(
            "A1",
            patient,
            practitioner,
            "2026-11-02 10:00"
        )

# Check that an appointment rejects an invalid status
def test_appointment_rejects_invalid_status():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    with pytest.raises(ValueError):
        Appointment(
            "A1",
            patient,
            practitioner,
            datetime(2026, 11, 2, 10, 0),
            "scheduled"
        )

# APPOINTMENT CANCELLATION TESTS

# Check that a scheduled appointment can be cancelled
def test_scheduled_appointment_can_be_cancelled():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 2, 10, 0)
    )

    appointment.cancel()

    assert appointment.status == AppointmentStatus.CANCELLED

# Check that a cancelled appointment cannot be cancelled again
def test_cancelled_appointment_cannot_be_cancelled_again():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 2, 10, 0)
    )

    appointment.cancel()

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status == AppointmentStatus.CANCELLED

# Check that a completed appointment cannot be cancelled
def test_completed_appointment_cannot_be_cancelled():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")

    appointment = Appointment(
        "A1",
        patient,
        practitioner,
        datetime(2026, 11, 2, 10, 0),
        AppointmentStatus.COMPLETED
    )

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status == AppointmentStatus.COMPLETED