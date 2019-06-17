from bs4 import BeautifulSoup
import requests
import json

url = '' #insert what you want to enter here and change the attributes and/or attribute names accordingly below!!
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


info_client = []
for info in content.findAll('div', attrs={"class": "video-item"}):
    clientObject = {
        "Logo": info.find('img').get('src'),
        "Name": info.find('h4', attrs={"class": "field-content"}).text,
        "Job-title": info.find('div', attrs={"class":"job-title"}).text
    }
    
    info_client.append(clientObject)

    with open('clientData.json', 'w') as outfile:
        json.dump(info_client, outfile)

