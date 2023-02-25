#%%
from operator import concat
import requests
import json
import re
import pandas as pd
import numpy as np
from tqdm import tqdm # progress bar
from team import Team
from player import Player
import pickle as pickle

#%%
def player_data_search(season, season_series, phase, group):
    ''' Collect player data from spesific season
    '''

    req = f'https://www.pesistulokset.fi/api/v1/stats/pelaajat/lyodyt?\
            season={season}&seasonSeries={season_series}&phase={phase}&\
            group={group}'
    players = [] # ALL players are here, is this best data format?

    response = requests.get(req)
    response.encoding = 'utf-8-sig' 
    response = json.loads(response.text)

    # Little annoying that we dont get players full name, id and team id 
    # from the same place So create temporaly dictionary for players id
    # and full name (Needed for data scraping)
    player_id_and_full_name = {}

    player_information = response['maps']['players']
    [player_id_and_full_name.update({p['id'] : p['name']})
     for p in player_information]

    for inf in response['data']:
        player_id = inf['player_id']
        team_id = inf["team_id"]
        stats = inf['stats']
        matches = stats['matches']
        homeRuns = stats['homeRuns']
        scorings = stats['scorings']
        scoringPercent = stats['scoringPercent']
        homeRunsAndScoringsTotal = stats["homeRunsAndScoringsTotal"]
        players.append(Player(player_id,player_id_and_full_name[player_id],team_id ))
        [p.add_hit_stats(matches,homeRuns,scorings,scoringPercent,homeRunsAndScoringsTotal) 
        for p in players if p.id == player_id]


    req = f'https://www.pesistulokset.fi/api/v1/stats/pelaajat/tuodut?\
            season={season}&seasonSeries={season_series}&phase={phase}&\
            group={group}'
    response = requests.get(req)
    response.encoding = 'utf-8-sig' # Encode the data
    response = json.loads(response.text)


    for inf in response['data']:
        player_id = inf['player_id']
        stats = inf['stats']
        matches = stats['matches']
        runs = stats['runs']
        runTries = stats['runTries']
        runPercent = stats['runPercent']
        [p.add_bring_stats(matches, homeRuns, runs, runTries, runPercent) 
        for p in players if p.id == player_id]
        

    req = f'https://www.pesistulokset.fi/api/v1/stats/pelaajat/karkilyonnit-pesavaleittain?\
            season={season}&seasonSeries={season_series}&phase={phase}&group={group}'
    response = requests.get(req)
    response.encoding = 'utf-8-sig' # Encode the data
    response = json.loads(response.text)


    for inf in response['data']:
        player_id = inf['player_id']
        stats = inf['stats']
        bpest = stats['batterPointEventSucceededTotal']
        bpestp = stats['batterPointEventSucceededTotalPercent']
        bpett = stats['batterPointEventTriesTotal']
        bpestb0 = stats['batterPointEventSucceededToBase0']
        bpestb1 = stats['batterPointEventSucceededToBase1']
        bpestb2 = stats['batterPointEventSucceededToBase2']
        bpestb3 = stats['batterPointEventSucceededToBase3']
        bpettb0 = stats['batterPointEventTriesToBase0']
        bpettb1 = stats['batterPointEventTriesToBase1']
        bpettb2 = stats['batterPointEventTriesToBase2']
        bpettb3 = stats['batterPointEventTriesToBase3']
        bpesptb0 = stats['batterPointEventSucceededPercentToBase0']
        bpesptb1 = stats['batterPointEventSucceededPercentToBase1']
        bpesptb2 = stats['batterPointEventSucceededPercentToBase2']
        bpesptb3 = stats['batterPointEventSucceededPercentToBase3']
        [p.add_edge_stats(bpest,bpestp,bpett,bpestb0,bpestb1,bpestb2,bpestb3,bpettb0,bpettb1,
        bpettb2,bpettb3,bpesptb0,bpesptb1,bpesptb2,bpesptb3)
         for p in players if p.id == player_id]

    return players


#%%
'''
    season = 33
    season_series = 347
    phase = 1
    group = 876
'''

# Get season information from players
players = player_data_search(33,347,1,876)
file_name = "player_info"
out_file = open(file_name, 'wb')
pickle.dump(players,out_file)
out_file.close()

# Save data

# %%
in_file = open(file_name,'rb')
players = pickle.load(in_file)
in_file.close()
ind = 0
for p in players:
    print(f' {p.name } {p.id} {p.homeRunsAndScoringsTotal} {p.runPercent} {p.bpettb1}')
    ind +=1
    if ind == 10:
        break
# %%
