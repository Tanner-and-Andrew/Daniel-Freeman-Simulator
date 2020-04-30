import toolbox
from Plants import Plants
from Animals import Animals



class Plot(object):

    def __init__(self):
        self.__type = type
        #animal or crop
        self.__contents = ''
        #specific crop
        self.__count = 0
        self.__owned = False
        self.__isempty = True
        self.__plants = []
        self.read_plants('plants.csv')
        self.__animals = []
        self.read_animals('animals.csv')

    def get_type(self):
        return self.__type

    def get_contents(self):
        return self.__contents

    def check_isempty(self):
        return self.__isempty

