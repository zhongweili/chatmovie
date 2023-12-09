from gptool.types.function import Function
from functions.movie.get_similar_movies.types import (
    FunctionInput,
    FunctionOutput,
    SimilarMovie,
)
from tmdbv3api import Movie

movie = Movie()


def get_similar_movies(params: FunctionInput) -> FunctionOutput:
    movies_data = movie.similar(params.movie_id)

    similar_movies = [
        SimilarMovie(title=movie["title"], overview=movie["overview"])
        for movie in movies_data
    ]

    return FunctionOutput(similar_movies=similar_movies)


function = Function(
    function=get_similar_movies,
    description="Get the similar movies for a specific movie id.",
)
