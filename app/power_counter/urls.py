from django.urls import path

from .views import (PowerCounterListView,
                    PowerCounterCreateView,
                    PowerCounterDetailView,
                    PowerCounterDeleteView,

)
urlpatterns = [
    path("power-list/", PowerCounterListView.as_view(), name="power-list"),
    path("power-create/", PowerCounterCreateView.as_view(), name="power-create"),
    path("power-detail/<int:pk>/", PowerCounterDetailView.as_view(), name="power-detail"),
    path("power-delete/<int:pk>/", PowerCounterDeleteView.as_view(), name="power-delete"),
]
