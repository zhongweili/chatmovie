from pydantic import BaseModel, Field

class FunctionInput(BaseModel):
    movie_id: int = Field(..., description="The ID of the movie.")


class SimilarMovie(BaseModel):
    title: str
    overview: str

    def __eq__(self, other):
        if not isinstance(other, SimilarMovie):
            return False
        return self.title == other.title and self.overview == other.overview


class FunctionOutput(BaseModel):
    similar_movies: list[SimilarMovie]
