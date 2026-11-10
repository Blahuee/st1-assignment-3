from datetime import datetime

from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.queries import (
    appointment_sort_key,
    select_appointments,
)

# TEST DATA SETUP

def create_test_appointments():
    patient = Patient("P1", "Test Patient")

    practitioner1 = Practitioner(
        "D1",
        "Dr Smith",
        "General Practice"
    )

    practitioner2 = Practitioner(
        "D2",
        "Dr Jones",
        "Cardiology"
    )

    appointments = [
        Appointment(
            "A3",
            patient,
            practitioner1,
            datetime(2026, 11, 5, 11, 0),
        ),
        Appointment(
            "A1",
            patient,
            practitioner1,
            datetime(2026, 11, 5, 10, 0),
        ),
        Appointment(
            "A2",
            patient,
            practitioner2,
            datetime(2026, 11, 5, 9, 0),
        ),
        Appointment(
            "A4",
            patient,
            practitioner1,
            datetime(2026, 11, 5, 10, 0),
            AppointmentStatus.CANCELLED,
        ),
        Appointment(
            "A5",
            patient,
            practitioner1,
            datetime(2026, 11, 5, 12, 0),
            AppointmentStatus.COMPLETED,
        ),
    ]

    return appointments

# QRY-01: PRACTITIONER ISOLATION

def test_select_appointments_only_returns_requested_practitioner():
    appointments = create_test_appointments()

    results = select_appointments(appointments, "D1")

    assert len(results) == 4

    for appointment in results:
        assert appointment.practitioner.practitioner_id == "D1"

# QRY-02: APPOINTMENT STATUS FILTERING

def test_select_appointments_returns_all_statuses_by_default():
    appointments = create_test_appointments()

    results = select_appointments(appointments, "D1")

    statuses = [appointment.status for appointment in results]

    assert AppointmentStatus.SCHEDULED in statuses
    assert AppointmentStatus.CANCELLED in statuses
    assert AppointmentStatus.COMPLETED in statuses

def test_select_appointments_filters_each_status():
    appointments = create_test_appointments()

    expected_counts = {
        AppointmentStatus.SCHEDULED: 2,
        AppointmentStatus.CANCELLED: 1,
        AppointmentStatus.COMPLETED: 1,
    }

    for status in AppointmentStatus:
        results = select_appointments(
            appointments,
            "D1",
            status
        )

        assert len(results) == expected_counts[status]

        for appointment in results:
            assert appointment.status is status

# QRY-03: APPOINTMENT SORTING

def test_select_appointments_sorts_by_datetime_then_appointment_id():
    appointments = create_test_appointments()

    results = select_appointments(appointments, "D1")

    appointment_ids = [
        appointment.appointment_id
        for appointment in results
    ]

    assert appointment_ids == ["A1", "A4", "A3", "A5"]

# FP-01: REPEATED CALLS

def test_select_appointments_returns_consistent_results():
    appointments = create_test_appointments()

    first_results = select_appointments(appointments, "D1")
    second_results = select_appointments(appointments, "D1")

    assert first_results == second_results
    assert first_results is not second_results

# FP-02: SOURCE LIST AND OBJECTS ARE NOT MUTATED

def test_select_appointments_does_not_change_source_list_or_objects():
    appointments = create_test_appointments()

    original_order = appointments.copy()

    original_details = [
        (
            appointment.appointment_id,
            appointment.date_time,
            appointment.status,
            appointment.practitioner.practitioner_id,
        )
        for appointment in appointments
    ]

    results = select_appointments(appointments, "D1")

    assert appointments == original_order
    assert all(
        original is current
        for original, current in zip(appointments, original_order)
    )

    current_details = [
        (
            appointment.appointment_id,
            appointment.date_time,
            appointment.status,
            appointment.practitioner.practitioner_id,
        )
        for appointment in appointments
    ]

    assert current_details == original_details
    assert results is not appointments

# FP-03: NAMED SORTING KEY

def test_appointment_sort_key_returns_datetime_and_id():
    appointments = create_test_appointments()

    appointment = appointments[0]

    assert appointment_sort_key(appointment) == (
        appointment.date_time,
        appointment.appointment_id,
    )
    

# QRY-03: EQUAL-TIME TIE-BREAK BY APPOINTMENT ID

def test_select_appointments_breaks_equal_time_ties_by_appointment_id():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")
    same_time = datetime(2026, 11, 5, 10, 0)

    # A cancelled and a completed appointment share a time without
    # breaking the scheduled conflict rule. The higher ID comes first
    # in the source, so only the ID tie-break can put A1 first.
    later_id = Appointment(
        "A9", patient, practitioner, same_time, AppointmentStatus.COMPLETED
    )
    earlier_id = Appointment(
        "A1", patient, practitioner, same_time, AppointmentStatus.CANCELLED
    )
    source = [later_id, earlier_id]

    results = select_appointments(source, "D1")

    assert results == [earlier_id, later_id]
    assert source == [later_id, earlier_id]

# QRY-02: NO MATCHING STATUS GIVES A NEW EMPTY LIST

def test_select_appointments_returns_empty_list_when_no_status_matches():
    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")
    source = [
        Appointment("A1", patient, practitioner, datetime(2026, 11, 5, 10, 0))
    ]

    results = select_appointments(
        source, "D1", AppointmentStatus.CANCELLED
    )

    assert results == []
    assert results is not source
    assert source[0].status is AppointmentStatus.SCHEDULED

# FP-02: NEW LIST FOR EMPTY AND ALREADY-SORTED INPUTS

def test_select_appointments_returns_new_list_for_empty_and_sorted_input():
    empty_source = []
    empty_results = select_appointments(empty_source, "D1")

    assert empty_results == []
    assert empty_results is not empty_source

    patient = Patient("P1", "Test Patient")
    practitioner = Practitioner("D1", "Dr Smith", "General Practice")
    sorted_source = [
        Appointment("A1", patient, practitioner, datetime(2026, 11, 5, 9, 0)),
        Appointment("A2", patient, practitioner, datetime(2026, 11, 5, 10, 0)),
    ]

    sorted_results = select_appointments(sorted_source, "D1")

    assert sorted_results == sorted_source
    assert sorted_results is not sorted_source
    assert all(
        result is original
        for result, original in zip(sorted_results, sorted_source)
    )