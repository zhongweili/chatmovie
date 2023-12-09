from pydantic import BaseModel, Field
from functions.movie.search_movies.types import MovieSearchResult


class FunctionInput(BaseModel):
    query: str = Field(..., description="The name of the person to search for.")


class PersonSearchResult(BaseModel):
    id: int
    name: str
    known_for_department: str
    known_for_movies: list[MovieSearchResult]

    def __eq__(self, other):
        if not isinstance(other, PersonSearchResult):
            return False
        return (
            self.id == other.id
            and self.name == other.name
            and self.known_for_department == other.known_for_department
        )


class FunctionOutput(BaseModel):
    search_results: list[PersonSearchResult]
