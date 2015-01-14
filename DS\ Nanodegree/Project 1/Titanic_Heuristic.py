__author__ = 'ralphblanes'
import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):
    '''
    In this exercise, we will perform some rudimentary practices similar to those of
    an actual data scientist.

    Part of a data scientist's job is to use her or his intuition and insight to
    write algorithms and heuristics. A data scientist also creates mathematical models
    to make predictions based on some attributes from the data that they are examining.

    We would like for you to take your knowledge and intuition about the Titanic
    and its passengers' attributes to predict whether or not the passengers survived
    or perished. You can read more about the Titanic and specifics about this dataset at:
    http://en.wikipedia.org/wiki/RMS_Titanic
    http://www.kaggle.com/c/titanic-gettingStarted

    In this exercise and the following ones, you are given a list of Titantic passengers
    and their associated information. More information about the data can be seen at the
    link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data.

    For this exercise, you need to write a simple heuristic that will use
    the passengers' gender to predict if that person survived the Titanic diaster.

    You prediction should be 78% accurate or higher.

    Here's a simple heuristic to start off:
       1) If the passenger is female, your heuristic should assume that the
       passenger survived.
       2) If the passenger is male, you heuristic should
       assume that the passenger did not survive.

    You can access the gender of a passenger via passenger['Sex'].
    If the passenger is male, passenger['Sex'] will return a string "male".
    If the passenger is female, passenger['Sex'] will return a string "female".

    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survived or 0 otherwise.

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0

    You can also look at the Titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        #Checking age
        p_class = passenger["Pclass"]
        x,y = "adult","child"
        if passenger["Age"] != 0:
            age = x if passenger["Age"] >= 18 else y
        #Checking fare
        fare = passenger["Fare"]
        sex = passenger["Sex"].lower()
        if fare < 10:
            ticketPrice = "low"
        elif 10 <= fare <= 20:
            ticketPrice = "medium"
        elif 10 <= fare <= 20:
            ticketPrice = "high"
        elif fare > 30:
            ticketPrice = "very high"
       #Checking sex
       #Updating predictions
        if ticketPrice == "low" and (sex == "female" and age == "child"):
            predictions[passenger_id] = 1
        #Medium price
        elif ticketPrice == "medium":
            if sex == "female":
                predictions[passenger_id] = 1
            elif sex == "male" and age == "child":
                predictions[passenger_id] = 1
        #High price
        elif ticketPrice == "high":
            if sex == "female" and p_class !=3:
                predictions[passenger_id] = 1
            elif sex == "male" and (age == "child" and p_class == 2):
                predictions[passenger_id] = 1
        #Very high price
        elif ticketPrice == "very high":
            if sex == "female" and p_class !=3:
                predictions[passenger_id] = 1
            elif sex == "male" and ((age == "child" and p_class !=3)):
                predictions[passenger_id] = 1

        else:
            predictions[passenger_id] = 0



    return predictions

def compareResults(filepath, predictionList):
    survivedList = {}
    correct_count = 0
    df = pandas.read_csv(filepath)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']
        survivedList[passenger_id] = passenger["Survived"]
    for key in predictionList:
        print survivedList[key] == predictionList[key]
        if survivedList[key] == predictionList[key]:
            correct_count += 1
    return float(correct_count)/len(predictionList)

predictions = simple_heuristic('Data/titanic_data.csv')
correct_percentage = compareResults('Data/titanic_data.csv', predictions)
print correct_percentage