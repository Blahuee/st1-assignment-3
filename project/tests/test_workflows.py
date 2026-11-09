from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def test_complete_appointment_workflow():
    # Create one shared data store and services
    store = SmartCareDataStore()
    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    appointment_time = datetime(2026, 10, 1, 9, 0)

    # Register one patient and two practitioners
    patient = patients.register_patient("P1", "Test Patient")
    practitioner1 = practitioners.register_practitioner(
        "D1", "Doctor One", "General Practice"
    )
    practitioner2 = practitioners.register_practitioner(
        "D2", "Doctor Two", "Cardiology"
    )

    # Verify patient and practitioner lookups
    assert patients.find_patient("P1") is patient
    assert practitioners.find_practitioner("D1") is practitioner1
    assert practitioners.find_practitioner("D2") is practitioner2

    # Book the first appointment
    first = appointments.book_appointment(
        "A1", "P1", "D1", appointment_time
    )

    assert appointments.find_appointment("A1") is first

    # Reject another booking with the same practitioner and time
    before_conflict = store.list_appointments()

    with pytest.raises(ValueError):
        appointments.book_appointment(
            "A2", "P1", "D1", appointment_time
        )

    assert store.list_appointments() == before_conflict

    # The same patient can book another practitioner at the same time
    second = appointments.book_appointment(
        "A2", "P1", "D2", appointment_time
    )

    assert appointments.find_appointment("A2") is second

    # Cancel the first appointment; its history is retained
    cancelled = appointments.cancel_appointment("A1")

    assert cancelled is first
    assert first.status is AppointmentStatus.CANCELLED
    assert appointments.find_appointment("A1") is first

    # A second cancellation must be rejected without changing state
    with pytest.raises(ValueError):
        appointments.cancel_appointment("A1")

    assert first.status is AppointmentStatus.CANCELLED

    # The cancelled appointment frees D1's original time slot
    third = appointments.book_appointment(
        "A3", "P1", "D1", appointment_time
    )

    assert appointments.find_appointment("A3") is third

    # Listing all appointments for D1 includes cancellation history
    all_d1 = appointments.list_practitioner_appointments("D1")

    assert [item.appointment_id for item in all_d1] == ["A1", "A3"]
    assert all_d1[0].status is AppointmentStatus.CANCELLED
    assert all_d1[1].status is AppointmentStatus.SCHEDULED

    # Filtering to scheduled appointments excludes cancelled history
    scheduled_d1 = appointments.list_practitioner_appointments(
        "D1", AppointmentStatus.SCHEDULED
    )

    assert [item.appointment_id for item in scheduled_d1] == ["A3"]

    # Unknown practitioner should raise LookupError
    with pytest.raises(LookupError):
        appointments.list_practitioner_appointments("UNKNOWN")

    # Unknown appointment should raise LookupError
    with pytest.raises(LookupError):
        appointments.find_appointment("UNKNOWN")