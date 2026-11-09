"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')
    
MENU_TEXT = """
SmartCare menu
1  Register patient
2  Find patient
3  Register practitioner
4  Find practitioner
5  Book appointment
6  Cancel appointment
7  Find appointment
8  List a practitioner's appointments
0  Exit"""


def parse_status(text: str) -> AppointmentStatus | None:
    """Convert console text to a status; blank means every status."""
    cleaned = text.strip().lower()
    if not cleaned:
        return None
    for status in AppointmentStatus:
        if status.value == cleaned:
            return status
    raise ValueError('Status must be scheduled, cancelled or completed')

def register_patient_command(patients: PatientService) -> None:
    patient_id = input('Patient ID: ')
    name = input('Patient name: ')
    patient = patients.register_patient(patient_id, name)
    print(f'Registered patient {patient.patient_id}: {patient.name}')


def find_patient_command(patients: PatientService) -> None:
    patient = patients.find_patient(input('Patient ID: '))
    print(f'Patient {patient.patient_id}: {patient.name}')


def register_practitioner_command(practitioners: PractitionerService) -> None:
    practitioner_id = input('Practitioner ID: ')
    name = input('Practitioner name: ')
    specialty = input('Specialty: ')
    practitioner = practitioners.register_practitioner(
        practitioner_id, name, specialty,
    )
    print(
        f'Registered practitioner {practitioner.practitioner_id}: '
        f'{practitioner.name} ({practitioner.specialty})'
    )

def find_practitioner_command(practitioners: PractitionerService) -> None:
    practitioner = practitioners.find_practitioner(input('Practitioner ID: '))
    print(
        f'Practitioner {practitioner.practitioner_id}: '
        f'{practitioner.name} ({practitioner.specialty})'
    )

def book_appointment_command(appointments: AppointmentService) -> None:
    appointment_id = input('Appointment ID: ')
    patient_id = input('Patient ID: ')
    practitioner_id = input('Practitioner ID: ')
    date_time = parse_date_time(input('Date/time (YYYY-MM-DD HH:MM): '))
    appointment = appointments.book_appointment(
        appointment_id, patient_id, practitioner_id, date_time,
    )
    print(f'Booked {format_appointment(appointment)}')


def cancel_appointment_command(appointments: AppointmentService) -> None:
    appointment = appointments.cancel_appointment(input('Appointment ID: '))
    print(f'Cancelled {format_appointment(appointment)}')


def find_appointment_command(appointments: AppointmentService) -> None:
    appointment = appointments.find_appointment(input('Appointment ID: '))
    print(format_appointment(appointment))

def list_appointments_command(appointments: AppointmentService) -> None:
    practitioner_id = input('Practitioner ID: ')
    status = parse_status(
        input('Status (scheduled/cancelled/completed, blank for all): '),
    )
    found = appointments.list_practitioner_appointments(
        practitioner_id, status,
    )
    if not found:
        print('No matching appointments.')
    for appointment in found:
        print(format_appointment(appointment))

def run_menu() -> None:
    """Stage 9: implement the register/find/book/cancel/list/exit menu.

    Call services, recover from expected input errors, and keep this
    session's data until exit. main.py reports the incomplete menu
    without crashing.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    try:
        while True:
            print(MENU_TEXT)
            choice = input('Choose an option: ').strip()
            if choice == '0':
                print('Goodbye. Session data is discarded.')
                return
            try:
                if choice == '1':
                    register_patient_command(patients)
                elif choice == '2':
                    find_patient_command(patients)
                elif choice == '3':
                    register_practitioner_command(practitioners)
                elif choice == '4':
                    find_practitioner_command(practitioners)
                elif choice == '5':
                    book_appointment_command(appointments)
                elif choice == '6':
                    cancel_appointment_command(appointments)
                elif choice == '7':
                    find_appointment_command(appointments)
                elif choice == '8':
                    list_appointments_command(appointments)
                else:
                    print('Unknown choice. Enter a number from the menu.')
            except (ValueError, LookupError) as error:
                print(f'Error: {error}')
    except EOFError:
        print('\nInput ended. Session data is discarded.')