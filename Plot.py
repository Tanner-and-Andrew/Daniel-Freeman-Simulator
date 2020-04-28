import toolbox
from Plants import Plants
from Animals import Animals



class Plot(object):

    def __init__(self):
        self.__type = type
        #animal or crop
        self.__contents =  contents
        #specific crop
        self.__count = 0
        self.__owned = False
        self.__isempty = True
        self.__plants = []
        self.read_plants('plants.csv')
        self.__animals = []
        self.read_animals('animals.csv')

    def read_plants(self, filename):
        """Read in all plants from the file and add them to
           the list of plants."""
        with open(filename, 'r') as plantsFile:
            for line in plantsFile:
                type, price, risk, sellValue = line.split(',')
                type = type.strip()
                price = price.strip()
                risk = risk.strip()
                sellValue = sellValue.strip()
                """if type not in Product.productTypes:
                    raise ValueError(f'{name}: product type cannot be "{type}". Check {filename}.')"""
                if not toolbox.is_number(price):
                    raise ValueError(f'{type}: plant price must be a number. Check {filename}.')
                plant = Plants(type, float(price), int(risk), float(sellValue))
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