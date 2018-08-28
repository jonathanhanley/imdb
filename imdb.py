import json
import requests
class Movie(object):
    title=""
    year=""
    rated=""
    released=""
    runtime=""
    genre=""
    director=""
    writer=""
    actors=""
    plot=""
    language=""
    country=""
    awards=""
    poster=""
    metascore=""
    imdbRating=""
    dvd=""
    boxOffice=""


    def __init__(self,title,year,rated,released,runtime,genre,director,writer,actors,plot,language,country,awards,poster,metascore,imdbRating,dvd,boxOffice):
        self.title=title
        self.year=year
        self.rated=rated
        self.released=released
        self.runtime=runtime
        self.genre=genre
        self.director=director
        self.writer=writer
        self.actors=actors
        self.plot=plot
        self.language=language
        self.country=country
        self.awards=awards
        self.poster=poster
        self.metascore=metascore
        self.imdbRating=imdbRating
        self.dvd=dvd
        self.boxOffice=boxOffice
def json_(name):
    name=name.replace(' ','%20')

    get=requests.get('http://www.omdbapi.com/?apikey=db229f4&t=%s'%name)
    data=get.json()
    return data

def make_movie(name):
    data=json_(name)
    title=data['Title']
    year=data['Year']
    rated=data['Rated']
    released=data['Released']
    runtime=data['Runtime']
    genre=data['Genre']
    director=data['Director']
    writer=data['Writer']
    actor=data['Actors']
    language=data['Language']
    country=data['Country']
    awards=data['Awards']
    poster=data['Poster']
    metascore=data['Metascore']
    plot=data['Plot']
    imdbRating='imdbRating'
    dvd='DVD'
    boxOffice='BoxOffice'
    movie=Movie(title,year,rated,released,runtime,genre,director,writer,actor,plot,language,country,awards,poster,metascore,imdbRating,dvd,boxOffice)
    return movie
def object(name):
    movie=make_movie(name)
    return movie
