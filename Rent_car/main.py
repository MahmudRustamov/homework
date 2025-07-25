from apps.auth.views import register, login, logout
from apps.rents.admin_views import *
from apps.rents.user_views import *
from apps.cars.admin_views import *
from apps.cars.user_views import *
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
    1. Add car
    2. Show cars
    3. Delete cars
    4. Show all rents
    5. Show all users
    6. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        add_car()
    elif choice == "2":
        show_cars()
    elif choice == "3":
        delete_car()
    elif choice == "4":
        show_rents()
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
    1. Show all cars
    2. Rent a car
    3. Show my rents
    4. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        show_cars()
    elif choice == "2":
        rent_car()
    elif choice == "3":
        show_my_rents()
    elif choice == "4":
        logout()
        return auth_menu()
    else:
        print("Invalid choice!!!")

    return user_menu()


if __name__ == '__main__':
    logout()
    auth_menu()
