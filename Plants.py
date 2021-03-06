class Plants(object):

    def __init__(self, type, price, risk, sellValue, lowerLimit, upperLimit):
        self.__type = type
        self.__price = price
        self.__risk = risk
        self.__sellValue = sellValue
        self.__lowerLimit = lowerLimit
        self.__upperLimit = upperLimit

    def get_type(self):
        return self.__type

    def get_price(self):
        return float(self.__price)

    def get_risk(self):
        return self.__risk

    def get_sellValue(self):
        return float(self.__sellValue)

    def get__lowerLimit(self):
        return self.__lowerLimit

    def get__upperLimit(self):
        return float(self.__upperLimit)

    def set_sellValue(self, newValue):
        self.__sellValue = newValue

    def __str__(self):
        string = f"{self.__type}...\n   Cost: {self.__price}\n   Success Rate: {self.__risk}"
        string += f"\n  Sell Price: each {self.__type} sells at {self.__sellValue} per bushel"
        return string