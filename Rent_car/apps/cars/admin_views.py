from core.utils import get_next_id
from core.file_manager import append, read, writerows

def add_car():
    name = input("Car name: ")
    model = input("Model: ")
    price_for_hour = input("Price for an hour: ")

    next_id = get_next_id("cars")
    append(filename="cars", data=[next_id, name, model, price_for_hour, "Not Rented"])
    print("New car is added successfully")


def delete_car():
    cars = read("cars")
    car_id = input("Enter car ID: ")
    is_found = False
    for index, car in enumerate(cars):
        if car[0] == car_id:
            cars.pop(index)
            is_found = True
            break
    if is_found:
        writerows(filename="cars", data = cars)
        print("Car is deleted successfully!!")
    else:
        print("Car is not found")
    
