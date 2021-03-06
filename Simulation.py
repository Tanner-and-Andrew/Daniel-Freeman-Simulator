from Farmer import Farmer
from Economy import Economy
from Plants import Plants
from Animals import Animals
from time import sleep
from Plot import Plot
import toolbox
from time import sleep


class Simulation(object):

    def __init__(self):
        self.__menu = 'main'
        self.__farmer = None
        self.__plants = []
        self.read_plants('plants.csv')
        self.__animals = []
        self.read_animals('animals.csv')
        self.__economy = Economy(self.__animals, self.__plants)

    def main(self):
        self.help('farmhelp.txt')
        command = ''
        self.get_family()
        self.show_plots()
        while command != 'quit':
            if command == 'help':
                self.help('farmhelp.txt')
            elif command == 'advance':
                command = self.advance()
            elif command == 'plant':
                self.plant()
            elif command == 'breed':
                self.import_animal()
            elif command == 'shop':
                self.__menu = 'shop'
            elif command == 'report':
                self.__economy.print_farm_report()
                answer = input("<Press RETURN to continue>")
            elif command == 'reset':
                self.reset()
            elif command == 'land':
                self.__farmer.buy_plot()
            elif command == 'sell land':
                self.__farmer.sell_plot()
                self.show_plots()
            elif command == 'sell animal':
                self.sell_animals()
            elif command == 'back':
                self.__menu = 'main'
            if command == 'quit':
                print("\n          ...GAME OVER...")
            else:
                self.get_menu()
                self.__menu = 'main'
                command = self.get_command()

    def get_menu(self):
        """
        Displays the menu.
        :return:
        """
        if self.__menu == 'main':
            print("[A]dvance  [P]lant  [B]reed  [S]hop  Last [Y]ear's Report  [R]eset  [Q]uit")
        if self.__menu == 'shop':
            print("Purchase: [L]and   Sell: La[N]d  Ani[M]als  Bac[K]")

    def get_command(self):
        """
        Get a valid command from the user.
        :return:
        """

        commands = {'a': 'advance',
                    'p': 'plant',
                    'b': 'breed',
                    'r': 'reset',
                    'q': 'quit',
                    's': 'shop',
                    'y': 'report',
                    'l': 'land',
                    'n': 'sell land',
                    'k': 'back',
                    'm': 'sell animal'}

        validCommands = commands.keys()

        letter = '&&&&&&'
        while letter not in validCommands:
            userInput = input('Command: ')
            letter = userInput.lower()

        return commands[letter]

    def help(self, filename, prompt=None):
        """
        Displays instructions.
        :param filename: name of file that contains instructions
        :param prompt: question to ask after to continue program
        :return:
        """
        with open(filename, 'r') as file:
            help = file.read()
        print(help, end='')
        if prompt:
            input('\n' + prompt)
        hi = input("\n\npress <return> to continue")

    def status_bar(self):
        """
        Displays helpful information relating to the farm.
        :return: None
        """
        string = f"Year: {self.__economy.get_year()+1}  Balance: ${self.__farmer.get_money():0.2f}   "
        workers = (self.__farmer.get_farmHands() + (self.__farmer.get_family()-1))
        string += f"Total Workers: {workers}   Plots Owned: {self.__farmer.get_owned_plots()}\n"
        print(string)

    def sell_animals(self):
        """
        asks if they want to sell animals and removes them from that plot.
        :return: None
        """
        whichPlot = self.__farmer.get_plot()
        plotList = self.__farmer.get_totalPlots()
        exists = False
        for plot in plotList:
            if plot.get_type() == 'animal':
                #
                # Makes sure there exists a plot with animals to sell
                #
                exists = True
        if exists:
            while plotList[whichPlot].get_type() != 'animal':
                whichPlot = self.__farmer.get_plot()
            else:
                index = plotList[whichPlot].get_index()
                profit = (plotList[whichPlot].get_count() * self.__animals[index].get_sellValue())
                money = self.__farmer.get_money() + profit
                self.__farmer.set_money(money)
                plotList[whichPlot].reset_animal_plot()
                print(f'Balance: ${self.__farmer.get_money()-profit:0.2f} + ${profit:0.2f} ='
                      f' ${self.__farmer.get_money():0.2f}')
                sleep(2)
        self.show_plots()
        self.status_bar()

    def read_plants(self, filename):
        """Read in all plants from the file and add them to
           the list of plants."""
        with open(filename, 'r') as plantsFile:
            for line in plantsFile:
                type, price, risk, sellValue, lowerLimit, upperLimit = line.split(',')
                type = type.strip()
                price = price.strip()
                risk = risk.strip()
                sellValue = sellValue.strip()
                lowerLimit = lowerLimit.strip()
                upperLimit = upperLimit.strip()
                """if type not in Product.productTypes:
                    raise ValueError(f'{name}: product type cannot be "{type}". Check {filename}.')"""
                if not toolbox.is_number(price):
                    raise ValueError(f'{type}: plant price must be a number. Check {filename}.')
                plant = Plants(type, price, int(risk), sellValue, lowerLimit, upperLimit)
                self.__plants.append(plant)
                #print(self.__plants)

    def read_animals(self, filename):
        """Read in all animals from the file and add them to
           the list of animals."""
        with open(filename, 'r') as animalsFile:
            for line in animalsFile:
                type, price, product, productValue, sellValue = line.split(',')
                type = type.strip()
                price = price.strip()
                product = product.strip()
                productValue = productValue.strip()
                sellValue = sellValue.strip()
                """if type not in Product.productTypes:
                    raise ValueError(f'{name}: product type cannot be "{type}". Check {filename}.')"""
                if not toolbox.is_number(price):
                    raise ValueError(f'{type}: animal price must be a number. Check {filename}.')
                animal = Animals(type, float(price), product, float(productValue), float(sellValue))
                self.__animals.append(animal)

    def reset(self):
        """
        resets the game entirely
        :return: None
        """
        confirm = toolbox.get_boolean("Are you sure you want to reset? All progress will be lost. ")
        if confirm:
            self.__init__()
            self.main()

    def plant(self):
        """
        asks which plot and plants the crop of their choice on the plot
        :return: None
        """
        counter = 0
        for plot in self.__farmer.totalPlots:
            if plot.check_isempty() == False and plot.get_owned() == True:
                counter += 1
        if counter == self.__farmer.get_owned_plots():
            print("You have no empty plots. Advance to next year or buy more plots of land.")
        else:
            whichPlot = self.__farmer.get_plot()
            plotList = self.__farmer.totalPlots
            while not plotList[whichPlot].check_isempty():
                print('You must choose an empty plot.')
                whichPlot = self.__farmer.get_plot()
            else:
                print('==================================================')
                plantNumber = 1
                for plants in self.__plants:
                    string = f'==   {plantNumber} =  {plants.get_type()}  Price: ${plants.get_price():0.2f}  '
                    string += f'Chance of Success: {plants.get_risk()}%'
                    print(string)
                    plantNumber += 1
                print('==================================================')
                numberOfCrops = len(self.__plants)
                plantType = toolbox.get_integer_between(1, numberOfCrops, "Which crop do you want to plant? ", "**ERROR: You must choose a number from 1-4**")
                plant = self.__plants[plantType-1]
                contents = plant.get_type()
                self.__farmer.plant(whichPlot, contents, plantType-1)
                money = self.__farmer.get_money() - plant.get_price()
                if self.__farmer.get_money() < money:
                    oldBalance = self.__farmer.get_money() + money
                    self.__farmer.set_money(oldBalance)
                    print("You don't have enough money to make this purchase.")
                else:
                    self.__farmer.set_money(money)
            self.show_plots()
            self.status_bar()

    def import_animal(self):
        """
        asks which plot and puts the animal of their choice on the plot
        :return: None
        """
        counter = 0
        for plot in self.__farmer.totalPlots:
            if plot.check_isempty() == False and plot.get_owned() == True:
                counter += 1
        if counter == self.__farmer.get_owned_plots():
            print("You have no empty plots. Advance to next year or buy more plots of land.")
        else:
            whichPlot = self.__farmer.get_plot()
            plotList = self.__farmer.totalPlots
            while not plotList[whichPlot].check_isempty():
                print('You must choose an empty plot.')
                whichPlot = self.__farmer.get_plot()
            else:
                print('==================================================')
                animalNumber = 1
                for animal in self.__animals:
                    string = f'==   {animalNumber} =  {animal.get_type()}  Price: {animal.get_price():0.2f}  '
                    string += f' Product: {animal.get_product()}  Earnings: ${animal.get_productValue():0.2f}'
                    print(string)
                    animalNumber += 1
                print('==================================================')
                animalType = toolbox.get_integer_between(1, animalNumber-1, "Which animal do you want to purchase? ", "**ERROR: You must choose a number from 1-4**")
                animal = self.__animals[animalType-1]
                contents = animal.get_type()
                self.__farmer.import_animal(whichPlot, contents, animalType-1)
                money = self.__farmer.get_money() - animal.get_price()
                if self.__farmer.get_money() < money:
                    oldBalance = self.__farmer.get_money() + money
                    self.__farmer.set_money(oldBalance)

                    print("You don't have enough money to make this purchase.")
                else:
                    self.__farmer.set_money(money)
            self.show_plots()
            self.status_bar()

    def advance(self):
        """
        This will advance the simulation forward one year.
        :return: None
        """
        self.__economy.run()
        answer = input("<Press RETURN to continue>")
        self.__economy.determine_success(self.__farmer.totalPlots)
        balance = self.__economy.print_results(self.__farmer.totalPlots, self.__farmer.get_farmHands(), self.__farmer.get_family(), self.__farmer.get_money())
        self.__farmer.set_money(balance)
        answer = input("<Press RETURN to continue>")
        self.__economy.reset_plots(self.__farmer.totalPlots)
        if self.__farmer.get_money() < 0:
            print("You have lost all your money and are now in debt. You are forced to sell your children and farm,")
            print("and you are now on the run from the government, with a warrant for your arrest due to tax")
            print("evasion. Better luck next time.")
            answer = toolbox.get_boolean("Would you like to reset the game?")
            if answer:
                self.reset()
            else:
                command = 'quit'
        else:
            command = ''
            self.show_plots()
            self.status_bar()
        return command


    def print_farmHand_options(self):
        """
        Returns a string that shows the user the fire/hire choice.
        :return: String
        """
        string = '------------------------------'
        string += f'\nTotal Farm Hands: {self.__farmer.get_farmHands()}'
        string += '\nOptions:'
        string += '\n-----------------------------'
        string += '\n1.) Fire'
        string += '\n2.) Hire'
        return string

    def get_family(self):
        """
        Asks the user what family size they want.
        Chosen from three options.
        :return:
        """
        self.print_family()
        choice = toolbox.get_integer_between(1, 3, 'Which family size would you like? ', "**ERROR: You must choose a number from 1-3**")
        if choice == 1:
            family = 2
            farmHands = 3
        elif choice == 2:
            family = 4
            farmHands = 1
        else:
            family = 5
            farmHands = 0
        self.__farmer = Farmer(family, farmHands)

    def print_family(self):
        string = '-----------------------\n'
        string += 'Family Size Options :'
        string += '\n\n1.) No Children'
        string += '\n2.) Two Children'
        string += '\n3.) Three Children'
        string += '\n(Your starting children and farm hands will add up to 3, not counting you,'
        string += '\nto account for the four plots that need to be worked on initially.'
        string += '\neg: option one will give you no children, but will assign you three farm hands.'
        string += '\nEach carry expenses, as you have too provide your family with food, which costs'
        string += "\nmoney, or pay farmhands a salary. It's up to you to decide what you want."
        string += '\n-----------------------\n'
        print(string)

    def show_plots(self):
        """
        displays the plots in aan organized format with the contents
        :return: None
        """
        contentList = []
        plotList = self.__farmer.totalPlots
        for plot in plotList:
            if plot.get_owned() == False:
                plot.set_contents("For Sale")
            contentList.append(plot.get_contents())
        string = f"""
 ________________ ________________ ________________ ________________ ________________
|                |                |                |                |                |        
|                |                |                |                |                |
|       1        |       2        |        3       |        4       |        5       |
|{contentList[0]:^16}|{contentList[1]:^16}|{contentList[2]:^16}|{contentList[3]:^16}|{contentList[4]:^16}|
|                |                |                |                |                |
|________________|________________|________________|________________|________________|
 ________________ ________________ ________________ ________________ ________________
|                |                |                |                |                |        
|                |                |                |                |                |
|       6        |       7        |       8        |       9        |       10       |
|{contentList[5]:^16}|{contentList[6]:^16}|{contentList[7]:^16}|{contentList[8]:^16}|{contentList[9]:^16}|
|                |                |                |                |                |
|________________|________________|________________|________________|________________|
 ________________ ________________ ________________ ________________ ________________
|                |                |                |                |                |        
|                |                |                |                |                |
|       11       |       12       |       13       |       14       |       15       |
|{contentList[10]:^16}|{contentList[11]:^16}|{contentList[12]:^16}|{contentList[13]:^16}|{contentList[14]:^16}|
|                |                |                |                |                |
|________________|________________|________________|________________|________________|
 ________________ ________________ ________________ ________________ ________________
|                |                |                |                |                |        
|                |                |                |                |                |
|       16       |       17       |       18       |       19       |       20       |
|{contentList[15]:^16}|{contentList[16]:^16}|{contentList[17]:^16}|{contentList[18]:^16}|{contentList[19]:^16}|
|                |                |                |                |                |
|________________|________________|________________|________________|________________|
"""
        print(string)



if __name__ == "__main__":
    simulation = Simulation()
    simulation.main()