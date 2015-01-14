import math

__author__ = 'ralphblanes'
import pandas
def find_std_deviation():
    salaries_df = pandas.read_excel("/Users/ralphblanes/Documents/Data Science Nanodegree/Project 1/Data/Statistics/Lesson 4- Variability - Calculate SD for salary in social network sample - Shared.xlsx")
    mean = salaries_df["Salary"].mean()
    print("The mean is %f" %mean)
    sqd_mean_dev = []
    for salary in  salaries_df["Salary"]:
        sqd_mean_dev.append(math.pow(salary - mean,2))
    variance = sum(sqd_mean_dev)/(len(sqd_mean_dev))
    print("The variance is %f" %variance)
    std_deviation = math.sqrt(variance)
    print("The standard deviation is %f" %std_deviation)

find_std_deviation()