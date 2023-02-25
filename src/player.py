from turtle import home


class Player:

    
    def __init__(self,id,name, team_id):
        self.id = id
        self.name = name
        self.team_id = team_id

    def __eq__(self,obj):
        if isinstance(obj,Player):
            if self.id == obj.id:
                return True
            else:
                return False

    def add_hit_stats(self,matches,homeRuns,scorings,scoringPercent,homeRunsAndScoringsTotal):
        self.matches = matches
        self.homeRuns = homeRuns
        self.scorings = scorings
        self.scoringPercent = scoringPercent
        self.homeRunsAndScoringsTotal = homeRunsAndScoringsTotal
    
    def add_bring_stats(self, matches,homeRuns,runs,runTries,runPercent):
        self.matches = matches
        self.homeRuns = homeRuns
        self.runs = runs
        self.runTries = runTries
        self.runPercent = runPercent
    
    '''
    karkilyonnit-pesavaleittain
    bpest = batterPointEventSucceededTotal
    bpestp = batterPointEventSucceededTotalPercent
    bpett = batterPointEventTriesTotal
    bpestb0-3 = batterPointEventSucceededToBase0-3
    bpettb0-3 = batterPointEventTriesToBase0-3
    bpesptb0-3 = batterPointEventSucceededPercentToBase0-3

    '''
    def add_edge_stats(self,bpest, bpestp, bpett, bpestb0, bpestb1, bpestb2, bpestb3,
    bpettb0,bpettb1,bpettb2,bpettb3,bpesptb0,bpesptb1,bpesptb2,bpesptb3):
        self.bpest = bpest
        self.bpestp = bpestp
        self.bpett = bpett
        self. bpestb0 = bpestb0
        self.bpestb1 = bpestb1
        self.bpestb2 = bpestb2
        self.bpestb3 = bpestb3
        self.bpettb0 = bpettb0
        self.bpettb1 = bpettb1
        self.bpettb2 = bpettb2
        self.bpettb3 = bpettb3
        self.bpesptb0 = bpesptb0
        self.bpesptb1 = bpesptb1
        self.bpesptb2 = bpesptb2
        self.bpesptb3 = bpesptb3

    '''
    saatot
    bast = batterAdvancingsSucceededTotal
    bact = batterAdvancingCaughtTotal
    bacot = batterAdvancingOutTotal
    batt = batterAdvancingTriesTotal
    '''
    def add_brings_stat(self,bast,bact,bacot,batt):
        self.bast = bast
        self.bact = bact
        self.bacot = bacot
        self.batt = batt

    '''
    etenemiset
    rast = runnerAdvancingsSucceededTotal
    rpest = runnerPointEventSucceededTotal
    rpect = runnerPointEventCaughtTotal
    rpeot = runnerPointEventOutTotal
    rpett = runnerPointEventTriesTotal
    rwt = runnerWalksTotal
    raowtt = runnerAdvancingsOnWildThrowTotal
    rtest = runnerTailEventSucceededTotal
    rtect = runnerTailEventCaughtTotal
    rteot = runnerTailEventOutTotal
    rtett = runnerTailEventTriesTotal
    '''
    def add_progress_stat(self,rast,rpest,rpect,rpeot,rpett,rwt,raowtt,rtest,rtect,rteot,rtett):
        self.rast = rast
        self.rpest = rpest
        self.rpect = rpect
        self.rpeot = rpeot
        self.rpett = rpett
        self.rwt = rwt
        self.raowtt = raowtt
        self.rtest = rtest
        self.rtrect = rtect
        self.rteot = rteot
        self.rtett = rtett

    def __str__(self):
        return str(self.id)

    