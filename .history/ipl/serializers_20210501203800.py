from rest_framework import serializers
from .models import IplMatch


class IplMatchSerializer(serializers.ModelSerializer):
    team1 = serializers.SerializerMethodField()
    team2 = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'id', 'city', 'date', 'playerOfMatch', 'venue', 'team1',
            'team2', 'tossWinner', 'tossDecision', 'winner', 'result',
            'resultMargin', 'eliminator', 'umpire1', 'umpire2'
        ]

    def get_team1(self, post):
        return Vote.objects.filter(post=post).count()


'id', 'city', 'date', 'playerOfMatch', 'venue', 'team1', 'team2', 'tossWinner,' 'tossDecision', 'winner,'
'result', 'resultMargin', 'eliminator', 'umpire1' 'umpire2'
