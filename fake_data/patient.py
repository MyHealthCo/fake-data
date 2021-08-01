from . import fake


def personal_id() -> dict:
    return {
        "name": {
            "given": fake.first_name(),
            "middle": fake.first_name(),
            "surname": fake.last_name(),
        },
        "tax_id_number": fake.ssn(),
    }


def fake_patient() -> dict:
    is_minor = fake.boolean(chance_of_getting_true=20)
    patient = {
        "physique": {
            "height_in_centimeters": fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=159.5, max_value=176.5)
        }
    }

    patient.update(personal_id())

    if is_minor:
        patient["guardian"] = personal_id()

    return patient
