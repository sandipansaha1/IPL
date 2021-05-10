from django.db import models

class IplMatch(models.Model):

    city	= models.CharField(max_length=100)
    date    = models.DateTimeField(editable=False)	
    playerOfMatch	= models.CharField(max_length=100)
    venue	= models.CharField(max_length=100)
    team1	= models.CharField(max_length=100)
    team2	= models.CharField(max_length=100)
    tossWinner	= models.CharField(max_length=100)
    tossDecision	= models.CharField(max_length=100)
    matchWinner	= models.CharField(max_length=100)
    result	= models.CharField(max_length=100)
    resultMargin	= models.CharField(max_length=100)
    umpire1	= models.CharField(max_length=100)
    umpire2 = models.CharField(max_length=100)

