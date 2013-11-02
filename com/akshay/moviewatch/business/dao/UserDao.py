import md5
from com.akshay.moviewatch.business.dao.Dao import session
from com.akshay.moviewatch.domain.User import User

__author__ = 'akshay'


class UserDao:
    def saveUser(self, user):
        session.add(user)
        session.commit()

    def findAll(self):
        return session.query(User).all()

    def findById(self, id):
        return session.query(User).filter(User.id == id).one()

    def findByEmailId(self, emailId):
        return session.query(User).filter(User.emailId == emailId).first()

    def findByEmailIdAndPassword(self, emailId, password):
        return session.query(User).filter(User.emailId == emailId).filter(
            User.password == md5.new(password).hexdigest()).one()