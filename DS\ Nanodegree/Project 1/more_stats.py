__author__ = 'ralphblanes'
import scipy.stats
import pandas

def compare_averages(path):
    #Reading data from the path
    baseball_df = pandas.read_csv(path)

    #Splitting onto two dataframes biased on batting hands
    left_averages = baseball_df[baseball_df["handedness"] == "L"]["avg"]
    right_averages = baseball_df[baseball_df["handedness"] == "R"]["avg"]

    ##We're doing welch's Ttest
    test_info = scipy.stats.ttest_ind(left_averages,right_averages, equal_var = False)

    result = (test_info[1] >= 0.05)
    return (result,test_info)


print compare_averages("./Data/Statistics/baseball_data.csv")
