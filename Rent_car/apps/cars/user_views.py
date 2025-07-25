from core.file_manager import read


def show_cars():
    cars = read(filename="cars")
    if cars:
        print("\n<<< Cars List >>>")
        for car in cars:
            try:
                print(f"ID: {car[0]} ->  Name: {car[1]}  Model: {car[2]}  Price for an hour: {car[3]}  Status: {car[-1]}")
            except IndexError:
                print("Warning: Some cars data is incomplete.")
    else:
        print("There are not any cars yet")


def get_car(car_id):
    cars = read(filename="cars")
    for car in cars:
        if car[0] == car_id:
            return car
        
    return False

        

