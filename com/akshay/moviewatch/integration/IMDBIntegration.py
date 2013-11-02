import json
import urllib2
from com.akshay.moviewatch.domain.MovieMin import MovieMin
__author__ = 'akshay'


class IMDBIntegration:
    def __init__(self):
        pass

    def getSuggestedTitles(self, title):

        titles = urllib2.urlopen("http://www.imdb.com/xml/find?json=1&q=" + urllib2.quote(title.encode('utf-8'))).read()
        titlesJSON = json.loads(titles)['title_popular']
        movies = []
        for titleJSON in titlesJSON:
            movie = MovieMin()
            movie.title = titleJSON['title']
            movie.metaData.append({'description': titleJSON['description']})
            movie.imdbId = titleJSON['id']
            movies.append(movie)
            if len(movies) > 2:
                break
        return movies

#
# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
#     movie = Movie('Pacific Rim', '2013')
#     integration = IMDBIntegration()
#     movies = integration.getSuggestedTitles('Harry Potter and the Deathly Hallows')
#     print movies
