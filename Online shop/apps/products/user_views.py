from core.file_manager import read


def show_products():
    products = read(filename="products")
    if products:
        print("\n<<< Products List >>>")
        for product in products:
            try:
                print(f"ID: {product[0]} ->  Name: {product[1]}  Price: {product[2]}  Quantity: {product[3]}")
            except IndexError:
                print("Warning: Some product data is incomplete.")
    else:
        print("There are not any products yet")


def get_product(product_id):
    products = read(filename="products")
    for product in products:
        if product[0] == product_id:
            return product
        
    return False

        

