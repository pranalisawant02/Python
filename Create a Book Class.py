#Q18.  Create a Book Class

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def book_details(self):
        print (f"Title: {self.title}\nAuthor: {self.author}")

book1 = Book("To Kill a Mockingbird", "Harper Lee")

# Display book details
book1.book_details()
