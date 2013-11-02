import md5
from sqlalchemy import Column, Integer, String, Sequence
from com.akshay.moviewatch.business.dao.Dao import Base

__author__ = 'akshay'


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    emailId = Column(String(50), unique=True)
    password = Column(String(50))

    def __init__(self, name, emailId, password):
        self.name = name
        self.emailId = emailId
        self.password = md5.new(password).hexdigest()

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.emailId, self.password)
