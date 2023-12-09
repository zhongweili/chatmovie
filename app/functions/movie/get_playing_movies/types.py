from pydantic import BaseModel


class FunctionInput(BaseModel):
    limit: int = None


class MovieInfo(BaseModel):
    id: int
    title: str
    overview: str
    poster_path: str
    release_date: str

    def __eq__(self, other):
        if not isinstance(other, MovieInfo):
            return False
        return (
            self.id == other.id
            and self.title == other.title
            and self.overview == other.overview
            and self.poster_path == other.poster_path
            and self.release_date == other.release_date
        )


class FunctionOutput(BaseModel):
    playing: list[MovieInfo]
