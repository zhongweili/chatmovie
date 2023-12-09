from gptool.types.function import Function
from functions.person.search_people.types import (
    FunctionInput,
    FunctionOutput,
    PersonSearchResult,
)
from functions.movie.search_movies.types import MovieSearchResult
from tmdbv3api import Person

person = Person()


def search_people(params: FunctionInput) -> FunctionOutput:
    people_data = person.search(params.query)

    search_results = []
    for person_data in people_data:
        known_for_movies = [
            MovieSearchResult(
                id=movie["id"],
                title=movie["title"],
                overview=movie["overview"],
                poster_path="http://image.tmdb.org/t/p/w500" + movie["poster_path"]
                if movie["poster_path"] is not None
                else "",
                release_date=movie["release_date"],
            )
            for movie in person_data["known_for"]
        ]

        search_results.append(
            PersonSearchResult(
                id=person_data["id"],
                name=person_data["name"],
                known_for_department=person_data["known_for_department"],
                known_for_movies=known_for_movies,
            )
        )

    return FunctionOutput(search_results=search_results)


function = Function(
    function=search_people,
    description="Search for people by name.",
)
