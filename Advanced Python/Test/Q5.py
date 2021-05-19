# . What is method overriding give an example using Books class

# Method overloading - Its is when class have same method name and different arguments.

class Book:

    def book(self,name,author):
        self.name = name
        self.author = author
        print("Book :",self.name,self.author)

class Author(Book):

    def book(self,gender,age):
        self.gender = gender
        self.age = age
        print("Author :",self.gender,self.age)

ob = Author()
ob.book('Male','23')