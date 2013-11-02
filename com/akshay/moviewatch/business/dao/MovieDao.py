from com.akshay.moviewatch.business.dao.Dao import session
from com.akshay.moviewatch.domain.Movie import Movie
from com.akshay.moviewatch.domain.UserStatus import UserStatus

__author__ = 'akshay'


class MovieDao:
    def saveMovie(self, movie):
        session.add(movie)
        session.commit()

    def findForUser(self, user_id):
        return session.query(Movie).filter(Movie.listeningUsers.any(user_id=user_id)).all()

    def findById(self, id):
        return session.query(Movie).filter(Movie.id == id).one()

    def findByIMDBId(self, imdbId):
        return session.query(Movie).filter(Movie.imdbId == imdbId).all()

    def findByStatus(self, status):
        return session.query(Movie).filter(Movie.status == status).all()

    def setStatusForUser(self, movie_id, user_id, userStatus):
        movie = session.query(Movie).filter(Movie.id == movie_id).first()
        for listeningUser in movie.listeningUsers:
            if listeningUser.user_id == user_id:
                listeningUser.status = userStatus
        self.saveMovie(movie)
        print movie.listeningUsers

    def setStatus(self, movie, status):
        movie.status = status
        self.saveMovie(movie)

    def findNonArchivedForUser(self, userId):
        return session.query(Movie).filter(Movie.listeningUsers.any(user_id=userId)).\
            filter(~Movie.listeningUsers.any(status=UserStatus.ARCHIVED)).all()
