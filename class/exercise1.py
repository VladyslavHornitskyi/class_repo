
#Class exercise file
class Book:
    def __init__(self, title, book_id):
        self.title = title
        self.book_id = book_id
book_1 = Book("The Great Gatsby", 1)
book_2 = Book("The Lord of the Rings", 2)



class Library:
    def __init__(self,city, name, book_list, user_list):
        self.city = city
        self.name = name
        self.book_list = book_list
        self.user_list = user_list

    def add_book(self, book):
        self.book_list.append(book)

    def add_users(self, user):
        self.user_list.append(user)

first_library = Library("Brussels", "Uccle libtary",[book_1], [])

first_library.add_book(book_2)

class User:
    def __init__(self, name, borrowed_books):
        self. name = name
        self.borrowed_books = []

    def borrow_book(self, library, book):
        if book in book_list:
            self.borrow_book.append(book)
        else:
            print("Book is not in the library")

    def return_book(self, library, book):
        if book in self.borrow_book:
            self.borrow_book.remove(book)
