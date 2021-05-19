class Book:
    def details(self,book_name,author):
        self.book_name = book_name
        self.author = author

        print("Book Name :",self.book_name, "Author Name : ",self.author)

class Author(Book):
    def author_details(self,age,place,gender):
        self.age = age
        self.place = place
        self.gender = gender

        print("Age : ",self.age, "Gender : ",self.gender, "Place : ",self.place)

    def __str__(self):
        return self.book_name+" , "+self.author


bk = Author()
bk.details('Alchemist ','Paulo Coelho')
bk.author_details(50,' Male','Brazil')
print(bk)


# to string
