from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
warnings.simplefilter("ignore")

import pandas as pd
import requests

API_ENDPOINT = "http://localhost:3200/api/seasons/"

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("file", help="Filename to process")
parser.add_argument("player", type=int, help="ID of player")
args = vars(parser.parse_args())

rawdata = pd.read_html(args['file'], header=0, encoding="utf-8", keep_default_na=False)
seasons = rawdata[0]

for index, row in seasons.iterrows():
  print(row['Year'])
  data = {
    'player_id': args['player'],
    'year': row['Year'],
    'club': row['Team'],
    'info': row['Info'],
    'nation': row['Nation'],
    'division': row['Division']
  }

  r = requests.post(url=API_ENDPOINT, data=data)
  print(r.text)


