from statistics import *
from scipy.stats import kurtosis
from file_reader_skill_migration import SkillMigrationFileReader

# create a class that will allow to refer to methods which can will perform calculations in a main file


class Statcalc:

    def __init__(self):
        self.reader = SkillMigrationFileReader("skill_migration.xlsx")
        self.entire_table = self.reader.print_all_cell_data()

    def start_story(self):
        # A list of tuples. Each tuple: (country, skill, migration no)
        print(self.entire_table[1:])

    # create a method that loops through the migration numbers column and stores values in a list
    def create_and_store_list(self):
        data_list = []
        for item in self.entire_table[1:]:
            migration_vector = item[2]
            data_list.append(migration_vector)
        return data_list

    def top_10(self):
        # Loop through the data to get top 10 countries and skills imigrated
        for item in self.entire_table[1:]:
            if item[2] > 3000:
                print(item[0] + " || " + item[1] + " || " + str(item[2]))

    def bottom_10(self):
        # Loop through the data to get the most emigrating skills and origin of these skills (countries)
        for item in self.entire_table[1:]:
            if item[2] < -5600:
                print(item[0] + " || " + item[1] + " || " + str(item[2]))

    def find_average(self, data_list):
        return mean(data_list)

    def find_stdev(self, data_list):
        return stdev(data_list, xbar=None)

    def find_kurtosis(self, data_list):
        return kurtosis(data_list)











