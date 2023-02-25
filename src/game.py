class Game:
    """
    Pesapallo match details
    """

    def __init__(self,home,away,result, home_squad, away_squad):
        self.home = home
        self.away = away
        self.result = result
        self.home_squad = home_squad
        self.away_squad = away_squad
    
    def __str__(self):
        return str(self.result)

    

