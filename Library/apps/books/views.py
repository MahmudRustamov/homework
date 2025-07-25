from core.file_manager import read

def show_all_books():
    books = read(filename="books")
    if books:
        for book in books:
            print(f"ID: {book[0]}  TITLE: {book[1]}  AUTHOR: {book[2]}  PAGES: {book[3]}  QUANTITY: {book[4]}")
    else:
        print("There are not any books yet")