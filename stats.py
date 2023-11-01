import pandas as pd
import requests
import re

API_ENDPOINT = "http://localhost:3200/api/stats/"

rawdata = pd.read_html('JQHistory.html', header=0, encoding="utf-8", keep_default_na=False)
stats = rawdata[1]

for index, row in stats.iterrows():
  apps = None
  starts = None
  subs = None
  passes = None
  penalties = None
  pens_taken = None
  pens_scored = None

  apps = re.findall("\d+", row['Tot Apps'])
  if (apps):
    if (len(apps) > 1):
      starts = apps[0]
      subs = apps[1]
    else:
      starts = apps[0]
      subs = None
  
  passes = re.findall("\d+", row['Pas %'])
  if (passes):
    passes = passes[0]
  else:
    passes = None

  shots = re.findall("\d+", row['Shts OT (%)'])
  if (shots):
    shots = shots[0]
  else:
    shots = None

  penalties = re.findall("\d+", row['Pens'])
  if (penalties):
    if (len(penalties) > 1):
      pens_taken = penalties[0]
      pens_scored = penalties[1]
    else:
      pens_taken = penalties[0]
      pens_scored = None

  if row['Gls'] == '-':
    row['Gls'] = None
  if row['Asts'] == '-':
    row['Asts'] = None
  if row['Pens'] == '-':
    row['Pens'] = None
  if row['PoM'] == '-':
    row['PoM'] = None
  if row['Yel'] == '-':
    row['Yel'] = None
  if row['Red'] == '-':
    row['Red'] = None
  if row['TckW/90'] == '-':
    row['TckW/90'] = None
  if row['Pas %'] == '-':
    row['Pas %'] = None
  if row['Drb/90'] == '-':
    row['Drb/90'] = None
  if row['Shts OT (%)'] == '-':
    row['Shts OT (%)'] = None
  if row['Fouls'] == '-':
    row['Fouls'] = None
  if row['Fls Ag'] == '-':
    row['Fls Ag'] = None
  if row['Av R'] == '----':
    row['Av R'] = None

  data = {
    'season_id': 1028,
    'match_type': index,
    'starts': starts,
    'subs': subs,
    'pens_taken': pens_taken,
    'pens_scored': pens_scored,
    'goals': row['Gls'],
    'assists': row['Asts'],
    'pom': row['PoM'],
    'yellow_cards': row['Yel'],
    'red_cards': row['Red'],
    'tackles_won': row['TckW/90'],
    'pass_completion': passes,
    'dribbles_made': row['Drb/90'],
    'shots_target': shots,
    'fouls': row['Fouls'],
    'fouls_against': row['Fls Ag'],
    'average_rating': row['Av R']
  }

  # print(data)

  r = requests.post(url=API_ENDPOINT, data=data)
  print(r.text)

# print(stats.loc[1]['Tot Apps'])
# data = {
#   'season_id': 2,
#   'match_type': 2,
#   'goals': stats.loc[1]['Gls'],
#   'assists': stats.loc[1]['Asts']
# }

# r = requests.post(url=API_ENDPOINT, data=data)
# print(r)

