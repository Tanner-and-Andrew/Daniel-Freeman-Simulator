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
        self.__index = 0
        self.__success = True
        #self.__plants = []
        #self.read_plants('plants.csv')
        #self.__animals = []
        #self.read_animals('animals.csv')

    def reset_plot(self):
        self.__init__()

    def set_plant(self, string, index):
        self.__contents = string
        self.__type = 'crop'
        self.__isempty = False
        self.__count = 100
        self.__index = index

    def set_animal(self, string, index):
        self.__contents = string
        self.__type = 'animal'
        self.__isempty = False
        self.__count = 10
        self.__index =  index

    def set_owned(self, para):
        self.__owned = para

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

    def get_index(self):
        return self.__index

    def get_count(self):
        return self.__count

    def get_success(self):
        return self.__success

    def set_success(self, parameter):
        self.__success = parameter

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


