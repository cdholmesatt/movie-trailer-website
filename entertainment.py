
""" UDACITY FULL STACK WEB DEVELOPER NANODEGREE  - PROJECT 1
Entertainment.py - python file for Movie info and Movie trailer program.  
-----------------------------------------------------------------------------------
This is the 1st program for the Nanodegree for Full Stack Developer - P1 Submission 

Available Modules:
media.py
entertainment.py
fresh_cherrytomatoes.py
-----------------------------------------------------------------------------------
This is the documentation for entertainment.py
#
#This program allows a user to view information arranged
#concerning a pre-built list of several of the developers
#favorite movies and relevant detail concerning the movie.
#The detail is fetched from omdb.com using
#
#            'Plot'
#            'Poster'
#            'trailer_youtube'
#            'Released'
#            'Year'
#            'Genre'
#            'Director'
#            'Rated'
#            'Actors'
#You can click the poster image of the movie and it will
#kick off the official movie trailer found on www.youtube.com
        
-----------------------------------------------------------------------------------"""

import fresh_cherrytomatoes
import media

#instances of media.Movie created for all of the developers list of
#favorite movies to fetch data
matrix = media.Movie("The Matrix")
scarface = media.Movie("Scarface")
thegoodbadugly = media.Movie("The Good The Bad And The Ugly")
independenceday = media.Movie("Independence Day")
sanandreas = media.Movie("San Andreas")
jurassicworld = media.Movie("Jurassic World")
goodfellas = media.Movie("goodfellas")
trainingday = media.Movie("Training Day")
age_of_ultron = media.Movie("Age of Ultron")
django = media.Movie("Django Unchained")
godfather = media.Movie("The GodFather")
pulpfiction = media.Movie("Pulp Fiction")
killbill = media.Movie("Kill Bill: Vol. 1")
killbill2 = media.Movie("Kill Bill: Vol. 2")
movies = [matrix,scarface,thegoodbadugly,independenceday,sanandreas,jurassicworld,goodfellas,trainingday,age_of_ultron,django,godfather,pulpfiction,killbill,killbill2]     
fresh_cherrytomatoes.open_movies_page(movies)
#prints documentation used to build the readme file
print media.Movie.__doc__
