from sqlalchemy import Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.orm import relationship
from com.akshay.moviewatch.business.dao.Dao import Base
from com.akshay.moviewatch.domain.Status import Status

__author__ = 'akshay'


class UserMovie(Base):
    __tablename__ = 'UserMovies'
    movie_id = Column(Integer, ForeignKey('Movie.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    status = Column(String(50))
    usersBackref = relationship("User", backref="listeningMovies")

    def __repr__(self):
        return "<UserMovie('%s','%s','%s')>" % (self.movie_id, self.user_id, self.status)


class Movie(Base):
    __tablename__ = 'Movie'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    title = Column(String(50))
    year = Column(String(4))
    imdbId = Column(String(50))
    status = Column(String(20), default=str(Status.PRE_RELEASE))
    metaData = []

    listeningUsers = relationship("UserMovie", backref="listeningMovies")

    def __init__(self, title, imdbId, year=None):
        self.title = title
        self.year = year
        self.imdbId = imdbId

    def __repr__(self):
        return "<Movie('%s','%s')>" % (self.title, self.year)