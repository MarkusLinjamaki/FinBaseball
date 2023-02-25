import requests
import json
import re
import pandas as pd
import numpy as np
from team import Team
from player import Player

# TODO return team stats
def team_data_search(season, season_series, phace, group):
        
    teams = []
    phace = 1
    season_series = 347
    group = 876
    season = 33
    website = f'https://www.pesistulokset.fi/api/v1/stats/joukkueet/kolmostilanteet-per-ottelu? \
                season={season}&seasonSeries={season_series}&phase={phace}&group={group}'

    response = requests.get(website)
    response.encoding = 'utf-8-sig' 
    response_text = json.loads(response.text)

    for a in response_text['data']:
        print(a['team_id'])
        print(a['stats']['runnersAtThirdBase'])

    website = f'https://www.pesistulokset.fi/api/v1/stats/joukkueet/karkilyonnit-per-ottelu? \
                season={season}&seasonSeries={season_series}&phase={phace}&group={group}'

    response = requests.get(website)
    response.encoding = 'utf-8-sig' 
    response_text = json.loads(response.text)

    for a in response_text['data']:
        print(a['team_id'])
        print(a['stats']['pointEventsTotal'])



