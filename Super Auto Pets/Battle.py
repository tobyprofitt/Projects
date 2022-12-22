"""
Battle class
"""
import Pet
import Team 

class Battle:
        def __init__(self, team1: Team, team2: Team):
            self.team1 = team1
            self.team2 = team2
        
        