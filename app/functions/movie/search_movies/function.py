from gptool.types.function import Function
from functions.movie.search_movies.types import (
    FunctionInput,
    FunctionOutput,
    MovieSearchResult,
)
from tmdbv3api import Movie

movie = Movie()


def search_movies(params: FunctionInput) -> FunctionOutput:
    movies_data = movie.search(params.title)
    if params.limit >= 3:
        params.limit = 3

    search_results = [
        MovieSearchResult(
            id=movie["id"],
            title=movie["title"],
            overview=movie["overview"],
            poster_path="http://image.tmdb.org/t/p/w500" + movie["poster_path"]
            if movie["poster_path"] is not None
            else "",
            release_date=movie["release_date"],
        )
        for movie in movies_data
    ]

    return FunctionOutput(search_results=search_results[: params.limit])


function = Function(
    function=search_movies,
    description="Search for movies by title.",
)
