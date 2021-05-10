from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import IplMatch
from django.shortcuts import render


# Create your views here.
class UserPostsReadView(generics.ListAPIView):
    serializer_class = PostSerializer
    model = IplMatch
    paginate_by = 100