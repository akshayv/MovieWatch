import random
import string
from com.akshay.moviewatch.business.dao.Dao import Base, engine
from com.akshay.moviewatch.business.dao.MovieDao import MovieDao
from com.akshay.moviewatch.business.dao.UserDao import UserDao
from com.akshay.moviewatch.business.service.MovieService import MovieService
from com.akshay.moviewatch.business.service.SessionService import SessionService
from com.akshay.moviewatch.business.service.UserService import UserService
from com.akshay.moviewatch.domain.Movie import UserMovie
from com.akshay.moviewatch.domain.UserStatus import UserStatus
from com.akshay.moviewatch.integration.IMDBIntegration import IMDBIntegration

__author__ = 'akshay'

movieDao = MovieDao()
userDao = UserDao()
userService = UserService()
movieService = MovieService()
sessionService = SessionService()
imdbIntegration = IMDBIntegration()
Base.metadata.create_all(engine)


def getIMDBSuggestionsForTitle(title):
    return imdbIntegration.getSuggestedTitles(title)


def registerMovie(movie_id, user_email_id):
    user = userDao.findByEmailId(user_email_id)
    movie = movieDao.findById(movie_id)
    userMovie = UserMovie()
    userMovie.status = UserStatus.WATCHING
    userMovie.usersBackref = user
    userMovie.movie_id = movie_id
    movie.listeningUsers.append(userMovie)
    movieDao.saveMovie(movie)


def saveMovie(movie_title, movie_year, movie_imdb_id):
    movieService.createMovie(movie_title, movie_year, movie_imdb_id)


def getRegisteredMovies(user_email_id):
    user = userDao.findByEmailId(user_email_id)
    return movieDao.findForUser(user.id)


def createUser(userName, password, emailId):
    registeredUser = userDao.findByEmailId(emailId)
    if registeredUser is not None:
        return False
    userService.createUser(userName, password, emailId)
    return sessionService.generateSessionId(emailId)


def getNonArchivedMoviesForUser(user_email_id):
    user = userDao.findByEmailId(user_email_id)
    return movieDao.findNonArchivedForUser(user.id)


def archiveMovieForUser(movieId, user_email_id):
    user = userDao.findByEmailId(user_email_id)
    movieDao.setStatusForUser(movieId, user.id, UserStatus.ARCHIVED)


def authenticate(user_email_id, session_id):
    return sessionService.authenticateUser(session_id, user_email_id)


def login(userEmail, password):
    authenticatedUser = userService.authenticate(userEmail, password)
    if authenticatedUser is not None:
        return sessionService.generateSessionId(userEmail)
    return False


if __name__ == "__main__":
    print ''.join(random.choice(string.ascii_uppercase) for x in range(8))
#     user = User('akshay', 'akshay.irock@gmail.com', 'h1oidna8')
#     print createUser(userDao, user)
#     movie = Movie('Pacific Rim', '2013')
#     saveMovie(movie)
#     print movieDao.findForUser(user.id)
#     print movie.listeningUsers
#     movieDao.setStatusForUser(movie.id, user, UserStatus.NOTIFIED)
#     print movie.listeningUsers
#     movieDao.setStatus(movie, Status.DVD_RELEASED)
#     print movieDao.getNonArchivedMoviesForUser(user)
#     print userDao.getByEmailIdAndPassword('akshay.irock@gmail.com', 'h1oidna8')
