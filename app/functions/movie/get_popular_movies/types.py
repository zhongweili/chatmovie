from pydantic import BaseModel, Field
from typing import Optional


class FunctionInput(BaseModel):
    limit: Optional[int] = Field(..., description="The limit number of popular movies.")


class MovieInfo(BaseModel):
    id: int
    title: str
    overview: str
    poster_path: str

    def __eq__(self, other):
        if not isinstance(other, MovieInfo):
            return False
        return (
            self.id == other.id
            and self.title == other.title
            and self.overview == other.overview
            and self.poster_path == other.poster_path
        )


class FunctionOutput(BaseModel):
    popular: list[MovieInfo]
