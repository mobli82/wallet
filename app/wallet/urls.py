from django.urls import path
from .views import (home, 
                    counters_list, 
                    statistics, 
                    gaz_counter_summary_usage, 
                    gaz_counter_summary_costs, 
                    suppliers_list,
                    power_counter_summary_usage,
                    power_counter_summary_costs,
)

urlpatterns = [
    path("", home, name="home"),
    path("countres/", counters_list, name="counters"),
    path("statistics-list/", statistics, name="statistics-list"),
    path("gaz-summary-usage/", gaz_counter_summary_usage, name="gaz-summary-usage"),
    path("gaz-summary-costs/", gaz_counter_summary_costs, name="gaz-summary-costs"),
    path("power-summary-usage/", power_counter_summary_usage, name="power-summary-usage"),
    path("power-summary-costs/", power_counter_summary_costs, name="power-summary-costs"),
    path("suppliers-list/", suppliers_list, name="suppliers-list"),
]
