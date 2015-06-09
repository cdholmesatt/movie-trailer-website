
                
import fresh_cherrytomatoes
import media
import os
import os.path
import sys
import urllib
import json
import re

omdb = "http://www.omdbapi.com/?t="
youtube = "http://www.youtube.com/"
imdb = "http://www.imdb.com/"

class Movie():
        """ README FILE
        -----------------------------------------------------------------------------------
        media.py - python file for a Movie info and Movie trailer program.  
        -----------------------------------------------------------------------------------
        This is the 1st program for the Nanodegree for Full Stack Developer - P1 Submission 

        Available Modules:
        media.py
        entertainment.py
        fresh_cherrytomatoes.py
        -----------------------------------------------------------------------------------
        This is the documentation for the Movie class in media.py 
        The class was designed to receive a movie_title value from entertainment.py

        The movie_title value is then used to search youtube for the official movie trailer
        html output is returned and searched using regular expressions and match
        store in trailer_result

        The movie_title value is then used to search the omdb site, the
        omdb dictionary values are passed as json output from omdb code
        -----------------------------------------------------------------------------------
	Directions - To run this program you will need to execute entertainment.py python program
	Which will import and pass values to media.py and fresh_cherrytomatoes.py.  The result being a 
	html page being opened that will display the box image and listing and details of the developers 
	favorite movies.
	-----------------------------------------------------------------------------------
	License - This program is free software: you can redistribute it and/or modify it under the
	terms of the GNU General Public License as published by the Free Software Foundation, either
	version 3 of the License, or (at your option) any later version.
	This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
	without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
	See the GNU General Public License for more details.
	You should have received a copy of the GNU General Public License along with this program. 
	If not, see http://www.gnu.org/licenses/.
	-----------------------------------------------------------------------------------
	Author - C.Holmes
	-----------------------------------------------------------------------------------
	Date - 6/8/2015
	"""

        
        def __init__(self,movie_title):
            #Creates an object of a movie
            self.title = movie_title
            #Searches youtube for the official movie trailer associated with the contents of movie_title
            search_text = movie_title+" trailer official"
            movie = {"search_query":search_text}
            search = urllib.urlopen(youtube+'results'+"?"+urllib.urlencode(movie))
            result = search.read()
            search.close()       
            match = re.search('\"yt-lockup-title\"\>\<a href=\"\/watch\?v\=([\w|\d|-|_]+)\"\s',result)
            if match:
               match.group(1)
               trailer_youtube = youtube+'watch?v='+match.group(1)
                   
            #Searches omdb for the movie elements associated with the contents of movie_title
            connection = urllib.urlopen(omdb+self.title+"&y=&plot=short&r=json")
            jsoninput = connection.read()
            try:
                            #then save the result contents of dictionary into "decoded" 
                            decoded = json.loads(jsoninput)
                            #print json.dumps(decoded, sort_keys=True, indent=4)
                            
                            imdbURL = imdb +'title/'+decoded['imdbID']+"/?ref_=nv_sr_1"
                            #Plot, Poster, trailer_youtube,Released, Year, Genre,Director, Rated, Actors):           
                            self.storyline = decoded['Plot']
                            self.poster_image_url = decoded['Poster']
                            self.trailer_youtube_url = trailer_youtube
                            self.release_date = decoded['Released']
                            self.year = decoded['Year']
                            self.genre = decoded['Genre']
                            self.director = decoded['Director']
                            self.rating = decoded['Rated']
                            self.actors = decoded['Actors']
                            self.imdburl = imdbURL
                            
            except (ValueError, KeyError, TypeError):
                            print "JSON format error"
