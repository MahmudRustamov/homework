from datetime import datetime 
from apps.auth.utils import get_active_user
from apps.products.user_views import show_products, get_product
from core.file_manager import read, append, writerows
from core.utils import get_next_id


def order_product():
    user = get_active_user()
    show_products()
    product_id = input("Enter product ID: ").strip()
    
    product = get_product(product_id=product_id)
    while not product:
        print("Product id not found!!")
        product_id = input("Enter product ID: ").strip()
        product = get_product(product_id=product_id)

    quantity = input("Enter quantity: ")
    while int(product[-1]) < int(quantity):
        print("Not enough products!!")
        quantity = input("Enter quantity: ")

    created_at = datetime.now()
    next_id = get_next_id("orders")
    data = [next_id, product[1], product[2], quantity, int(quantity) * int(product[2]), user[0], user[2], created_at]
    append(filename="orders", data=data)

    products = read(filename="products")
    for index, product in enumerate(products):
        if product[0] == product_id:
            products[index][-1] = int(products[index][-1]) - int(quantity)
            writerows(filename="products", data=products)
            print("Order is created!!")
            return


def show_my_orders():
    user = get_active_user()
    orders = read(filename = "orders")
    is_found = False
    if orders:
        print("<<< My Orders >>>")
        for order in orders:
            if order[-3] == user[0]:
                print(f"""ID: {order[0]}  Name: {order[1]}  Price: {order[2]}  Quantity: {order[3]}  Total Price: {order[4]}  Date: {order[-1]}""")
                is_found = True
        if not is_found:
            print("You do not have any orders")
    else:
        print("Orders not found")
