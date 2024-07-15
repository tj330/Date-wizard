from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('day_predict', views.day, name="day"),
    path('goal_setter', views.goal, name="goal"),
]
