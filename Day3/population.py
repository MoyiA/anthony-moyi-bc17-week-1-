import requests

#requests to get the population of a counrty in the world as dictated by user input 

def country_population():

    country = input()
    country = country.lower()
    country = country.capitalize()

    url = "http://api.population.io:80/1.0/population/{}/2015-12-24/".format(country)

    try:
        data = requests.get(url)
        if data.status_code != 200:
            print(data.status_code)

        for content in data.json():
            print(data.json()[content])
    except Exception:
        print("Error occurred")

country_population()
