from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('fashion', views.fashion, name="fashion"),
    path('fashion_1', views.fashion_1, name="fashion_1"),
    path('fashion_2', views.fashion_2, name="fashion_2"),
    path('fashion_3', views.fashion_3, name="fashion_3"),

    path('food', views.food, name="food"),
    path('food_1', views.food_1, name="food_1"),
    path('food_2', views.food_2, name="food_2"),

    path('beauty', views.beauty, name="beauty"),
    path('beauty_1', views.beauty_1, name="beauty_1"),
    path('beauty_2', views.beauty_2, name="beauty_2"),
    path('beauty_3', views.beauty_3, name="beauty_3"),

    path('transportation', views.transportation, name="transportation"),
    path('transportation_1', views.transportation_1, name="transportation_1"),
    path('transportation_2', views.transportation_2, name="transportation_2"),
]
