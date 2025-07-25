from apps.auth.views import register, login, logout
from apps.orders.admin_views import *
from apps.orders.user_views import *
from apps.products.admin_views import *
from apps.products.user_views import *
from apps.auth.views import *


def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)
    choice = input("Choice: ")
    if choice == "1":
        if register():
            print("Successfully registered")
        else:
            print("Something went wrong")
    elif choice == "2":
        result = login()
        if result == "admin":
            print("Welcome Admin")
            return admin_menu()
        elif result == "user":
            return user_menu()
        else:
            return auth_menu()
    elif choice == "3":
        print("Good bye")
        return None
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
    1. Add product
    2. Delete product
    3. Show products
    4. Show all orders
    5. Show all users
    6. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        add_product()
    elif choice == "2":
        delete_product()
    elif choice == "3":
        show_products()
    elif choice == "4":
        show_orders()
    elif choice == "5":
        show_users()
    elif choice == "6":
        logout()
        return auth_menu()
    else:
        print("Invalid choice")
    return admin_menu()


def user_menu():
    print("""
    1. Show all products
    2. Order product
    3. Show my orders
    4. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        show_products()
    elif choice == "2":
        order_product()
    elif choice == "3":
        show_my_orders()
    elif choice == "4":
        logout()
        return auth_menu()
    else:
        print("Invalid choice!!!")

    return user_menu()


if __name__ == '__main__':
    logout()
    auth_menu()
