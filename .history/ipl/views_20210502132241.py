from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .serializers import IplMatchSerializer
from .models import IplMatch
from django.shortcuts import render
from django.db.models import Q

teamDict = {
    'RCB': 'Royal Challengers Bangalore',
    'CSK': 'Chennai Super Kings',
    'RPS': 'Rising Pune Supergiants',
    'MI': 'Mumbai Indians',
    'PW': 'Pune Warriors',
    'GL': 'Gujarat Lions',
    'KTK': 'Kochi Tuskers Kerala',
    'DCSRH': 'Deccan Chargers',
    'SRH': 'Sunrisers Hyderabad',
    'KXIP': 'Kings XI Punjab',
    'DC': 'Delhi Capitals',
    'RR': 'Rajasthan Royals',
    'DDDC': 'Delhi Daredevils',
    'KKR': 'Kolkata Knight Riders'
}


# Create your views here.
class MatchListView(generics.ListAPIView):
    serializer_class = IplMatchSerializer
    model = IplMatch
    queryset = model.objects.all()
    paginate_by = 100


class MatchListViewAsPerYear(generics.ListAPIView):
    serializer_class = IplMatchSerializer
    model = IplMatch
    queryset = model.objects.all()

    def get_queryset(self, *args, **kwargs):
        requestedYear = self.kwargs['year']
        return IplMatch.objects.filter(date__year=requestedYear)


class MatchListViewAsPerTeam(generics.ListAPIView):
    serializer_class = IplMatchSerializer
    model = IplMatch
    queryset = model.objects.all()

    def get_queryset(self, *args, **kwargs):
        teamName = teamDict[self.kwargs['team']]
        return IplMatch.objects.filter(team1=teamName | team2=teamName)
