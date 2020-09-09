from django.urls import path
from .views import (GazCounterListView, 
                    GazCounterCreateView, 
                    GazCounterDetailView, 
                    GazCounterDeleteView, 
                    # GazCounterUpdateView
)

urlpatterns = [
    path("gaz-list/", GazCounterListView.as_view(), name="gaz-list"),
    path("gaz-create/", GazCounterCreateView.as_view(), name="gaz-create"),
    path("gaz-detail/<int:pk>/", GazCounterDetailView.as_view(), name="gaz-detail"),
    path("gaz-delete/<int:pk>/", GazCounterDeleteView.as_view(), name="gaz-delete"),
    # path("gaz-update/<int:pk>/", GazCounterUpdateView.as_view(), name="gaz-update"),
]
