from gptool.types.function import Function
from functions.person.get_person_details.types import (
    FunctionInput,
    FunctionOutput,
    PersonInfo,
)
from tmdbv3api import Person

person = Person()


def get_person_details(params: FunctionInput) -> FunctionOutput:
    person_data = person.details(params.person_id)

    person_details = PersonInfo(
        name=person_data["name"],
        known_for_department=person_data["known_for_department"],
    )

    return FunctionOutput(person_details=person_details)


function = Function(
    function=get_person_details,
    description="Get the general person information for a specific id.",
)
