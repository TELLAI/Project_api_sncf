import requests
import json
import pprint
import csv

read = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas',auth=('d402691b-69c5-48e6-b658-9f9be6140b8a',''))
data = json.loads(read.text)
data_links=[]
names_gares = []
list_zip = []
list_latitude = []
list_longitude = []
list_id = []
count = 0

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
                            if k == "coord":
                                dict_coord = dict_info[k]
                                for x in dict_coord.keys():
                                    if x == "lat":
                                        list_latitude.append(dict_coord[x])
                                    elif x == "lon":
                                        list_longitude.append(dict_coord[x])
                            if k == "id":
                                list_id.append(dict_info[k])
                            if k == "zip_code":
                                list_zip.append(dict_info[k])

result_zip = zip(names_gares, list_zip, list_latitude, list_longitude, list_id)
result_set = set(result_zip)

with open('api_sncf_2.csv', 'w') as file:
    fieldnames = ["Nom_gares", "Departement", "Latitude", "Longitude", "ID"]

    csv_file = csv.writer(file, delimiter='\t')

    csv_file.writerow(fieldnames)

    for i in result_set:
        csv_file.writerow([i])