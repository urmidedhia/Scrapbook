from django.urls import path, include
from home import views

urlpatterns = [
    path('odin/', views.home, name='home'),
]