import random
class Economy(object):

    def __init__(self, animals, plants):
        self.__animals = animals
        self.__plants = plants
        self.__year = 1849
        """self.__crop1 = plants[0]
        self.__crop2 = crop2
        self.__crop3 = crop3
        self.__crop4 = crop4
        self.__cows = cows
        self.__sheep = sheep
        self.__chickens = chickens
        self.__goats = goats"""

    def run(self):
        self.randomize_plants()
        self.randomize_animals()
        self.print_farm_report()
        self.print_results()

    def randomize_plants(self):
        for plant in plants:
            sellValue = Plants.get_sellValue()
            lowerLimit = Plants.get___lowerLimit()
            upperLimit = Plants.get_upperLimit()
            sellValue = random.choice([sellValue-(0.15*sellValue), sellValue, sellValue+(0.15*sellValue)])
            if sellValue < lowerLimit:
                sellValue = lowerLimit
            elif sellValue > upperLimit:
                sellValue = upperLimit
        Plants.set_sellValue(sellValue)

    def print_farm_report(self):
        self.__year += 1
        string = "################################################################################################\n"
        string += f"                               ANNUAL FARM REPORT: {self.__year}\n"
        string += "################################################################################################\n\n"
        for plant in self.__plants:
            string += f"{Plants.get_type()}: ${Plants.get_sellValue()} per bushel\n\n"
        for animal in self.__animals:
            string += f"{Animals.get_type()}-\n     {Animals.get_product()}: ${Animals.get_productValue()} per pound"
            string += f"\n     Price per {Animals.get_type()}: ${Animals.get_sellValue()}"
        print(string)






