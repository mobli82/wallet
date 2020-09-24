from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import(CreateView, DetailView, ListView, UpdateView, DeleteView)

from .forms import PowerSupplierForm
from .models import PowerSupplierModel

class PowerSuppliersListView(LoginRequiredMixin, ListView):
    model = PowerSupplierModel
    template_name = 'suppliers/power_supplier/power_suppliers_list.html'

class PowerSupplierDetailView(LoginRequiredMixin, DetailView):
    model = PowerSupplierModel
    template_name = 'suppliers/power_supplier/power_supplier_detail.html'

class PowerSupplierCreateView(LoginRequiredMixin, CreateView):
    model = PowerSupplierModel
    form_class = PowerSupplierForm
    template_name = 'suppliers/power_supplier/power_supplier_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PowerSupplierUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PowerSupplierModel
    form_class = PowerSupplierForm
    template_name = 'suppliers/power_supplier/power_supplier_update.html'

    def test_func(self):
        obj = self.get_object()

        if self.request.user == obj.owner:
            return True
        return False

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PowerSupplierDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PowerSupplierModel
    template_name = 'suppliers/power_supplier/power_supplier_delete.html'
    success_url = '/suppliers/power-suppliers/'

    def test_func(self):
        obj = self.get_object()

        if self.request.user == obj.owner:
            return True
        return False

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)