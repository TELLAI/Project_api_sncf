import csv
import json
import requests
import pprint

depart = 'stop_area:OCE:SA:87686006'
arrivee = 'stop_area:OCE:SA:87722025'
URL = f"https://api.sncf.com/v1/coverage/sncf/journeys?from={depart}&to={arrivee}"


r = requests.get(URL, auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data = json.loads(r.text)

i = 0
def get_increment_key(data, i):
    i += 1
    if type(data) == dict:
        for key, value in dict(data).items():
            print("    " * (i-1) + "|----> " + key + " (dict)")
            get_increment_key(value, i)
    elif type(data) == list:
        for element in list(data):
            print("    " * (i-1) + "|----> " + " (list)")
            get_increment_key(element, i)

get_increment_key(data, i)

"""
def get_json(data, i=0):
    i += 1
    if type(data) == dict:
        for key, value in dict(data).items():
            print("    "*(i-1)+"|--->", key, 'dict')
            get_json(value,i)
    elif type(data) == list:
        print("list")
        if len(list(data)) > 0:
            get_json(list(data)[0],i)
"""