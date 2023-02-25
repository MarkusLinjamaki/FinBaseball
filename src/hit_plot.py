#%%
import matplotlib.pyplot as plt
from multiprocessing.sharedctypes import Value
from operator import concat
import requests
import json






# TODO Maybe move to somewhere else
def hit_stats_search(match_id):
    '''Baseball savant visuals.

    Parameters:
    match_id(int): Match id
    
    '''

    hit_out = "out"
    hit_in = "in"
    hit_caught = "caught"

    outs = {
        'coord' : []
    }
    ins = {
        'coord' : []
    }
    caughts = {
        'coord' : []
    }
    hit_stats = []

    req = f'https://www.pesistulokset.fi/api/v1/online/{match_id}/events' 
    response = requests.get(req)
    response.encoding = 'utf-8-sig' # Encode the data
    data = json.loads(response.text)
    data = data['events']
    grouptypes = []
    for event in data:
        grouptypes.append(event['groupType'])
        if event['groupType'] == 'he':
            player_id = event['batter']
            team_id = event['team']
            # Need to scale coordinates to match actual Pesäpallo field
            x_scale = ((float(event['hit']['x'])-10) / 82) * (42) + 29
            #x_scale = float((event['hit']['x']))
            y = float((event['hit']['y']))
            if event['hit']['out']: # OUT

                outs['coord'].append((x_scale,y))
                hit_type = hit_out
            elif event['hit']['caught']:

                caughts['coord'].append((x_scale,y))
                hit_type = hit_caught
            else:

                ins['coord'].append((x_scale,y))
                hit_type = hit_in
            hit_stats.append([x_scale,y,hit_type,player_id,team_id,match_id])
    return hit_stats





