from django.urls import path, include
from entries import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('entry/', views.entry, name='entry'),
    path('close/', views.close, name='close'),
    path('wall/', views.wall, name='wall'),
    path('family/', views.family, name='family'),
    path('scar/', views.scar, name='scar'),
    path('fomo/', views.fomo, name='fomo'),
    path('dates/', views.dates, name='dates'),
]


