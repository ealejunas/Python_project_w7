from statistics_calculations import *

input("Hi all, lets do the statistical analysis!")
input("Data structure looks like this: ")
input()
stat_class = Statcalc()   # 1 instance
stat_class.start_story()   # 2 call each method

input()
input("Store data as a list and perform analysis: ")
x = stat_class.create_and_store_list()
print(x)

input()
input("Top 10 countries in skill imigration: ")
input()
stat_class.top_10()

input()
print("Lowest 10 countries in skill emigration: ")
input()
stat_class.bottom_10()

input()
print("Migration is", round(stat_class.find_average(x), 0), " people (in 000s) on average in all countries, meaning that we have an OUTFLOW of skills!")
input()
print("However, the data is very volatile, due to large standard deviation, that reaches", round(stat_class.find_stdev(x), 2), ".")
input()
print("What is more, we can have a look at a measure called kurtosis, that might help with the study of normal distribution.")
input()
print("Kurtosis: ", round(stat_class.find_kurtosis(x), 2))
input()
print("This indicates that the data does not follow a normal distribution, therefore any other distributions shall be considered.")
input()
input("Thank you!")
input("Do you have any questions?")





