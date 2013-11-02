from com.akshay.moviewatch.domain.MovieMin import MovieMin

__author__ = 'akshay'


def mapMovies(movies):
    mappedMovies = []
    for movie in movies:
        mappedMovie = MovieMin()
        mappedMovie.id = movie.id
        mappedMovie.imdbId = movie.imdbId
        mappedMovie.metaData = movie.metaData
        mappedMovie.status = movie.status
        mappedMovie.title = movie.title
        mappedMovie.year = movie.year
        mappedMovies.append(mappedMovie)
    return mappedMovies
