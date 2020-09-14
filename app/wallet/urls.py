from django.urls import path
from .views import home, counters_list

urlpatterns = [
    path("", home, name="home"),
    path("countres/", counters_list, name="counters"),
]
