from django.urls import path
from .views import home, counters_list, statistics, gaz_counter_summary

urlpatterns = [
    path("", home, name="home"),
    path("countres/", counters_list, name="counters"),
    path("statistics-list/", statistics, name="statistics-list"),
    path("gaz-summary/", gaz_counter_summary, name="gaz-summary"),
]
