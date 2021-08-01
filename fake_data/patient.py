from . import fake


def personal_id() -> dict:
    return {
        "employment": {
            "employer": fake.company(),
            "occupation": fake.job(),
        },
        "name": {
            "given": fake.first_name(),
            "middle": fake.first_name(),
            "surname": fake.last_name(),
        },
        "tax_id_number": fake.ssn(),
    }


def address() -> dict:
    return {
        "street": fake.street_address(),
        "city": fake.city(),
        "postal_code": fake.postcode(),
        "country_code": "US",
    }


def fake_patient() -> dict:
    is_minor = fake.boolean(chance_of_getting_true=20)
    patient = {
        "id": fake.uuid4(),
        "address": address(),
        "blood_type": {
            "group": fake.random.choice(["A", "AB", "B", "O"]),
            "rh_factor": fake.random.choice(["+", "-", "null"]),
        },
        "physique": {
            "height_in_centimeters": fake.pyfloat(
                left_digits=3,
                right_digits=2,
                positive=True,
                min_value=159,
                max_value=177,
            ),
            "weight_in_kilograms": fake.pyfloat(
                left_digits=3,
                right_digits=1,
                positive=True,
                min_value=62,
                max_value=105,
            ),
        },
        "preferred_pharmacy": {
            "name": fake.random.choice(
                [
                    "CVS Health",
                    "Walgreens",
                    "Cigna",
                    "UnitedHealth Group",
                    "WalMart",
                    "Kroger",
                    "Rite Aid",
                ]
            ),
            "address": address(),
        },
        "sex": fake.random.choice(["Female", "Male"]),
    }

    patient.update(personal_id())

    if is_minor:
        patient["birth_date"] = fake.date_between(
            start_date="-18y", end_date="today"
        ).isoformat()
        patient["employment"]["employer"] = None
        patient["employment"]["occupation"] = "Student"
        patient["guardian"] = personal_id()
        patient["guardian"]["address"] = patient["address"]
    else:
        patient["birth_date"] = fake.date_between(
            start_date="-102y", end_date="-19y"
        ).isoformat()

    return patient
