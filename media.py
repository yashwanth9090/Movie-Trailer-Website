"""This module defines Movie class that provides a way to store attrubutes of a movie and to display movie trailer """
import webbrowser
class Movie():
    
    """This class stores movie related information like Movie title, Movie storyline, Movie poster, Movie trailer"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,rating):
        """This method initialises instance variables that are passed as a argument to this method"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        
    def show_trailer(self):
        """Plays the movie trailer in the web browser"""
        webbrowser.open(self.trailer_youtube_url)