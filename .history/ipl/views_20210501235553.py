from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .serializers import IplMatchSerializer
from .models import IplMatch
from django.shortcuts import render


# Create your views here.
class MatchListView(generics.ListAPIView):
    serializer_class = IplMatchSerializer
    model = IplMatch
    queryset = model.objects.all()
    paginate_by = 100


class TeamListView(generics.ListAPIView):
    serializer_class = IplMatchSerializer
    model = IplMatch
    queryset = model.objects.all()

    def get_queryset(self):
        return IplMatch.objects.filter(date__year=2009)
