from rest_framework import serializers
from .models import IplMatch


class IplMatchSerializer(serializers.ModelSerializer):
    team1 = serializers.SerializerMethodField()
    matchYear = serializers.SerializerMethodField()

    #team2 = serializers.SerializerMethodField()

    class Meta:
        model = IplMatch
        fields = [
            'id', 'city', 'date', 'playerOfMatch', 'venue', 'team1', 'team2',
            'tossWinner', 'tossDecision', 'matchYear', 'matchWinner', 'result',
            'resultMargin', 'umpire1', 'umpire2'
        ]

    def get_team1(self, obj):
        if obj.team1 == obj.tossWinner and "bat" == obj.tossDecision:
            return obj.team1
        else:
            temp = obj.team2
            obj.team2 = obj.team1
            return temp

    def get_matchYear(self, obj):
        return obj.date.year
