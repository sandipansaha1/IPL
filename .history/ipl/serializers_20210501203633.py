from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    vote_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'id', 'city', 'date', 'playerOfMatch', 'venue', 'team1',
            'team2', 'tossWinner', 'tossDecision', 'winner', 'result',
            'resultMargin', 'eliminator', 'umpire1'
            'umpire2'
        ]

    def get_vote_count(self, post):
        return Vote.objects.filter(post=post).count()


'id', 'city', 'date', 'playerOfMatch', 'venue', 'team1', 'team2', 'tossWinner,' 'tossDecision', 'winner,'
'result', 'resultMargin', 'eliminator', 'umpire1' 'umpire2'
