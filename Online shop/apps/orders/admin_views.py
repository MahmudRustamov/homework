from core.file_manager import read


def show_orders():
    orders = read(filename="orders")
    if orders:
        for order in orders:
            print(f"ID: {order[0]}  Name: {order[1]}  Price: {order[2]}  Quantity: {order[3]}  Total price: {order[4]}  User_id: {order[5]}  Email: {order[6]}  Date: {order[-1]}")
    else:
        print("There are no orders yet!!!")