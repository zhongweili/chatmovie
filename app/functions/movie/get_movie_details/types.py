from pydantic import BaseModel, Field


class FunctionInput(BaseModel):
    movie_id: int = Field(..., description="The ID of the movie.")


class MovieDetails(BaseModel):
    title: str
    overview: str
    popularity: float

    def __eq__(self, other):
        if not isinstance(other, MovieDetails):
            return False
        return (
            self.title == other.title
            and self.overview == other.overview
            and self.popularity == other.popularity
        )


class FunctionOutput(BaseModel):
    details: MovieDetails
