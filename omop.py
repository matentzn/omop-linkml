# Auto generated from omop.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-06-01T12:55:19
# Schema: omop-linkml
#
# id: https://w3id.org/omop-linkml
# description: omop
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OMOP_LINKML = CurieNamespace('omop-linkml', 'https://w3id.org/omop-linkml')
DEFAULT_ = OMOP-LINKML


# Types

# Class references



@dataclass
class PersonList(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP-LINKML.PersonList
    class_class_curie: ClassVar[str] = "omop-linkml:PersonList"
    class_name: ClassVar[str] = "person_list"
    class_model_uri: ClassVar[URIRef] = OMOP-LINKML.PersonList

    persons: Optional[Union[Union[dict, "Person"], List[Union[dict, "Person"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.persons, list):
            self.persons = [self.persons] if self.persons is not None else []
        self.persons = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.persons]

        super().__post_init__(**kwargs)


@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OMOP-LINKML.Person
    class_class_curie: ClassVar[str] = "omop-linkml:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = OMOP-LINKML.Person

    person_id: Optional[int] = None
    gender_concept_id: Optional[int] = None
    year_of_birth: Optional[int] = None
    month_of_birth: Optional[int] = None
    day_of_birth: Optional[int] = None
    birth_datetime: Optional[str] = None
    race_concept_id: Optional[int] = None
    ethnicity_concept_id: Optional[int] = None
    location_id: Optional[str] = None
    provider_id: Optional[str] = None
    care_site_id: Optional[int] = None
    person_source_value: Optional[int] = None
    gender_source_value: Optional[Union[str, "GenderSourceValueEnum"]] = None
    gender_source_concept_id: Optional[int] = None
    race_source_value: Optional[str] = None
    race_source_concept_id: Optional[int] = None
    ethnicity_source_value: Optional[Union[str, "EthnicitySourceValueEnum"]] = None
    ethnicity_source_concept_id: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.person_id is not None and not isinstance(self.person_id, int):
            self.person_id = int(self.person_id)

        if self.gender_concept_id is not None and not isinstance(self.gender_concept_id, int):
            self.gender_concept_id = int(self.gender_concept_id)

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, int):
            self.year_of_birth = int(self.year_of_birth)

        if self.month_of_birth is not None and not isinstance(self.month_of_birth, int):
            self.month_of_birth = int(self.month_of_birth)

        if self.day_of_birth is not None and not isinstance(self.day_of_birth, int):
            self.day_of_birth = int(self.day_of_birth)

        if self.birth_datetime is not None and not isinstance(self.birth_datetime, str):
            self.birth_datetime = str(self.birth_datetime)

        if self.race_concept_id is not None and not isinstance(self.race_concept_id, int):
            self.race_concept_id = int(self.race_concept_id)

        if self.ethnicity_concept_id is not None and not isinstance(self.ethnicity_concept_id, int):
            self.ethnicity_concept_id = int(self.ethnicity_concept_id)

        if self.location_id is not None and not isinstance(self.location_id, str):
            self.location_id = str(self.location_id)

        if self.provider_id is not None and not isinstance(self.provider_id, str):
            self.provider_id = str(self.provider_id)

        if self.care_site_id is not None and not isinstance(self.care_site_id, int):
            self.care_site_id = int(self.care_site_id)

        if self.person_source_value is not None and not isinstance(self.person_source_value, int):
            self.person_source_value = int(self.person_source_value)

        if self.gender_source_value is not None and not isinstance(self.gender_source_value, GenderSourceValueEnum):
            self.gender_source_value = GenderSourceValueEnum(self.gender_source_value)

        if self.gender_source_concept_id is not None and not isinstance(self.gender_source_concept_id, int):
            self.gender_source_concept_id = int(self.gender_source_concept_id)

        if self.race_source_value is not None and not isinstance(self.race_source_value, str):
            self.race_source_value = str(self.race_source_value)

        if self.race_source_concept_id is not None and not isinstance(self.race_source_concept_id, int):
            self.race_source_concept_id = int(self.race_source_concept_id)

        if self.ethnicity_source_value is not None and not isinstance(self.ethnicity_source_value, EthnicitySourceValueEnum):
            self.ethnicity_source_value = EthnicitySourceValueEnum(self.ethnicity_source_value)

        if self.ethnicity_source_concept_id is not None and not isinstance(self.ethnicity_source_concept_id, int):
            self.ethnicity_source_concept_id = int(self.ethnicity_source_concept_id)

        super().__post_init__(**kwargs)


# Enumerations
class GenderSourceValueEnum(EnumDefinitionImpl):

    F = PermissibleValue(text="F",
                         description="F")
    M = PermissibleValue(text="M",
                         description="M")

    _defn = EnumDefinition(
        name="GenderSourceValueEnum",
    )

class EthnicitySourceValueEnum(EnumDefinitionImpl):

    UNKNOWN = PermissibleValue(text="UNKNOWN",
                                     description="UNKNOWN")

    _defn = EnumDefinition(
        name="EthnicitySourceValueEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "NOT HISPANIC OR LATINO",
                PermissibleValue(text="NOT HISPANIC OR LATINO",
                                 description="NOT HISPANIC OR LATINO") )
        setattr(cls, "HISPANIC OR LATINO",
                PermissibleValue(text="HISPANIC OR LATINO",
                                 description="HISPANIC OR LATINO") )

# Slots
class slots:
    pass

slots.persons = Slot(uri=OMOP-LINKML.persons, name="persons", curie=OMOP-LINKML.curie('persons'),
                   model_uri=OMOP-LINKML.persons, domain=None, range=Optional[Union[Union[dict, Person], List[Union[dict, Person]]]])

slots.person_id = Slot(uri=OMOP-LINKML.person_id, name="person_id", curie=OMOP-LINKML.curie('person_id'),
                   model_uri=OMOP-LINKML.person_id, domain=None, range=Optional[int])

slots.gender_concept_id = Slot(uri=OMOP-LINKML.gender_concept_id, name="gender_concept_id", curie=OMOP-LINKML.curie('gender_concept_id'),
                   model_uri=OMOP-LINKML.gender_concept_id, domain=None, range=Optional[int])

slots.year_of_birth = Slot(uri=OMOP-LINKML.year_of_birth, name="year_of_birth", curie=OMOP-LINKML.curie('year_of_birth'),
                   model_uri=OMOP-LINKML.year_of_birth, domain=None, range=Optional[int])

slots.month_of_birth = Slot(uri=OMOP-LINKML.month_of_birth, name="month_of_birth", curie=OMOP-LINKML.curie('month_of_birth'),
                   model_uri=OMOP-LINKML.month_of_birth, domain=None, range=Optional[int])

slots.day_of_birth = Slot(uri=OMOP-LINKML.day_of_birth, name="day_of_birth", curie=OMOP-LINKML.curie('day_of_birth'),
                   model_uri=OMOP-LINKML.day_of_birth, domain=None, range=Optional[int])

slots.birth_datetime = Slot(uri=OMOP-LINKML.birth_datetime, name="birth_datetime", curie=OMOP-LINKML.curie('birth_datetime'),
                   model_uri=OMOP-LINKML.birth_datetime, domain=None, range=Optional[str])

slots.race_concept_id = Slot(uri=OMOP-LINKML.race_concept_id, name="race_concept_id", curie=OMOP-LINKML.curie('race_concept_id'),
                   model_uri=OMOP-LINKML.race_concept_id, domain=None, range=Optional[int])

slots.ethnicity_concept_id = Slot(uri=OMOP-LINKML.ethnicity_concept_id, name="ethnicity_concept_id", curie=OMOP-LINKML.curie('ethnicity_concept_id'),
                   model_uri=OMOP-LINKML.ethnicity_concept_id, domain=None, range=Optional[int])

slots.location_id = Slot(uri=OMOP-LINKML.location_id, name="location_id", curie=OMOP-LINKML.curie('location_id'),
                   model_uri=OMOP-LINKML.location_id, domain=None, range=Optional[str])

slots.provider_id = Slot(uri=OMOP-LINKML.provider_id, name="provider_id", curie=OMOP-LINKML.curie('provider_id'),
                   model_uri=OMOP-LINKML.provider_id, domain=None, range=Optional[str])

slots.care_site_id = Slot(uri=OMOP-LINKML.care_site_id, name="care_site_id", curie=OMOP-LINKML.curie('care_site_id'),
                   model_uri=OMOP-LINKML.care_site_id, domain=None, range=Optional[int])

slots.person_source_value = Slot(uri=OMOP-LINKML.person_source_value, name="person_source_value", curie=OMOP-LINKML.curie('person_source_value'),
                   model_uri=OMOP-LINKML.person_source_value, domain=None, range=Optional[int])

slots.gender_source_value = Slot(uri=OMOP-LINKML.gender_source_value, name="gender_source_value", curie=OMOP-LINKML.curie('gender_source_value'),
                   model_uri=OMOP-LINKML.gender_source_value, domain=None, range=Optional[Union[str, "GenderSourceValueEnum"]])

slots.gender_source_concept_id = Slot(uri=OMOP-LINKML.gender_source_concept_id, name="gender_source_concept_id", curie=OMOP-LINKML.curie('gender_source_concept_id'),
                   model_uri=OMOP-LINKML.gender_source_concept_id, domain=None, range=Optional[int])

slots.race_source_value = Slot(uri=OMOP-LINKML.race_source_value, name="race_source_value", curie=OMOP-LINKML.curie('race_source_value'),
                   model_uri=OMOP-LINKML.race_source_value, domain=None, range=Optional[str])

slots.race_source_concept_id = Slot(uri=OMOP-LINKML.race_source_concept_id, name="race_source_concept_id", curie=OMOP-LINKML.curie('race_source_concept_id'),
                   model_uri=OMOP-LINKML.race_source_concept_id, domain=None, range=Optional[int])

slots.ethnicity_source_value = Slot(uri=OMOP-LINKML.ethnicity_source_value, name="ethnicity_source_value", curie=OMOP-LINKML.curie('ethnicity_source_value'),
                   model_uri=OMOP-LINKML.ethnicity_source_value, domain=None, range=Optional[Union[str, "EthnicitySourceValueEnum"]])

slots.ethnicity_source_concept_id = Slot(uri=OMOP-LINKML.ethnicity_source_concept_id, name="ethnicity_source_concept_id", curie=OMOP-LINKML.curie('ethnicity_source_concept_id'),
                   model_uri=OMOP-LINKML.ethnicity_source_concept_id, domain=None, range=Optional[int])