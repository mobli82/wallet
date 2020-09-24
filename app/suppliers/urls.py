from django.urls import path

from .gaz_suppliers_views import (GazSuppliersListView, 
                    GazSupplierCreateView, 
                    GazSupplierDetailView,
                    GazSupplierUpdateView,
                    GazSupplierDeleteView
)

urlpatterns = [
    path("gaz-suppliers/", GazSuppliersListView.as_view(), name="gaz-suppliers"),
    path("gaz-suppliers/create/", GazSupplierCreateView.as_view(), name="gaz-supplier-create"),
    path("gaz-supplier/detail/<int:pk>/", GazSupplierDetailView.as_view(), name="gaz-supplier-detail"),
    path("gaz-supplier/update/<int:pk>/", GazSupplierUpdateView.as_view(), name="gaz-supplier-update"),
    path("gaz-supplier/delete/<int:pk>/", GazSupplierDeleteView.as_view(), name="gaz-supplier-delete"),
]
