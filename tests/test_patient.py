from pydantic import ValidationError

from fake_data import patient
from fake_data.patient import fake_patient

from .models import Patient


def test_it_follows_the_schema() -> None:
    patient_to_test = fake_patient()

    try:
        validated_patient = Patient(**patient_to_test)
        assert validated_patient is not None
    except ValidationError as e:
        print(e.errors())
        raise e

    assert patient_to_test is not None
