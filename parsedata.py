import json

with open('clientData.json') as json_data:
    jsonData = json.load(json_data)
    

for i in jsonData:
    if "http" in i['Logo']:
        print(i)