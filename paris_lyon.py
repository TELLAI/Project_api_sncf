import csv
import json
import requests
import pprint
import datetime

depart = 'stop_area:OCE:SA:87686006'
arrivee = 'stop_area:OCE:SA:87722025'
URL = f"https://api.sncf.com/v1/coverage/sncf/journeys?from={depart}&to={arrivee}"


r = requests.get(URL, auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data = json.loads(r.text)
with open('journeys.json', 'w') as file:
    json.dump(r.text, file)

print(type(data))
list_arret = []
list_arrivee = []
list_depart = []
list_attente = []
for i in data.keys():
    if i == "journeys":
        data_links = data[i]
        for i in data_links:
            dict_vrac = i
            for key in dict_vrac.keys():
                if key == "sections":
                    liste_info = dict_vrac[key]
                    for j in liste_info:
                        dict_info = j
                        for k in dict_info.keys():
                            if k == "stop_date_times":
                                list_stop_point = dict_info[k]
                                for y in list_stop_point:
                                    dict_arret = y
                                    for key in dict_arret.keys():
                                        if key == "arrival_date_time":
                                            arrivee=datetime.datetime.strptime(dict_arret[key], "%Y%m%dT%H%M%S")
                                            arrivee_s = str(arrivee)
                                            list_arrivee.append(arrivee_s)
                                        if key == "departure_date_time":
                                            depart=datetime.datetime.strptime(dict_arret[key], "%Y%m%dT%H%M%S")
                                            depart_s = str(depart)
                                            list_depart.append(depart_s)
                                            diff = str(depart - arrivee) 
                                            list_attente.append(diff)
                                        if key == "stop_point":
                                            dict_stop_point = dict_arret[key]
                                            for key in dict_stop_point.keys():
                                                if key == 'label':
                                                    list_arret.append(dict_stop_point[key])

result = zip(list_arret, list_arrivee, list_depart, list_attente)
result_set = set(result)

with open('paris_lyon.csv', 'w') as file:
    fieldnames = ["Nom_gares_arrêt", "Date d'arrivee", "Date de départ", "temps d'arrêt en gare"]

    csv_file = csv.writer(file, delimiter='\t')

    csv_file.writerow(fieldnames)

    for i in result_set:
        csv_file.writerow([i])