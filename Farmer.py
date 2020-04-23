import toolbox
from Plot import Plot


class Farmer(object):

    def __init__(self):
        self.__farmHands = 0
        self.__family = 0
        self.__money = 0
        self.__totalPlots = []

    def hire_farmHands(self):
        """
        Adds a farmHand to the total amount of farmHands.
        Raises the salary fee.
        :return:
        """
        confirm = toolbox.get_boolean("Are you sure you want to hire a farm hand? : ")
        if confirm:
            self.__farmHands += 1

    def fire_farmHands(self):
        """
        Removes a farmHand from the total amount.
        Lowers the salary fee.
        :return:
        """
        confirm = toolbox.get_boolean("Are you sure you want to fire a farm hand? : ")
        if confirm:
            amount = toolbox.get_integer_between(1, self.__farmHands, "How many farm hands would you like to fire?: ")
            self.__farmHands = self.__farmHands - amount

    def buy_plot(self):
        """
        Purchases another plot of land for the farmer to use.
        Adds a plot to self.__totalPlots.
        Subtracts the price from self.__money.
        :return: None
        """
        plotPrice = 50
        confirm = toolbox.get_boolean('Are you sure you want to purchase another plot? : ')
        if confirm:
            self.__money = self.__money - plotPrice
            if self.__money < 0:
                self.__money = self.__money + plotPrice
                print("You don't have enough money to make this purchase.")
            else:
                self.__totalPlots.append('plot')

