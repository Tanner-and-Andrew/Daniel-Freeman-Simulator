class Plot(object):

    def __init__(self):
        self.__type = type
        #animal or crop
        self.__contents =  contents
        #specific crop
        self.__count = 0
        self.__owned = False
        self.__isempty = True
        self.__animals = []
        self.__plants = []

    def read_animals(self, filename):
        """Read in all products from the file and add them to
           the list of products."""
        with open(filename, 'r') as productsFile:
            for line in productsFile:
                name, type, price = line.split(',')
                name = name.strip()
                type = type.strip()
                price = price.strip()
                if type not in Product.productTypes:
                    raise ValueError(f'{name}: product type cannot be "{type}". Check {filename}.')
                if not toolbox.is_number(price):
                    raise ValueError(f'{name}: product price must be a number. Check {filename}.')
                product = Product(name, type, float(price))
                self.__products.append(product)
