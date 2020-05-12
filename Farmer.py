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

    def set_money(self, money):
        self.__money = money

    def get_owned_plots(self):
        """
        gets the number of plots owned
        :return: number of plots owned
        """
        counter = 0
        for plots in self.totalPlots:
            if plots.get_owned():
                counter += 1
        return counter

    def get_filled_plots(self):
        """
        gets the number of plots filled
        :return: number of plots filled
        """
        counter = 0
        for plots in self.totalPlots:
            if plots.check_isempty():
                counter += 1
        return counter

    def set_owned(self):
        """
        sets the plots given at the beginning of the game to owned
        :return: None
        """
        counter = 0
        while counter < 4:
            self.totalPlots[counter].set_owned(True)
            self.totalPlots[counter].set_empty(True)
            counter += 1

    def hire_farmHands(self):
        """
        Adds a farmHand to the total amount of farmHands.
        Raises the salary fee.
        :return:
        """
        self.__farmHands += 1

    def fire_farmHands(self):
        """
        Removes a farmHand from the total amount.
        Lowers the salary fee.
        :return:
        """
        self.__farmHands = self.__farmHands - 1

    def buy_plot(self):
        """
        Purchases another plot of land for the farmer to use.
        Makes a new plot True.
        Subtracts the price from self.__money.
        :return: None
        """
        plotPrice = 50
        confirm = toolbox.get_boolean(f'Are you sure you want to purchase another plot for ${plotPrice}? : ')
        if confirm:
            self.__money = self.__money - plotPrice
            if self.__money < plotPrice:
                self.__money = self.__money + plotPrice
                print("You don't have enough money to make this purchase.")
            else:
                counter = 0
                #
                # Loop through the list of plots and count the number of plots owned
                #
                for plots in self.totalPlots:
                    if plots.get_owned():
                        counter += 1
                self.totalPlots[counter].set_owned(True)
                self.totalPlots[counter].set_contents("EMPTY")
                self.hire_farmHands()
                print('\nYou also hired a farmhand to work on the new land.\n')

    def sell_plot(self):
        """
        Sells a plot of land chosen by the user.
        Change that plot to be False.
        Gives money depending on the value of the land.
        :return: None
        """
        plotPrice = 25
        confirm = toolbox.get_boolean("Are you sure you want to sell a plot?")
        if confirm:
            counter = 0
            for plots in self.totalPlots:
                if plots.get_owned():
                    counter += 1
            self.totalPlots[counter-1].set_owned(False)
            self.__money = self.__money + plotPrice
            print('You also fired a farmhand as they had no job.')
            self.fire_farmHands()

    def get_plot(self):
        counter = 0
        for plots in self.totalPlots:
            if plots.get_owned():
                counter += 1
        whichPlot = toolbox.get_integer_between(1, counter, "Which plot? ", "**ERROR: You must choose an owned plot**")
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
        return float(self.__money)

    def get_totalPlots_length(self):
        return len(self.totalPlots)

    def get_totalPlots(self):
        return self.totalPlots