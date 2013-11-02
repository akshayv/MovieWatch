from com.akshay.moviewatch.business.dao.UserDao import UserDao
from com.akshay.moviewatch.business.service.EmailService import EmailService
from com.akshay.moviewatch.domain.User import User

__author__ = 'akshay'


class UserService:

    userDao = UserDao()

    def notifyReleased(self, movie, user):
        emailService = EmailService()
        subject = movie.title + ' has been released'
        body = 'You were interested in ' + movie.title + ', and this email is being ' \
                                                         'sent because the movie has been released!' \
                                                         ' \n\n\nEnjoy!\n\nCheers'
        emailService.sendForUser(user, subject, body)
        del emailService

    def notifyDVDRelease(self, movie, user):
        emailService = EmailService()
        subject = 'DVD for ' + movie.title + ' has been released'
        body = 'You were interested in ' + movie.title + ', and this email is being ' \
                                                         'sent because the DVD for the movie has' \
                                                         ' been released \n\n\nEnjoy!\n\nCheers'
        emailService.sendForUser(user, subject, body)
        del emailService

    def createUser(self, userName, password, emailId):
        user = User(userName, emailId, password)
        self.userDao.saveUser(user)

    def authenticate(self, userEmail, password):
        return self.userDao.findByEmailIdAndPassword(userEmail, password)