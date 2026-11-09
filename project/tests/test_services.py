from datetime import datetime
import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
)
from smartcare.services import (
    PatientService,
    PractitionerService,
    AppointmentService,
)

# TEST DATA SETUP

# Create a fresh data store and register test participants
def create_test_services():
    data_store = SmartCareDataStore()

    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient("P1", "Test Patient")

    practitioner_service.register_practitioner(
        "D1",
        "Dr. Smith",
        "Specialty"
    )

    return (
        data_store,
        patient_service,
        practitioner_service,
        appointment_service
    )

# T-15: PATIENT SEARCH

# Check that a known patient is returned and an unknown patient is rejected
def test_find_patient_returns_known_patient_and_rejects_unknown():
    data_store, patient_service, _, _ = create_test_services()

    registered_patient = data_store.find_patient("P1")
    original_patient = patient_service.find_patient("P1")

    assert original_patient is registered_patient
    assert original_patient.patient_id == "P1"
    assert original_patient.name == "Test Patient"

    with pytest.raises(LookupError):
        patient_service.find_patient("P99")

# T-16: BLANK PATIENT SEARCH

# Check that blank and spaces-only patient IDs raise ValueError
def test_find_patient_rejects_blank_ids():
    _, patient_service, _, _ = create_test_services()

    patient_ids: list = [
        "",
        " "
    ]

    for patient_id in patient_ids:
        with pytest.raises(ValueError):
            patient_service.find_patient(patient_id)

# T-17: PRACTITIONER SEARCH

# Check that a known practitioner is returned and an unknown one is rejected
def test_find_practitioner_returns_known_and_rejects_unknown():
    data_store, _, practitioner_service, _ = create_test_services()

    registered_practitioner = data_store.find_practitioner("D1")
    original_practitioner = practitioner_service.find_practitioner("D1")

    assert original_practitioner is registered_practitioner
    assert original_practitioner.practitioner_id == "D1"
    assert original_practitioner.name == "Dr. Smith"

    with pytest.raises(LookupError):
        practitioner_service.find_practitioner("D99")

# T-18: APPOINTMENT BOOKING BOUNDARY

# Check that an exact-time conflict is rejected but one minute later is allowed
def test_booking_conflict_only_applies_to_exact_datetime():
    data_store, _, _, appointment_service = create_test_services()

    appointment_time = datetime(2026, 11, 5, 10, 0)

    original_appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        appointment_time
    )

    # Attempt to book the same practitioner at the same time
    with pytest.raises(ValueError):
        appointment_service.book_appointment(
            "A2",
            "P1",
            "D1",
            appointment_time
        )

    # Check that the rejected booking did not change existing records
    assert data_store.list_appointments() == [original_appointment]
    assert original_appointment.status is AppointmentStatus.SCHEDULED

    # Book the same practitioner one minute later
    second_appointment = appointment_service.book_appointment(
        "A3",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 1)
    )

    assert second_appointment.appointment_id == "A3"
    assert len(data_store.list_appointments()) == 2

# T-19: REUSE CANCELLED APPOINTMENT SLOT

# Check that a cancelled appointment no longer occupies its time slot
def test_cancelled_appointment_slot_can_be_reused():
    _, _, _, appointment_service = create_test_services()

    appointment_time = datetime(2026, 11, 5, 10, 0)

    appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        appointment_time
    )

    appointment_service.cancel_appointment("A1")

    new_appointment = appointment_service.book_appointment(
        "A2",
        "P1",
        "D1",
        appointment_time
    )

    assert new_appointment.appointment_id == "A2"
    assert new_appointment.status is AppointmentStatus.SCHEDULED

# T-20: SERVICE CANCELLATION

# Check that cancelling returns the same appointment with CANCELLED status
def test_cancel_appointment_returns_cancelled_object():
    _, _, _, appointment_service = create_test_services()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    cancelled_appointment = appointment_service.cancel_appointment("A1")

    assert cancelled_appointment is appointment
    assert cancelled_appointment.status is AppointmentStatus.CANCELLED

# T-21: RETAIN CANCELLED HISTORY

# Check that a cancelled appointment remains retrievable and in the list
def test_cancelled_appointment_remains_in_history():
    data_store, _, _, appointment_service = create_test_services()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    appointment_service.cancel_appointment("A1")

    found_appointment = appointment_service.find_appointment("A1")

    assert found_appointment is appointment
    assert found_appointment.status is AppointmentStatus.CANCELLED
    assert data_store.list_appointments() == [appointment]

# T-22: INVALID CANCELLATION

# Check that repeated and COMPLETED cancellations raise ValueError
def test_repeated_and_completed_cancellation_are_rejected():
    data_store, patient_service, practitioner_service, appointment_service = (
        create_test_services()
    )

    # Create and cancel a scheduled appointment
    cancelled_appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    appointment_service.cancel_appointment("A1")

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment("A1")

    assert cancelled_appointment.status is AppointmentStatus.CANCELLED

    # Create a COMPLETED appointment
    completed_appointment = Appointment(
        "A2",
        patient_service.find_patient("P1"),
        practitioner_service.find_practitioner("D1"),
        datetime(2026, 11, 5, 11, 0),
        AppointmentStatus.COMPLETED
    )

    data_store.add_appointment(completed_appointment)

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment("A2")

    assert completed_appointment.status is AppointmentStatus.COMPLETED

# T-23: INVALID APPOINTMENT CANCELLATION ID

# Check that unknown IDs raise LookupError and blank IDs raise ValueError
def test_cancel_appointment_rejects_unknown_and_blank_ids():
    data_store, _, _, appointment_service = create_test_services()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    with pytest.raises(LookupError):
        appointment_service.cancel_appointment("A99")

    appointment_ids: list = [
        "",
        " "
    ]

    for appointment_id in appointment_ids:
        with pytest.raises(ValueError):
            appointment_service.cancel_appointment(appointment_id)

    # Check that rejected cancellation attempts changed nothing
    assert data_store.list_appointments() == [appointment]
    assert appointment.status is AppointmentStatus.SCHEDULED

# T-24: APPOINTMENT LOOKUP

# Check that looking up a known appointment returns the same object
def test_find_appointment_returns_same_object():
    _, _, _, appointment_service = create_test_services()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    found_appointment = appointment_service.find_appointment("A1")

    assert found_appointment is appointment

# STAGE 9: PRACTITIONER APPOINTMENT LISTING

# Check that only appointments for the requested practitioner are returned
def test_list_practitioner_appointments_isolates_practitioners():
    data_store, _, practitioner_service, appointment_service = (
        create_test_services()
    )

    practitioner_service.register_practitioner(
        "D2",
        "Dr. Jones",
        "Specialty"
    )

    appointment_d1 = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    appointment_d2 = appointment_service.book_appointment(
        "A2",
        "P1",
        "D2",
        datetime(2026, 11, 5, 11, 0)
    )

    results = appointment_service.list_practitioner_appointments("D1")

    assert results == [appointment_d1]
    assert appointment_d2 not in results
    assert results[0] is appointment_d1

# Check that all statuses are returned by default and can be filtered
def test_list_practitioner_appointments_filters_statuses():
    data_store, patient_service, practitioner_service, appointment_service = (
        create_test_services()
    )

    scheduled = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    cancelled = appointment_service.book_appointment(
        "A2",
        "P1",
        "D1",
        datetime(2026, 11, 5, 11, 0)
    )
    appointment_service.cancel_appointment("A2")

    completed = Appointment(
        "A3",
        patient_service.find_patient("P1"),
        practitioner_service.find_practitioner("D1"),
        datetime(2026, 11, 5, 12, 0),
        AppointmentStatus.COMPLETED
    )
    data_store.add_appointment(completed)

    # No status supplied should return every appointment
    results = appointment_service.list_practitioner_appointments("D1")

    assert results == [scheduled, cancelled, completed]

    # Each status should return only matching appointments
    expected_results = {
        AppointmentStatus.SCHEDULED: [scheduled],
        AppointmentStatus.CANCELLED: [cancelled],
        AppointmentStatus.COMPLETED: [completed],
    }

    for status in AppointmentStatus:
        results = appointment_service.list_practitioner_appointments(
            "D1",
            status
        )

        assert results == expected_results[status]

# Check that invalid practitioner IDs and status values are rejected
def test_list_practitioner_appointments_rejects_invalid_inputs():
    _, _, _, appointment_service = create_test_services()

    with pytest.raises(LookupError):
        appointment_service.list_practitioner_appointments("D99")

    practitioner_ids = ["", " "]

    for practitioner_id in practitioner_ids:
        with pytest.raises(ValueError):
            appointment_service.list_practitioner_appointments(
                practitioner_id
            )

    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments(
            "D1",
            "scheduled"
        )

# Check that a known practitioner with no appointments returns an empty list
def test_list_practitioner_appointments_returns_empty_list():
    _, _, practitioner_service, appointment_service = (
        create_test_services()
    )

    practitioner_service.register_practitioner(
        "D2",
        "Dr. Jones",
        "Specialty"
    )

    results = appointment_service.list_practitioner_appointments("D2")

    assert results == []

# Check that listing returns a new list without replacing appointment objects
def test_list_practitioner_appointments_preserves_appointment_objects():
    _, _, _, appointment_service = create_test_services()

    appointment = appointment_service.book_appointment(
        "A1",
        "P1",
        "D1",
        datetime(2026, 11, 5, 10, 0)
    )

    appointment_service.cancel_appointment("A1")

    first_results = appointment_service.list_practitioner_appointments("D1")
    second_results = appointment_service.list_practitioner_appointments("D1")

    assert first_results is not second_results
    assert first_results[0] is appointment
    assert second_results[0] is appointment
    assert appointment.status is AppointmentStatus.CANCELLED