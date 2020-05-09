import random
from Farmer import Farmer
class Economy(object):

    def __init__(self, animals, plants):
        self.__animals = animals
        self.__plants = plants
        self.__year = 1849
        self.__previous_farm_report = ''
        #self.original_report()
        """self.__crop1 = plants[0]
        self.__crop2 = crop2
        self.__crop3 = crop3
        self.__crop4 = crop4
        self.__cows = cows
        self.__sheep = sheep
        self.__chickens = chickens
        self.__goats = goats"""

    def original_report(self):
        string = "################################################################################################\n"
        string += f"                               ANNUAL FARM REPORT: {self.__year}\n"
        string += "################################################################################################\n\n"
        string += f"\n**** Plants ****\n\n"
        for plant in self.__plants:
            string += f"{plant.get_type()}: ${plant.get_sellValue():0.2f} per bushel\n\n"
        string += f"**** Animals ****\n\n"
        for animal in self.__animals:
            string += f"{animal.get_type()}-\n     {animal.get_product()}: ${animal.get_productValue():0.2f} per pound"
            string += f"\n     Price per {animal.get_type()}: ${animal.get_sellValue():0.2f}\n"
        self.__previous_farm_report = string
        print(string)

    def get_year(self):
        return self.__year

    def run(self):
        self.__year += 1
        self.randomize_plants()
        #self.randomize_animals()
        self.print_farm_report()
        #success = self.determine_success()
        #self.print_results(success)

    def randomize_plants(self):
        for plant in self.__plants:
            sellValue = plant.get_sellValue()
            lowerLimit = plant.get__lowerLimit()
            upperLimit = plant.get__upperLimit()
            sellValue = random.choice([sellValue-(0.15*sellValue), sellValue, sellValue+(0.15*sellValue)])
            if sellValue < float(lowerLimit):
                sellValue = lowerLimit
            if sellValue > upperLimit:
                sellValue = upperLimit
        plant.set_sellValue(sellValue)

    def print_farm_report(self):
        #self.__year += 1
        string = "################################################################################################\n"
        string += f"                               ANNUAL FARM REPORT: {self.__year}\n"
        string += "################################################################################################\n\n"
        string += f"\n**** Plants ****\n\n"
        for plant in self.__plants:
            #string += f"\nPlants\n--------\n"
            string += f"{plant.get_type()}: ${plant.get_sellValue():0.2f} per bushel\n\n"
        string += f"**** Animals ****\n\n"
        for animal in self.__animals:
            #string += f"\nAnimals\n---------\n"
            string += f"{animal.get_type()}-\n     {animal.get_product()}: ${animal.get_productValue():0.2f} per pound"
            string += f"\n     Price per {animal.get_type()}: ${animal.get_sellValue():0.2f}\n"
        self.__previous_farm_report = string
        print(string)

    def determine_success(self, totalPlots):
        #ownedPlots = Farmer.get_totalPlots_length()
        for plot in totalPlots:
            if plot.get_owned():
                if plot.check_isempty() == False:
                    if plot.get_type() == 'crop':
                        plant = self.__plants[plot.get_index()]
                        number = random.randint(1, 100)
                        if number >= plant.get_risk():
                            plot.set_success(False)

    def print_results(self, totalPlots):
        string = "################################################################################################\n"
        string += f"                               YOUR FARM RESULTS: {self.__year}\n"
        string += "################################################################################################\n\n"
        string += f"\n**** Plants ****\n\n"
        totalPlantProfit = 0
        for plot in totalPlots:
            if plot.get_owned():
                if plot.check_isempty() == False:
                    if plot.get_type() == 'crop':
                        plant = self.__plants[plot.get_index()]
                        string += f"{plant.get_type()}:\n"
                        if plot.get_success():
                                string += f"     ${plant.get_sellValue():0.2f} per bushel \n\n"
                                plantProfit = (plant.get_sellValue()*40)
                                string += f"     ${plant.get_sellValue():0.2f} x {plot.get_count()} bushels         =      ${plantProfit:0.2f}\n\n"
                                totalPlantProfit += plantProfit
                        else:
                            string += "FAILED\n   *$0 earned\n\n"
        string += f"**** Animals ****\n\n"
        totalAnimalProfit = 0
        for plot in totalPlots:
            if plot.get_owned():
                if plot.check_isempty() == False:
                    if plot.get_type() == 'animal':
                        animal = self.__animals[plot.get_index()]
                        string += f"{animal.get_type()}-\n     {animal.get_product()}: ${animal.get_productValue():0.2f} per pound\n"
                        pounds = plot.get_count()*2
                        string += f"     Pounds Produced: {pounds}\n"
                        animalProfit = (pounds) * (animal.get_productValue())
                        string += f"     Revenue : {pounds}lbs x ${animal.get_productValue():0.2f}     =      ${animalProfit:0.2f}"
                        totalAnimalProfit += animalProfit

        print(string)










    def get_previous_report(self):
        return self.__previous_farm_report




