from player import Player

HOME_WIN = (1,0,0,0)
HOME_LOSS = (0,1,0,0)
AWAY_WIN = (0,0,1,0)
AWAY_LOSS = (0,0,0,1)

class Team:
    """ Team stats for one season
    """
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.games = 0
        self.home_wins = 0
        self.home_draws = 0
        self.home_losses = 0
        self.away_wins = 0
        self.away_draws = 0
        self.away_losses = 0
        self.players = []

    # Update team stats
    def update(self,home_win,home_loss,away_win,away_loss):
        self.games = self.games + 1
        self.home_wins = self.home_wins + home_win
        self.home_losses = self.home_losses + home_loss
        self.away_wins = self.away_wins + away_win
        self.away_losses = self.away_losses + away_loss
    
    
    def add_player(self,player):
        self.players.append(player)
    
    def __str__(self):
        return self.name