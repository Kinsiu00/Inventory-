# Then create an inventory class which keeps track of various products 
# and can sum up the inventory value.
from product import Product

class Inventory:
    def __init__(self): 
        # Make a list of item dictionaries
        self.products = []
        self.last_id = 0

    def define_product(self):
        print("Please enter new product information")
        name = input("Name: ")
        price = input("Price: ")
        while self.validate(price) == -1:
            price = input("Price must be a number: ")
        price = self.validate(price)
        quantity = input("Quantity: ")
        while self.validate(quantity) == -1:
            quantity = input("Quantity must be a number: ")
        quantity = self.validate(quantity)
        _id = self.get_last_id()
        self.set_product(name, price, _id, quantity)

    def validate(self, vals):
        vals = [v for v in vals if not v.isalpha()]

        if len(vals) == 0:
            return -1
        else:
            return int("".join(vals))  

    def set_product(self, name, price, _id, quantity):
        product = Product(name, price, _id, quantity)
        self.products.append(product)

    #Make unique lists of ID, Price, and Quantity
    def list_products(self):
        print("ID\tProduct\tPrice\tQuantity")
        for p in self.products:
            if p is not None:
                product = p.get_products()
                name, price, _id, quantity = product[0], product[1], product[2], product[3]
                print("{}\t{}\t${}\t{}".format(_id, name, price, quantity))
            ##print("Product: {} Price: ${} ID: {} Quantity: {}".format(name, price, id, quantity))
        print("Total products listed: {}".format(len(self.products)))

    def value(self):
        print("here")
        #list comprehension to calculate the price of the products in the inventory
        values = [product.get_product("price") for product in self.products]
        #formats the total value
        return "Total Value: {}".format(sum(values))

    def search_by_id(self, key):
        index = 0
        for p in self.products: 
            product = p.get_products()
            _id = product[2]
            if _id == key:
                return index
            index += 1
        return -1

    def delete_product(self, _id):
        index = self.search_by_id(int(_id))
        if index < 0:
            print("Invalid Id is selected. please see product listing for correct id.")
        else:
            del self.products[index]
            print("Product with id {} is successfully deleted".format(_id))

    def update_product(self, _id):
        index = self.search_by_id(int(_id))
        if index < 0:
            print("Invalid Id is selected. please see product listing for correct id.")
        else:
            product = self.products[index].get_products()
            name, price, _id, quantity = product[0], product[1], product[2], product[3]
            print(product)
            print("Please enter product information to update. If left blank value will not be updated")
            uname = input("Name: ")
            if uname is not None and uname != "":
               name = uname 
            uprice = input("Price: ")
            if uprice is not None:
               price = uprice
            uquantity = input("Quantity: ")
            if uquantity is not None:
               quantity = uquantity
            product = Product(name, price, _id, quantity)
            self.products[index] = product
            print("Product with id {} is successfully updated".format(_id))

    def get_last_id(self):
        self.last_id += 1
        return self.last_id
