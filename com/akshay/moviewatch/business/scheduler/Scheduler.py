from apscheduler.scheduler import Scheduler
from com.akshay.moviewatch.business.dao.MovieDao import MovieDao
from com.akshay.moviewatch.business.service.UserService import UserService
from com.akshay.moviewatch.domain.Status import Status

__author__ = 'akshay'

sched = Scheduler()
movieDao = MovieDao()
userService = UserService()


@sched.cron_schedule(day_of_week='mon-sun', hour=8)
def scheduled_job():
    print 'This job is run every everyday at 8am.'
    movies = movieDao.findByStatus(Status.PRE_RELEASE)
    #TODO: CHECK IF MOVIE IS RELEASED
    for movie in movies:
        movieDao.setStatus(movie, Status.RELEASED)
        for user in movie.listeningUsers:
            userService.notifyReleased(movie, user)

    movies = movieDao.findByStatus(Status.RELEASED)
    #TODO: CHECK IF DVD IS RELEASED
    for movie in movies:
        movieDao.setStatus(movie, Status.DVD_RELEASED)
        for user in movie.listeningUsers:
            userService.notifyDVDRelease(movie, user)


sched.start()

while True:
    pass