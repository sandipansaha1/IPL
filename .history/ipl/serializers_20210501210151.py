from rest_framework import serializers
from .models import IplMatch


class IplMatchSerializer(serializers.ModelSerializer):
    team1 = serializers.SerializerMethodField()

    #team2 = serializers.SerializerMethodField()

    class Meta:
        model = IplMatch
        fields = [
            'id', 'id', 'city', 'date', 'playerOfMatch', 'venue', 'team1',
            'team2', 'tossWinner', 'tossDecision', 'winner', 'result',
            'resultMargin', 'eliminator', 'umpire1', 'umpire2'
        ]

    def get_team1(self, obj):
        if self.team1 == obj.tossWinner and "bat" == obj.tossDecision:
            return self.team1
        else:
            obj.team2 = self.team1
            return self.team2


'id', 'city', 'date', 'playerOfMatch', 'venue', 'team1', 'team2', 'tossWinner,' 'tossDecision', 'winner,'
'result', 'resultMargin', 'eliminator', 'umpire1' 'umpire2'
