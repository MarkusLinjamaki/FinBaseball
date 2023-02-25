#%%
# from itertools import count
from multiprocessing.sharedctypes import Value
from operator import concat
from telnetlib import GA
import requests
import json
import re
import feather
import pandas as pd
import numpy as np
from tqdm import tqdm # progress bar
from team import *
from game import Game
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import hit_plot
import pickle
#%%




"""
TODO load current year team names and ids
TODO Save results in valid form
TODO Figure out how to find all the correc season events 
"""

def get_team_squads(game_id):
    """Get pesapallo match squad 
    """
    myUrl = f'https://www.pesistulokset.fi/ottelut/{game_id}#lineup'
    # Opening connection
    req = Request(myUrl,headers={'User-Agent': 'Mozilla/5.0'})
    page_html = urlopen(req).read()
    soup = BeautifulSoup(page_html,"html.parser")
    res = soup.find_all("div", class_ = "ml-3" )

    # Convert outfield positions to numbers for the ML 

    outfield_positions= {
    "Lukkari" : 1,
    "Sieppari" : 2,
    "Ykkösvahti" : 3,
    "Kakkosvahti" : 4,
    "Kolmosvahti" : 5,
    "Kakkospolttaja" : 6,
    "Kolmospolttaja" : 7,
    "Kakkoskoppari" : 8,
    "Kolmoskoppari" : 9
    }

    # We cant directly conclude which team player is playing. We suppose
    # that first home team players are listed, then coaches (Pelinjohtaja) 
    # and then the away players
    # NOTE Outfiel postions migth be used to something later...

    is_home_team = True
    home_team = []
    away_team = []
    infield_position_index = 1

    try:
        for r in res:
            outfield_position_index = 0 # This might not be changed if player has not outfield position
            player_name = r.find('h5').text.strip()
            outfield_position = r.find('span').text.strip()

            if "Pelinjohtaja" in outfield_position:
                is_home_team = False
                infield_position_index = 1
            else:
                if outfield_position in outfield_positions:
                    outfield_position_index = outfield_positions[outfield_position]

                if is_home_team:
                    home_team.append((player_name,infield_position_index,outfield_position_index))
                else:
                    away_team.append((player_name,infield_position_index,outfield_position_index))
                infield_position_index += 1
    except:
        home_team = None
        away_team = None
    return home_team, away_team


def season_search(level,series,phace,seasonseries, season):
    """Search season stats
    
        Returns:
            games: All season games
            hit_stats: Hit stats for all games

    """

    level = 1
    series = 1
    phace = 1
    seasonseries = 347
    season = 32
    teams = []
    req = f'https://www.pesistulokset.fi/api/v1/result-board?season={season} \
            &seasonSeries={seasonseries}&phase={phace}'
            

    response = requests.get(req)
    response.encoding = 'utf-8-sig' # Encode the data
    data = json.loads(response.text)
    teams_data =  data['data']['result_boards'][0]['resultBoard']
    teams = [Team(t['team']['id'], t['team']['shorthand']) for t in teams_data]

    req = f'https://www.pesistulokset.fi/api/v1/matches?level={level}& \
            series={series}&phase={phace}&seasonseries={seasonseries}& \
            limit=50&order=desc&type=results' 

    # All season games
    games = []

    # All hits
    hit_stats = []
    # We need two flags; when season starts and when it ends
    season_2020_begin = True 
    season_2020_end = True
    ## 


    # Continue until season has started and ended
    while season_2020_begin or season_2020_end:
        response = requests.get(req)
        response.encoding = 'utf-8-sig' 
        data = json.loads(response.text)
        # Request to next page
        req = data['next_page']
        game_data = data['data']

        for game in game_data:
            
            current_seasonserie = game['series']['seasonSeries']
            # If we are in correct season, season has begun
            if current_seasonserie == seasonseries:
                season_2020_begin = False

                # Lets find teams that are playing
                home = game['home']
                away = game['away']
                id = game['id']
                home_squad, away_squad = get_team_squads(id)
                hit_stats = hit_stats + hit_plot.hit_stats_search(id)

                # Need these to determine winner of the match
                periods_home = game['result']['periods_home']
                periods_away = game['result']['periods_away']

                home_team = [t for t in teams if t.id == home][0]
                away_team = [t for t in teams if t.id == away][0]

                if periods_home > periods_away:
                    games.append(Game(home, away,1, home_squad, away_squad))
                    
                    home_team.update(1,0,0,0)
                    away_team.update(0,0,0,1)
                    
                # Away win
                else:
                    games.append(Game(home, away,0, home_squad, away_squad))
                    home_team.update(0,1,0,0)
                    away_team.update(0,0,1,0)

            # If we are not in correct season and first flag is down the season has passed
            if not season_2020_begin and current_seasonserie != seasonseries:
                season_2020_end = False
                break
    return(games,hit_stats)



#%%
# TEST
games,hit_stats = season_search(1,1,1,347,32)
hit_stats = np.array(hit_stats)
np.save("hit_stats",hit_stats)

# Save games to futher fun
file_name = "game_info"
out_file = open(file_name, 'wb')
pickle.dump(games,out_file)
out_file.close()
# %%
