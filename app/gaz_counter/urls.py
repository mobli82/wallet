from django.urls import path
from .views import (GazCounterListView, GazCounterCreateView)

urlpatterns = [
    path("gaz-list/", GazCounterListView.as_view(), name="gaz-list"),
    path("gaz-create/", GazCounterCreateView.as_view(), name="gaz-create"),
]
