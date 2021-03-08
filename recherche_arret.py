import requests
import json
import pprint
import csv

read = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000',auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data = json.loads(read.text)

read = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000&start_page=1',auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data.update(json.loads(read.text))

read = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000&start_page=2',auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data.update(json.loads(read.text))

read = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000&start_page=3',auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data.update(json.loads(read.text))

read = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000&start_page=4',auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data.update(json.loads(read.text))



list_id = []
names_gares = []

for i in data.keys():
    if i == "stop_areas":
        data_links = data[i]
        for i in data_links:
            dict_vrac = i
            for key in dict_vrac.keys():
                if key == "administrative_regions":
                    liste_info = dict_vrac[key]
                    for j in liste_info:
                        dict_info = j
                        for k in dict_info.keys():
                            if k == "name":
                                names_gares.append(dict_info[k])
                            if k == "id":
                                list_id.append(dict_info[k])
dict_ID_GARES = {}

for i in range((len(names_gares) - 1)):
    dict_ID_GARES[names_gares[i]] = list_id[i]
    i+= 1

pprint.pprint(dict_ID_GARES)