import pandas as pd
import requests

API_ENDPOINT = "http://localhost:3200/api/seasons/"

rawdata = pd.read_html('JQHistory.html', header=0, encoding="utf-8", keep_default_na=False)
seasons = rawdata[0]

for index, row in seasons.iterrows():
  print(row['Year'])
  data = {
    'player_id': 1,
    'year': row['Year'],
    'club': row['Team'],
    'info': row['Info'],
    'nation': row['Nation'],
    'division': row['Division']
  }

  r = requests.post(url=API_ENDPOINT, data=data)
  print(r.text)


