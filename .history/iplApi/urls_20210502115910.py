"""iplApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from ipl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/match/', views.MatchListView.as_view()),
    #re_path(r'^api/match/(?P<year>[0-9]{4})/$', views.TeamListView.as_view()),
    path("api/match/<int:year>", views.TeamListView.as_view()),
]
