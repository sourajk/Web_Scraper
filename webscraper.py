from bs4 import BeautifulSoup
import requests
import json

url = 'https://us.epsilon.com/hear-from-our-clients'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

#new_con = content.findAll('li', attrs={"class": "hs-menu-item"})
#
#for x in new_con:
#    print(x.find('a').text)

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

