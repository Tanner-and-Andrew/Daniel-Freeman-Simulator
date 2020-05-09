class Animals(object):

    def __init__(self, type, price, product, productValue, sellValue):
        self.__type = type
        self.__price = price
        self.__product = product
        self.__productValue = productValue
        self.__sellValue = sellValue

    def get_type(self):
        return self.__type

    def get_price(self):
        return float(self.__price)

    def get_product(self):
        return self.__product

    def get_productValue(self):
        return float(self.__productValue)

    def get_sellValue(self):
        return float(self.__sellValue)

    def __str__(self):
        string = f"{self.__type}...\n   Cost: {self.__price}\n   Product: {self.__product}, sells at ${self.__productValue} per pound"
        string += f"\n  Sell Price: each {self.__type} sells at {self.__sellValue} per {self.__type}"
        return string