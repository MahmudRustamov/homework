from apps.auth.utils import get_active_user
from core.file_manager import read

def show_user_rented_books():
    user = get_active_user()

    rents = read(filename="rents")
    rented_books_id = []

    for book in rents:
        if book[2] == user[2]:
            rented_books_id.append(book[1])

    if rented_books_id:
        books = read(filename="books")
        for book in books:
            if book[0] in rented_books_id:
                print(f"ID: {book[0]}  TITLE: {book[1]}  AUTHOR: {book[2]}  PAGES: {book[3]}")
    else:
        print("You do not have any books yet")


