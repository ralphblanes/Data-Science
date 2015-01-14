__author__ = 'ralphblanes'
import json
import requests
import csv
import pandas
import pprint
from collections import OrderedDict
import time

def api_getUrl_topArtists(country_name):
    """

    :param country_name: The country which you wish to query
    :return: the new url
    """

    url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=FORMAT_ME_HARDER&api_key=7d095480f44e3853bc45b6914c635b75&format=json"
    url = url.replace("FORMAT_ME_HARDER",country_name)
    # print("URL generated is: %s" % url)
    return url

def get10TopArtists(country_name):
    """

    :param country_name: The country being queried
    :return:
     top_artists<list<(String,Int)>>, country<String>, where top_artists returns a list with
        an Artist's name and its number of listeners
    """




    # Loading the API's url
    url = api_getUrl_topArtists(country_name)
    data = requests.get(url).text
    data = json.loads(data)
    top_artists = []



    #This makes a tuple that contain an Artist's name and it's number of listeners
    for artist_rank in range(0, 10):
        top_artists.append((data["topartists"]["artist"][artist_rank]["name"],
                            data["topartists"]["artist"][artist_rank]["listeners"]))

    return top_artists


def main():

    #Getting all countries in the world and setting them as keys for test_cases
    test_cases = {}
    country_data = pandas.read_csv("Data/Last_Fm/wikipedia-iso-country-codes.csv")
    countries = country_data["country name"]

    for country_name in countries:
        country_name = country_name.lstrip().lower()
        test_cases[country_name] = get10TopArtists(country_name)

    for key in test_cases:
        print("Top 10 artists in %s :" % key)
        print("")
        for artist in test_cases[key]:
            print("%s has %s followers" % (artist[0],artist[1]))
        print("")


start_time = time.time()

main()

print("--- %s seconds ---" % (time.time() - start_time))