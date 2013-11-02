from com.akshay.moviewatch.business.dao.MovieDao import MovieDao
from com.akshay.moviewatch.domain.Movie import Movie

__author__ = 'akshay'


class MovieService:
    movieDao = MovieDao()

    def createMovie(self, movie_title, movie_year, movie_imdb_id):
        movie = Movie(movie_title, movie_year, movie_imdb_id)
        self.movieDao.saveMovie(movie)

