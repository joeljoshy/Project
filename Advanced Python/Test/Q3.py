# Create a Book class with instance Library_name, book_name, author, pages

class Book:


    def book(self, Library_name,book_name,author,pages):

        self.Library_name = Library_name
        self.book_name = book_name
        self.author= author
        self.pages = pages


    def print(self):
        print("Library Name : ",self.Library_name, "\nBook Name : ",self.book_name, "\nAuthor :",self.author, "\nPages : ",self.pages)


obj = Book()
obj.book('Gov. Library','Das Kapital', 'Karl Marx', 250)
obj.print()