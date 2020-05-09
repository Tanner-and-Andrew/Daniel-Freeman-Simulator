import toolbox
from Plot import Plot


class Farmer(object):

    def __init__(self, family, farmHands):
        self.__farmHands = farmHands
        self.__family = family
        self.__money = 200
        self.totalPlots = [Plot(), Plot(), Plot(), Plot(), Plot(), Plot(), Plot(), Plot(),
                           Plot(), Plot(), Plot(), Plot(), Plot(), Plot(), Plot(), Plot(),
                           Plot(), Plot(), Plot(), Plot()]
        self.set_owned()

    def __str__(self):
        string = 'Family Members:'
        string += f'\nTotal = {self.__family}'
        string += f'\nWorkers = {self.__family - 1}'
        string += '\n\nOthers:'
        string += f'\n\nFarm Hands = {self.__farmHands}'
        string += f'\n\nMoney = {self.__money}'
        string += f'\n\nPlots = {len(self.totalPlots)}'
        print(string)

    def get_owned_plots(self):
        counter = 0
        for plots in self.totalPlots:
            if plots.get_owned():
                counter += 1
        return counter

    def set_owned(self):
        counter = 0
        while counter < 4:
            self.totalPlots[counter].set_owned(True)
            counter += 1

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
            if self.__farmHands < 0:
                print("You don't have that many farm hands to fire.")
                self.__farmHands = self.__farmHands + amount

    def buy_plot(self):
        """
        Purchases another plot of land for the farmer to use.
        Makes a new plot True.
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
                counter = 0
                for plots in self.totalPlots:
                    if plots.get_owned():
                        counter += 1
                self.totalPlots[counter].set_owned(True)

    def sell_plot(self):
        """
        Sells a plot of land chosen by the user.
        Change that plot to be False.
        Gives money depending on the value of the land.
        :return: None
        """
        plotPrice = 25
        whichPlot = toolbox.get_integer_between(1, len(self.totalPlots), "Which plot would you like to sell? ")
        whichPlot = whichPlot - 1
        confirm = toolbox.get_boolean("Are you sure you want to sell this plot?")
        if confirm:
            counter = 0
            for plots in self.totalPlots:
                if plots.get_owned():
                    counter += 1
            self.totalPlots[counter-1].set_owned(False)

    def get_plot(self):
        counter = 0
        for plots in self.totalPlots:
            if plots.get_owned():
                counter += 1
        whichPlot = toolbox.get_integer_between(1, counter, "Which plot would you like to put this on? ")
        whichPlot = whichPlot - 1
        return whichPlot

    def plant(self, whichPlot, plant, index):
        self.totalPlots[whichPlot].set_plant(plant, index)

    def import_animal(self, whichPlot, animal, index):
        self.totalPlots[whichPlot].set_animal(animal, index)

    def get_farmHands(self):
        return self.__farmHands

    def get_family(self):
        return self.__family

    def get_money(self):
        return self.__money

    def get_totalPlots_length(self):
        return len(self.totalPlots)

    def get_totalPlots(self):
        return self.totalPlots