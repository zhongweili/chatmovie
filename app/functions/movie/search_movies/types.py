from pydantic import BaseModel, Field


class FunctionInput(BaseModel):
    title: str = Field(..., description="The title of the movie to search for.")
    limit: int = None


class MovieSearchResult(BaseModel):
    id: int
    title: str
    overview: str
    poster_path: str
    release_date: str

    def __eq__(self, other):
        if not isinstance(other, MovieSearchResult):
            return False
        return (
            self.id == other.id
            and self.title == other.title
            and self.overview == other.overview
            and self.poster_path == other.poster_path
            and self.release_date == other.release_date
        )


class FunctionOutput(BaseModel):
    search_results: list[MovieSearchResult]
