import requests, json, random
from dotenv import load_dotenv
import os
import datetime

x = datetime.datetime.now()
update = x.strftime("%c")

load_dotenv()

apikey = os.getenv("API")

f = open("./README.md", "w")

link = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(apikey)

res = requests.get(f'''{link}''')
data = json.loads(res.text)

date = data['date']


f.write(f'''
  # Awesome space image of the day from [NASA](https://api.nasa.gov/)

  ### Today image : {data['title']}
  Date : {date}

  ![]({data['url']})

  <small>Latest update : {update}</small>
''')

f.close()
