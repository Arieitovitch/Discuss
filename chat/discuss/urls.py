from django.urls import path
from . import views

urlpatterns = [
    path('hockey.html', views.hockey, name='hockey'),
    path('baseball.html', views.baseball, name='baseball'),
    path('basketball.html', views.basketball, name='basketball'),
    path('football.html', views.football, name='football'),
]