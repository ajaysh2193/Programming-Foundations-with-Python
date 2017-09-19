import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
fast_and_furious7 = media.Movie("Fast & Furious 7",
                             "Story revolves around some friends with their some mission with high speed cars",
                             "https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
                             "https://www.youtube.com/watch?v=Skpu5HaVkOc")
baahubali2 = media.Movie("Baahubali 2",
                        "A story revolve around Mahendra Baahubali and Mahishmati kingdom",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                        "https://www.youtube.com/watch?v=G62HrubdD6o")
jurassic_park = media.Movie("Jurassic Park",
                            "A story of a group visiting on an island where they try to survive against dinosaurs",
                            "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                            "https://www.youtube.com/watch?v=lc0UehYemQA")
three_idiots = media.Movie("3 Idiots",
                      "A story of 3 college friends and about educational system",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                      "https://www.youtube.com/watch?v=K0eDlFX9GMc&t=17s")

#print(toy_story.storyline)
#toy_story.show_trailer()

movies = [toy_story, avatar, fast_and_furious7, baahubali2, jurassic_park, three_idiots]
fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
#print media.Movie.__doc__
