import requests
from bs4 import BeautifulSoup
import json

url = "https://www.holidify.com/collections/monuments-of-india"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
p = soup.find_all("p", class_="card-text")
h3 = soup.find_all("h3", class_="card-heading")
images = soup.find_all("img", class_="card-img-top lazy")

data = {}
for i in range(len(h3)):
    name = h3[i].text
    image = images[i]['data-original']
    description = p[i].text.split('Timings')[0]
    timings = (p[i].text.split('Timings')[1]).split('Entry')[0]
    entry = (p[i].text.split('Entry')[1]).split('Speciality')[0]
    speciality = p[i].text.split('Speciality')[1]
    
    data[i] = { 'name': name,
                'image': image,
                'description': description,
                'timings': timings,
                'entry': entry,
                'speciality': speciality
                }

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
    f.close()
    
