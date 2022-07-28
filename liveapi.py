# For interaction with game api

from swgohhelp import SWGOHhelp, settings
import json
from pprint import pprint

with open('./config.json') as f:
  config = json.load(f)

# Connect to swgohhelp
# Get swgohhelp player data
def gpd():
  creds = settings(config['swgohhelp']['credname'], config['swgohhelp']['credpass'], config['swgohhelp']['crednum'], config['swgohhelp']['credlet'])
  client = SWGOHhelp(creds)

  response = client.get_data('player', config['allycodes'])
  with open('player.json', 'w') as f:
    json.dump(response, f)

