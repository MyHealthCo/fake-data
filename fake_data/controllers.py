from .patient import fake_patient


def patients(number_of_records: int) -> list:
    patients = []
    for _ in range(number_of_records):
        patients.append(fake_patient())

    return patients
