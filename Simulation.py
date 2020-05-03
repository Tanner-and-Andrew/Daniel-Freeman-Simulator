from Farmer import Farmer
from Economy import Economy
from Plants import Plants
from Animals import Animals
import toolbox


class Simulation(object):

    def __init__(self):
        self.__plotList = []
        self.__menu = 'main'
        self.__farmer = None
        self.__plants = []
        self.read_plants('plants.csv')
        self.__animals = []
        self.read_animals('animals.csv')
        self.__economy = Economy(self.__animals, self.__plants)

    def main(self):
        #self.help()
        command = ''
        self.get_family()
        while command != 'quit':
            if command == 'help':
                self.help('farmhelp.txt')
            elif command == 'advance':
                self.__economy.advance()
            elif command == 'plant':
                self.plant()
            elif command == 'breed':
                self.__farmer.breed()
            elif command == 'shop':
                self.__menu = 'shop'
                self.get_menu()
            elif command == 'reset':
                pass
            elif command == 'farmhands':
                self.edit_farmhands()
            elif command == 'land':
                pass
            self.get_menu()
            self.__menu = 'main'
            command = self.get_command()

    def get_menu(self):
        """
        Displays the menu.
        :return:
        """
        if self.__menu == 'main':
            print("[A]dvance  [P]lant  [B]reed  [S]hop  [R]eset  [Q]uit")
        if self.__menu == 'shop':
            print("Purchase: [F]armhands [L]and")

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
                    'f': 'farmhands',
                    'l': 'land',}

        validCommands = commands.keys()

        letter = '&&&&&&'
        while letter not in validCommands:
            userInput = input('Command: ')
            letter = userInput[0].lower()

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
                upperLimit = upperLimit.strip
                """if type not in Product.productTypes:
                    raise ValueError(f'{name}: product type cannot be "{type}". Check {filename}.')"""
                if not toolbox.is_number(price):
                    raise ValueError(f'{type}: plant price must be a number. Check {filename}.')
                plant = Plants(type, price, int(risk), sellValue, lowerLimit, upperLimit)
                self.__plants.append(plant)

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


    def plant(self):
        whichPlot = self.__farmer.get_plot()
        string = '=================================================='
        plantNumber = 1
        for plants in self.__plants:
            string = f'==   {plantNumber}=  {plants.get_type()}  Price:{plants.get_price()}  '
            string += f'Chance of Success: {plants.get_risk()}%'
            print(string)
            plantNumber += 1
        plantType = toolbox.get_integer_between(1, plantNumber, "Which crop do you want to plant? ")
        self.__farmer.plant(whichPlot, plantType)

    def advance(self):
        """
        This will advance the simulation forward one year.
        :return: None
        """
        self.__economy.run()

    def edit_farmhands(self):
        self.print_farmHand_options()
        answer = toolbox.get_integer_between(1, 2, "Which option? ")
        if answer == 2:
            self.__farmer.hire_farmHands()
        if answer == 1:
            self.__farmer.fire_farmHands()

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
        choice = toolbox.get_integer_between(1, 3, 'Which family size would you like? ')
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
        string += '\neg: option one will give you no children, but will assign you three farm hands.)'
        string += '\n-----------------------\n'
        print(string)


if __name__ == "__main__":
    simulation = Simulation()
    simulation.main()