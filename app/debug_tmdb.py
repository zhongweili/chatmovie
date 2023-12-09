# from tmdbv3api import TMDb, Movie

# tmdb = TMDb()

# movie = Movie()

# m = movie.details(111)

# print(m.title)
# print(m.overview)
# print(m.popularity)


from tmdbv3api import TMDb, Search

tmdb = TMDb()


search = Search()

results = search.movies("Matrix", year=1999)

for result in results:
    print(result.title)
    print(result.overview)
