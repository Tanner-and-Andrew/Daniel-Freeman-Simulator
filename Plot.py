import toolbox
from Plants import Plants
from Animals import Animals



class Plot(object):

    def __init__(self):
        self.__type = type
        #animal or crop
        self.__contents = 'EMPTY'
        #specific crop
        self.__count = 0
        self.__owned = False
        self.__isempty = True
        #self.__plants = []
        #self.read_plants('plants.csv')
        #self.__animals = []
        #self.read_animals('animals.csv')

    def set_plant(self, plant):
        self.__contents = plant
        self.__type = 'crop'
        self.__isempty = False

    def set_animal(self, animal):
        self.__contents = animal
        self.__type = 'animal'
        self.__isempty = False

    def set_owned(self):
        self.__owned = True

    def get_type(self):
        return self.__type

    def get_contents(self):
        return self.__contents

    def get_owned(self):
        return self.__owned

    def set_contents(self, contents):
        self.__contents = contents

    def check_isempty(self):
        return self.__isempty

    def __str__(self):
        print(f"""  
 ________________
|                |
|                | 
|     {self.__contents}      |
|                | 
|                |
|________________| 
           """)

    def print_plot(self):
        return f"""  
 ________________
|                |
|                | 
|     {self.__contents}      |
|                | 
|                |
|________________| 
           """


