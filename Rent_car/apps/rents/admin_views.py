from core.file_manager import read


def show_rents():
    rents = read(filename="rents")
    if rents:
        for rent in rents:
            print(f"ID: {rent[0]}  Name: {rent[1]}  Model: {rent[2]}  Price for an hour: {rent[3]}  Total price: {rent[-4]} User_ID: {rent[-3]} User: {rent[-2]}")
    else:
        print("There are no rents yet!!!")