# this approach works but is not considered a "pythonic" way
class Product:
    def __init__(self, price):
        # self.__price = price
        self.set_price(price)

    def ger_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("price cannot be 0 or less")

        self.__price = price


try:

    product = Product(-100)
    print(product.ger_price())
except:
    print("something went wrong, ")


# ----------------------------------------------------------
# pythonic way


class Product:

    def __init__(self, price):
        self.set_price(
            price
        )  # set_price method is called to initialize price and validate the passed value at the same time

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price

    # now we can go and create a property with ideal name here "price"
    price = property(get_price, set_price)


product = Product(1000)
print(product.get_price())
product.set_price(-2000)
print(product.get_price())
print()

# OK, Great now we can get or set the private-property "price" just like a normal instance property, but we still have those (get_price/set_price) methods

print(product.price)
product.price = 4000
print(product.price)

product.get_price()  # like so

# --------------------------------------------------------
# modern way


class Product:

    def __init__(self, price):
        self.price = price # now the price property can be accessed as a normal instance property (just inside the initializer/constructor)

    @property # @property decorator is called to mark this method as a getter method 
    def price(self): # now we can name this method "price" instead of "get_price"
        return self.__price

    @price.setter # @propertyName.setter decorator is called to mark this method as a setter method for "price"
    def price(self, price): # now we can name this method "price" instead of "set_price"
        if price > 0:
            # self.__price = price
            self.__price = price

print()
product = Product(1000)
print(product.price)
product.price = 430
product.price = -430 # negative value is ignored

print(product.price)