"""Stage 8 regression tests for the two prepared defects.

F8-01: practitioner conflict detection (FR-05, AC-04.1, AC-04.2).
F8-02: cancelled appointments must stay retrievable (FR-07, AC-05.2;
FR-08, AC-06.1).
"""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

SLOT = datetime(2026, 11, 5, 10, 0)


def create_services():
    """Return a fresh store and services with synthetic participants."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient('P1', 'Alex Example')
    patient_service.register_patient('P2', 'Sam Example')
    practitioner_service.register_practitioner(
        'D1', 'Taylor Example', 'General practice'
    )
    practitioner_service.register_practitioner(
        'D2', 'Jordan Example', 'Physio'
    )
    return data_store, appointment_service


def test_f8_01_same_practitioner_same_time_is_rejected():
    """F8-01: a second SCHEDULED booking for the same practitioner at
    the exact same time is rejected and changes nothing, while a
    different practitioner at that time is still allowed."""
    data_store, appointment_service = create_services()
    first = appointment_service.book_appointment('A1', 'P1', 'D1', SLOT)

    with pytest.raises(ValueError):
        appointment_service.book_appointment('A2', 'P2', 'D1', SLOT)

    assert data_store.list_appointments() == [first]
    assert data_store.find_appointment('A2') is None
    assert first.status is AppointmentStatus.SCHEDULED

    other = appointment_service.book_appointment('A3', 'P2', 'D2', SLOT)
    assert data_store.list_appointments() == [first, other]


def test_f8_02_cancelled_appointment_is_still_found():
    """F8-02: after cancellation the same object stays in the store,
    is found by ID through the store and the service, and a repeated
    cancellation is still rejected without changing it."""
    data_store, appointment_service = create_services()
    appointment = appointment_service.book_appointment(
        'A1', 'P1', 'D1', SLOT
    )

    appointment_service.cancel_appointment('A1')

    assert data_store.list_appointments() == [appointment]
    assert data_store.find_appointment('A1') is appointment
    assert appointment_service.find_appointment('A1') is appointment
    assert appointment.status is AppointmentStatus.CANCELLED

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A1')
    assert appointment.status is AppointmentStatus.CANCELLED
    assert data_store.list_appointments() == [appointment]