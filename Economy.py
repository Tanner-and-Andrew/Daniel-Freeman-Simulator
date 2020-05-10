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
            if float(sellValue) < float(lowerLimit):
                sellValue = lowerLimit
            if float(sellValue) > float(upperLimit):
                sellValue = float(upperLimit)
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

    def print_results(self, totalPlots, farmhands, family, balance):
        string = "################################################################################################\n"
        string += f"                               YOUR FARM RESULTS: {self.__year}\n"
        string += "################################################################################################\n"
        string += f"**** Plants ****\n\n"
        totalPlantProfit = 0
        for plot in totalPlots:
            if plot.get_owned():
                if plot.check_isempty() == False:
                    if plot.get_type() == 'crop':
                        plant = self.__plants[plot.get_index()]
                        string += f"{plant.get_type()}:\n"
                        if plot.get_success():
                                string += f"     ${plant.get_sellValue():0.2f} per bushel\n"
                                plantProfit = (plant.get_sellValue()*100)
                                string += f"     ${plant.get_sellValue():0.2f} x {plot.get_count()} bushels         =      ${plantProfit:0.2f}\n\n"
                                totalPlantProfit += plantProfit
                        else:
                            string += "   FAILED\n   *$0 earned\n\n"
        string += f"**** Animals ****\n\n"
        totalAnimalProfit = 0
        for plot in totalPlots:
            if plot.get_owned():
                if plot.check_isempty() == False:
                    if plot.get_type() == 'animal':
                        animal = self.__animals[plot.get_index()]
                        string += f"{animal.get_type()}:\n     {animal.get_product()}: ${animal.get_productValue():0.2f} per lb\n"
                        pounds = plot.get_count()*2
                        string += f"     Produced: {pounds} lbs\n"
                        animalProfit = (pounds) * (animal.get_productValue())
                        string += f"     Revenue : {pounds} lbs x ${animal.get_productValue():0.2f}     =      ${animalProfit:0.2f}\n"
                        totalAnimalProfit += animalProfit
        string += "################################################################################################\n\n"
        string += f"**** Expenses ****\n"
        string += f"Providing for family = $5 per Family Member\nPaying Farmhands = $7 per Farmhand\n"
        familyCost = (family*5)
        string += f"$5.00 x {family} Family Members    =    ${familyCost:0.2f}\n"
        farmhandCost = (farmhands * 7)
        string += f"$7.00 x {farmhands} Farmhand(s)    =    ${farmhandCost:0.2f}\n\n"
        string += "################################################################################################\n"
        string += f"**** Totals ****\n\n"
        totalRevenue = totalAnimalProfit + totalPlantProfit
        totalExpenses = farmhandCost + familyCost
        string += f"                       Total Revenue     =     ${totalRevenue:0.2f}\n"
        string += f"                            Expenses     =     ${totalExpenses:0.2f}\n\n"
        moneyEarned = totalRevenue-totalExpenses
        string += f"                     Yearly Earnings     =     ${moneyEarned:0.2f}\n"
        balance = balance + moneyEarned
        string += f"                    Updated Balance      =     ${balance:0.2f}\n"
        string += "################################################################################################"
        print(string)
        return balance

    def reset_plots(self, totalPlots):
        for plot in totalPlots:
            plot.reset_plant_plot()











    def get_previous_report(self):
        return self.__previous_farm_report




