from Farmer import Farmer
from Economy import Economy
from Plot import Plot
import toolbox


class Simulation(object):

    def __init__(self):
        self.__plotList = []
        self.__menu = 'main'
        self.__farmer = None

    def main(self):
        command = 'help'
        self.get_family()
        while command != 'quit':
            if command == 'help':
                self.help('farmhelp.txt')
            elif command == 'advance':
                economy.advance()
            elif command == 'plant':
                self.__farmer.plant()
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
            command, parameter = self.get_command()

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


    def advnace(self):
        """
        This will advance the simulation forward one year.
        :return: None
        """
        pass

    def edit_farmhands(self):
        #hire or fire
        if answer == 'h':
            self.__farmer.hire_farmHands()
        if answer == 'f':
            self.__farmer.fire_farmHands()

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
        string = '-----------------------'
        string += 'Family Size Options:'
        string += '\n\n1.) No Children'
        string += '\n2.) Two Children'
        string += '\n3.) Three Children'
        string += '-----------------------'
        return string


