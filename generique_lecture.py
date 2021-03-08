import csv
import json
import requests
import pprint

depart = 'stop_area:OCE:SA:87686006'
arrivee = 'stop_area:OCE:SA:87722025'
URL = f"https://api.sncf.com/v1/coverage/sncf/journeys?from={depart}&to={arrivee}"


r = requests.get(URL, auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data = json.loads(r.text)
"""
def fct_dict(data_1, key):
    for i in data_1.keys():
        if i == key:
            data_2 = data_1[key]
            return (data_2)

def fct_list(data_1):
    for i in data_1:
        data_2 = i
        return (data_2)
"""
list_keys_1 = ["journeys", "sections", "stop_date_times", "stop_point", "departure_date_time"]
list_keys_2 = ["journeys", "sections", "stop_date_times", "stop_point", "name"]
list_keys_3 = ["journeys", "sections", "stop_date_times", "stop_point", "arrival_date_time"]
data_search = []

def fct_zoom(data_1, list_keys):
    
    for count, i in enumerate (list_keys):
        if (type(data_1)) == dict:
            for key, value in data_1.items():
                if key == i and key != list_keys[len(list_keys) - 1]:
                    list_keys = list_keys[(count + 1):]
                    fct_zoom(value, list_keys)
                elif key == i and key == list_keys[len(list_keys) - 1]:
                    data_search.append(data_1[key])
        elif (type(data_1)) == list:
            for element in data_1:
                list_keys = list_keys[count:]
                fct_zoom(element, list_keys)
        else:
            print("Erreur")
    return list(set(data_search))

print(fct_zoom(data, list_keys_2))
data_search = []
print(fct_zoom(data, list_keys_1))
data_searche = []
print(fct_zoom(data, list_keys_3))


# liste_zip = zip(liste_name, liste_time)
# liste_set = set(liste_zip)

# print(liste_set)

#pprint.pprint(data["journeys"][0]["sections"][1])

#pprint.pprint(data["journeys"][0]["sections"][1]["stop_date_times"][0]["stop_point"]["label"])
"""
data_links = fct_zoom(data, "journeys")
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
                                        if key == "stop_point":
                                            dict_stop_point = dict_arret[key]
                                            for key in dict_stop_point.keys():
                                                if key == 'label':
                                                    list_arret.append(dict_stop_point[key])

"""