from datetime import date
from enum import Enum
from typing import Optional
from uuid import UUID

import iso3166
from pydantic import BaseModel


class Model(BaseModel):
    use_enum_values = True
    allow_population_by_field_name = True


class Employment(Model):
    employer: str
    occupation: str


class HumanName(Model):
    given: str
    middle: Optional[str]
    surname: str


class Alpha3Country(str):
    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("Must be a string")
        if len(v) != 3:
            raise ValueError("Must be an 3 Character Country Code")
        if v not in iso3166.countries_by_alpha3.keys():
            raise ValueError("Must be a valid iso3166 3-Character Country Code")


class TaxId(Model):
    tax_id_value: str
    issuing_country: Alpha3Country


class Address(Model):
    street: str
    city: str
    postal_code: int
    country_code: Alpha3Country


class BloodGroup(str, Enum):
    A = "A"
    B = "B"
    O = "O"
    AB = "AB"


class BloodRhFactor(str, Enum):
    POSITIVE = "+"
    NEGATIVE = "-"
    NULL = "null"


class BloodType(Model):
    group: BloodGroup
    rh_factor: BloodRhFactor


class Physique(Model):
    height_in_centimeters: float
    weight_in_kilograms: float


class Pharmacy(Model):
    name: str
    address: Address


class Sex(str, Enum):
    FEMALE = "Female"
    MALE = "Male"


class Guardian(Model):
    address: Address
    birth_date: date
    employment: Employment
    name: HumanName
    tax_id: TaxId


class Patient(Model):
    address: Address
    birth_date: date
    blood_type: BloodType
    employment: Employment
    guardian: Optional[Guardian]
    id: UUID
    name: HumanName
    physique: Physique
    preferred_pharmacy: Pharmacy
    tax_id: TaxId
    sex: Sex
