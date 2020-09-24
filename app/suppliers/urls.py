from django.urls import path

from .gaz_suppliers_views import (GazSuppliersListView, 
                    GazSupplierCreateView, 
                    GazSupplierDetailView,
                    GazSupplierUpdateView,
                    GazSupplierDeleteView,
)

from .power_suppliers_views import ( PowerSuppliersListView,
                                     PowerSupplierCreateView,
                                     PowerSupplierDetailView,
                                     PowerSupplierDeleteView,
                                     PowerSupplierUpdateView,
)

urlpatterns = [
    path("gaz-suppliers/", GazSuppliersListView.as_view(), name="gaz-suppliers"),
    path("gaz-suppliers/create/", GazSupplierCreateView.as_view(), name="gaz-supplier-create"),
    path("gaz-supplier/detail/<int:pk>/", GazSupplierDetailView.as_view(), name="gaz-supplier-detail"),
    path("gaz-supplier/update/<int:pk>/", GazSupplierUpdateView.as_view(), name="gaz-supplier-update"),
    path("gaz-supplier/delete/<int:pk>/", GazSupplierDeleteView.as_view(), name="gaz-supplier-delete"),
    path("power-suppliers/", PowerSuppliersListView.as_view(), name="power-suppliers"),
    path("power-supplier-create/", PowerSupplierCreateView.as_view(), name="power-supplier-create"),
    path("power-supplier/detail/<int:pk>/", PowerSupplierDetailView.as_view(), name="power-supplier-detail"),
    path("power-supplier/delete/<int:pk>/", PowerSupplierDeleteView.as_view(), name="power-supplier-delete"),
    path("power-supplier/update/<int:pk>/", PowerSupplierUpdateView.as_view(), name="power-supplier-update"),

]
