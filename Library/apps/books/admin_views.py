from core.utils import get_next_id
from core.file_manager import append, read, writerows
from datetime import datetime
from apps.books.user_views import show_user_rented_books


def add_book():
    title = input("Enter title of the book: ")
    author = input("Enter author name: ")
    pages = input("Pages: ")
    quantity = input("Quantity: ")

    next_id = get_next_id("books")
    append(filename="books", data=[next_id, title, author,pages,quantity])
    print("New book is added successfully")


def delete_book():
    books = read(filename="books")
    book_id = input("Enter book id to delete: ")
    is_found = False
    for index, book in enumerate(books):
        if book[0] == book_id:
            books.pop(index)
            is_found = True
            break

    if is_found:
        writerows(filename="books", data=books)
        print("Book is deleted successfully")
    else:
        print("Book is not found!!")        



def rent_book():
    email = input("Enter your email: ")
    users = read(filename = "users")
    is_found = False
    for user in users:
        if user[2] == email:
            is_found = True
            break

    if is_found:
        book_id = input("Enter book ID: ")
        books = read(filename="books")
        for index, book in enumerate(books):
            if book[0] == book_id and int(books[index][-1]) > 1:
                books[index][-1] = int(books[index][-1]) - 1
                writerows(filename="books", data = books)

                next_id = get_next_id(filename="rents")
                data = [next_id, book_id, email, datetime.now()]
                append(filename="rents", data = data)
                print("Book is rented")
                return 
        print("Book is not found")
    else:
        print("User not found, please register first")


def return_book():
    email = input("Enter your email: ")
    users = read(filename = "users")
    is_found = False
    for user in users:
        if user[2] == email:
            is_found = True
            break
    rents = read(filename="rents")
    rented_books_id = []
    for book in rents:
        if email in book[2]:
            rented_books_id.append(book[1])
    
    books = read(filename="books")
    if rented_books_id:
        for book in books:
            if book[0] in rented_books_id:
                print(f"ID: {book[0]}  TITLE: {book[1]}  AUTHOR: {book[2]}  PAGES: {book[3]}")
    else:
        print("User do not have any rented books yet")


    if is_found:
        book_id = input("Enter book ID: ")
        is_rented = False
        for index, book in enumerate(rents):
            if book[1] == book_id and email == book[2]:
                rents.pop(index)
                writerows(filename="rents", data = rents)
                is_rented =True
                break
        if is_rented:
            for index, book in enumerate(books):
                if book[0] == book_id:
                    books[index][-1] = int(books[index][-1]) + 1
                    writerows(filename="books", data = books)
                    break
            print("Book is returned!!")
        else:
            print("Book is not found")
    else:
        print("User not found, please register first")



def show_all_rented_books():
    rents = read(filename="rents")
    if rents:
        for book in rents:
            print(f"Rent ID:  {book[0]}  Book ID: {book[1]}  User: {book[2]}  DATE: {book[3]}")
    else:
        print("Book is not found!!")