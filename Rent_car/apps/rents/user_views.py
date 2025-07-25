from datetime import datetime 
from apps.auth.utils import get_active_user
from apps.cars.user_views import show_cars, get_car
from core.file_manager import read, append, writerows
from core.utils import get_next_id


def rent_car():
    user = get_active_user()
    show_cars()
    car_id = input("Enter car ID: ").strip()
    
    car = get_car(car_id = car_id)
    while not car:
        print("Car not found!!")
        car_id = input("Enter car ID: ").strip()
        car = get_car(car_id = car_id)

    is_rented = False
    cars = read("cars")
    for car in cars:
        if car[0] == car_id:
            if car[-1].strip() == "Not Rented":
                hours = input("How many hours would you like to rent: ")
                created_at = datetime.now()
                next_id = get_next_id("rents")
                data = [next_id, car[1], car[2], car[3], hours, int(hours) * int(car[-2]), user[0], user[2], created_at]
                append(filename="rents", data=data)

                cars = read(filename="cars")
                for index, car in enumerate(cars):
                    if car[0] == car_id:
                        cars[index][-1] = "Rented"
                        writerows(filename="cars", data=cars)
                        print("Order is created!!")
                        is_rented = True
                        return

    if  not is_rented:
        print("This car is already rented by others ")
        


def show_my_rents():
    user = get_active_user()
    rents = read(filename = "rents")
    is_found = False
    if rents:
        print("<<< My Rents >>>")
        for rent in rents:
            if rent[-3] == user[0]:
                print(f"""ID: {rent[0]}  Name: {rent[1]}  Model: {rent[2]}  Price_for_hour: {rent[3]}  Total Price: {rent[-4]}  Date: {rent[-1]}""")
                is_found = True
        if not is_found:
            print("You do not have any rents")
    else:
        print("Rents not found")
