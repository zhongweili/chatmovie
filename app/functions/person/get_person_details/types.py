from pydantic import BaseModel, Field

class FunctionInput(BaseModel):
    person_id: int = Field(..., description="The ID of the person.")


class PersonInfo(BaseModel):
    name: str
    biography: str

    def __eq__(self, other):
        if not isinstance(other, PersonInfo):
            return False
        return self.name == other.name and self.biography == other.biography


class FunctionOutput(BaseModel):
    person_details: PersonInfo
