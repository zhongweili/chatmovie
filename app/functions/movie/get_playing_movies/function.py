from gptool.types.function import Function
from functions.movie.get_playing_movies.types import (
    FunctionInput,
    FunctionOutput,
    MovieInfo,
)
from tmdbv3api import Movie

movie = Movie()


def get_playing_movies(params: FunctionInput) -> FunctionOutput:
    movies_data = movie.now_playing(region="CN")
    playing_movies = [
        MovieInfo(
            id=movie["id"],
            title=movie["title"],
            overview=movie["overview"],
            poster_path="http://image.tmdb.org/t/p/w500" + movie["poster_path"]
            if movie["poster_path"] is not None
            else "",
            release_date=movie["release_date"],
        )
        for movie in movies_data["results"]
    ]
    return FunctionOutput(playing=playing_movies[: params.limit])


function = Function(
    function=get_playing_movies,
    description="Get a list of movies that are playing in theatres.",
)
