from django.urls import path
from .views import (GazCounterListView)

urlpatterns = [
    path("gaz-list/", GazCounterListView.as_view(), name="gaz-list"),
]
