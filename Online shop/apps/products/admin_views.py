from core.utils import get_next_id
from core.file_manager import append, read, writerows
from apps.products.user_views import show_products

def add_product():
    name = input("Product name: ")
    price = input("Price $: ")
    quantity = input("Quantity: ")

    next_id = get_next_id("products")
    append(filename="products", data=[next_id,name, price, quantity])
    print("New product is added successfully")


def delete_product():
    show_products()
    product_id = input("To delete, enter the product ID: ").strip()
    products = read("products")
    is_found = False
    for index, product in enumerate(products):
        if product[0].strip() == product_id:
            products.pop(index)
            is_found = True
            break

    if is_found:
        writerows(filename="products", data=products)
        print("Product was deleted successfully!!")
    else:
        print("Product not found!!!")


    


