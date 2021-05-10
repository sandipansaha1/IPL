from django.db import models

class IplMatch(models.Model):
    
    city	= models.CharField(max_length=100)
    date	
    player_of_match	
    venue	
    team1	
    team2	
    toss_winner	
    toss_decision	
    winner	
    result	
    result_margin	
    umpire1	
    umpire2
    
    