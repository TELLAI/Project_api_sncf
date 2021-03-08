import csv
import json
import requests
import pprint
import datetime

class Travel:                     # class travel afin d'accéder aux endpoint d'un trajet et recuperer des infos
    
    def __init__(self, id_depart, id_arrivee, name_depart, name_arrivee):
        self.URL = f"https://api.sncf.com/v1/coverage/sncf/journeys?"
        self.id_depart = id_depart
        self.id_arrivee = id_arrivee
        self.token = ('d402691b-69c5-48e6-b658-9f9be6140b8a','')
        self.name = name_depart + "===>" + name_arrivee
        self.nb_arret = None
        self.list_arret = []
        self.list_arrivee = []
        self.list_depart = []
        self.list_attente = []
        self.data_search = []

    def fct_request(self):
        r = requests.get(f"{self.URL}from={self.id_depart}&to={self.id_arrivee}, auth={self.token}")
        data = json.loads(r.text)
        return data
        
    def fct_zoom(self, data_1, list_keys):
        for count, i in enumerate (list_keys):
            if (type(data_1)) == dict:
                for key, value in data_1.items():
                    if key == i and key != list_keys[len(list_keys) - 1]:
                        list_keys = list_keys[(count + 1):]
                        self.fct_zoom(value, list_keys)
                    elif key == i and key == list_keys[len(list_keys) - 1]:
                        self.data_search.append(data_1[key])
            elif (type(data_1)) == list:
                for element in data_1:
                    list_keys = list_keys[count:]
                    self.fct_zoom(element, list_keys)
            else:
                print("Erreur")
        return list(set(self.data_search))


my_travel = Travel('stop_area:OCE:SA:87686006', 'stop_area:OCE:SA:87722025', "Paris", "Lyon")
list_keys_1 = ["journeys", "sections", "stop_date_times", "stop_point", "departure_date_time"]
list_keys_2 = ["journeys", "sections", "stop_date_times", "stop_point", "name"]
list_keys_3 = ["journeys", "sections", "stop_date_times", "stop_point", "arrival_date_time"]

my_travel.list_arret = my_travel.fct_zoom(my_travel.fct_request(), list_keys_2)
my_travel.list_arrivee = my_travel.fct_zoom(my_travel.fct_request(), list_keys_3)
my_travel.list_depart = my_travel.fct_zoom(my_travel.fct_request(), list_keys_1)