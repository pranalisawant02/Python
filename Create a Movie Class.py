#Q21. Create a Movie Class

class Movie:
  def __init__(self, title,genre,rating):
    self.title=title
    self.genre=genre
    self.rating=rating

  def display_details(self):
    print (f"Title: {self.title}\nGenre: {self.genre}\nRating: {self.rating}")

mov=Movie("Sholay","Action,Drama",10)

mov.display_details()
