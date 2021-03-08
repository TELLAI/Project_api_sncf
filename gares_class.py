
import csv
import json
import requests
import pprint
import datetime
import os

class Gares:                    # classe Gares afin de créer une fiche technique de chaque gare */

    def __init__(self, name):
        self.pages = 0
        self.URL = 'https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000'
        self.token = ('75cad487-3e50-4835-a3b5-299fc791dcd5', '')
        self.id = None
        self.name_gare = name
        self.data = []
        self.dict_names_id = {}
        self.json_data = 'gares_keys.json'

    def fct_get_name_id(self):
        data_1 = self.data['stop_areas']
        for i in data_1:
            name = i['name']
            self.dict_names_id[name] = i['id']

        with open(self.json_data, 'w') as file:
            json.dump(self.dict_names_id, file)
            
    def fct_requet(self):
        print("slt")
        if(os.path.getsize(self.json_data) == 0):
            print("slt")
            while(self.pages < 5):
                print("slt")
                read = requests.get(self.URL + "&start_page=" + str(self.pages), auth=self.token)
                self.data = json.load(read.text)
                self.fct_get_name_id()
                self.pages += 1



    # def fct_load_search(self):
    #     while(self.pages < 5):
    #         self.fct_requet()
    #         self.fct_get_name_id()

    def fct_get_id(self):
        with open(self.json_data, 'r') as file2:
            self.dict_names_id = json.load(file2)

        for i in self.dict_names_id.keys():
            if i == self.name_gare:
                self.id = self.dict_names_id[i]

gare_depart = Gares('Paris-Gare-de-Lyon')
gare_arrviee = Gares('Lyon-Perrache')
gare_depart.fct_requet()
gare_depart.fct_get_id()
gare_arrviee.fct_requet()
gare_arrviee.fct_get_id()
print(gare_depart.id)
print(gare_depart.name_gare)
print(gare_depart.pages)