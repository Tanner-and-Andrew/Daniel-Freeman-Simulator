from Farmer import Farmer
from Economy import Economy
from Plot import Plot


class Simulation(object):

    def __init__(self):
        self.__plotList = []
        self.__menu = 'main'

    def main(self):
        command = 'help'
        self.get_family()
        while command != 'quit';
            if command == 'help':
                self.help('farmhelp.txt')
            elif command == 'advance':
                economy.advance()
            elif command == 'plant':
                farmer.plant()
            elif command == 'breed':
                farmer.breed()
            elif command == 'shop':
                self.__menu = 'shop'
                self.get_menu()
            elif command == 'reset':
                pass
            elif command == 'farmhands':
                self.edit_farmhands()
            elif command == 'land':

            elif command == 'change-display':
                self.change_graphics(parameter)
            elif command == 'save':
                self.save(parameter, './worlds/')
            elif command == 'load':
                self.load(parameter, './worlds/')
            elif command == 'more':
                self.__menu = 'more'
            elif command == 'back':
                self.__menu = 'main'
            elif command == 'world-type':
                self.get_geometry()
            elif command == 'change-rules':
                self.change_rules(parameter)
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
                    'l': 'land',


                    'o': 'load',
                    'h': 'help',
                    '?': 'help',
                    'g': 'change-display',
                    'u': 'change-rules',
                    'm': 'more',
                    'b': 'back',
                    'w': 'world-type',
                    'q': 'quit'}

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
        if answer = 'h':
            farmer.hire_farmHands()
        if answer = 'f':
            farmer.fire_farmHands()