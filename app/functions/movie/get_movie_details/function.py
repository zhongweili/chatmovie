from gptool.types.function import Function
from functions.movie.get_movie_details.types import (
    FunctionInput,
    FunctionOutput,
    MovieDetails,
)
from tmdbv3api import Movie

movie = Movie()


def get_movie_details(params: FunctionInput) -> FunctionOutput:
    movie_data = movie.details(params.movie_id)

    details = MovieDetails(
        title=movie_data["title"],
        overview=movie_data["overview"],
        popularity=movie_data["popularity"],
    )

    return FunctionOutput(details=details)


function = Function(
    function=get_movie_details,
    description="Get the primary information about a movie.",
)
