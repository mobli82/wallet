from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import(CreateView, DetailView, ListView, UpdateView, DeleteView)

from .forms import GazSupplierForm
from .models import GazSupplierModel

class GazSuppliersListView(LoginRequiredMixin, ListView):
    model = GazSupplierModel
    template_name = 'suppliers/gaz_supplier/gaz_suppliers_list.html'

class GazSupplierDetailView(LoginRequiredMixin, DetailView):
    model = GazSupplierModel
    template_name = 'suppliers/gaz_supplier/gaz_supplier_detail.html'

class GazSupplierCreateView(LoginRequiredMixin, CreateView):
    model = GazSupplierModel
    form_class = GazSupplierForm
    template_name = 'suppliers/gaz_supplier/gaz_supplier_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class GazSupplierUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GazSupplierModel
    form_class = GazSupplierForm
    template_name = 'suppliers/gaz_supplier/gaz_supplier_update.html'

    def test_func(self):
        obj = self.get_object()

        if self.request.user == obj.owner:
            return True
        return False

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class GazSupplierDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GazSupplierModel
    template_name = 'suppliers/gaz_supplier/gaz_supplier_delete.html'
    success_url = '/suppliers/gaz-suppliers/'

    def test_func(self):
        obj = self.get_object()

        if self.request.user == obj.owner:
            return True
        return False

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
