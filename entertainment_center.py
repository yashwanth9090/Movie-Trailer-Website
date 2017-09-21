"""Creates seven instances(objects) of movie class and passing arguments like title, storyline, poster and trailer link and displays them in a web browser"""
import media
import fresh_tomatoes

it = media.Movie("IT",
                       "The film tells the story of seven children in Derry, Maine, who are terrorized by the eponymous being, only to face their own personal demons in the process.","http://www.insidethemagic.net/wp-content/uploads/2017/03/it-teaser-poster.jpg","https://www.youtube.com/watch?v=FnCdOQsX5kc","8/10 IMDb")
annabelle_creations = media.Movie("Annabelle: Creations",
                     "In 1943, dollmaker Samuel Mullins and his wife Esther grieve for the loss of their seven-year-old daughter Annabelle, Bee, who died after she was run over by a passing car.",
                     "https://ewedit.files.wordpress.com/2017/03/annabelle.jpg?w=1800&h=2700",
                     "https://www.youtube.com/watch?v=11taaQy2KBg","6.9/10 IMDb")

bahubali_2 = media.Movie("Bahubali 2",
                        "Kattappa continues to narrate how he ended up killing Amarendra Baahubali ",
                        "https://images-na.ssl-images-amazon.com/images/I/711eHgGtnFL._SX385_.jpg",
                        "https://www.youtube.com/watch?v=qD-6d8Wo3do","8.6/10 IMDb")

simran = media.Movie("Simran",
                            "The movie is loosely based on the life of Sandeep Kaur, a non-resident Indian (NRI) in the United States who has been convicted of four bank robberies.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d3/Simran_Poster.jpg","https://www.youtube.com/watch?v=_LUe4r6eeQA","6.2/10 IMDb")
ratatouille = media.Movie("Ratatouille",
                         "A rat is a chef in Paris",
                         "http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg",
                         "https://www.youtube.com/watch?v=c3sBBRxDAqk","8/10 IMDb")
midnight_in_paris = media.Movie("Midnight in Paris",
                               "Going back in time to meet authors",
                               "https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY","7.7/10 IMDb")
hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                          "https://images-na.ssl-images-amazon.com/images/I/51ycTLUq6fL._AC_UL320_SR220,320_.jpg",
                          "https://www.youtube.com/watch?v=4S9a5V9ODuY","7.2/10 IMDb")
#Stores movie objects in an array
movies = [it,annabelle_creations, bahubali_2, simran, ratatouille, midnight_in_paris,hunger_games]
#Displays the movie website in a web browser by passing array of movies
fresh_tomatoes.open_movies_page(movies)