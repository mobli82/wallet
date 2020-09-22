from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

from .models import PowerCounterModel

class PowerCounterListView(LoginRequiredMixin, ListView):
    model = PowerCounterModel
    template_name = 'power_counter/power_counter_list.html'
    paginate_by = 5
    context_object_name = 'power_list'

    def get_queryset(self):
        return PowerCounterModel.objects.all().filter(owner=self.request.user).order_by('-date')

class PowerCounterDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = PowerCounterModel
    template_name = 'power_counter/power_counter_detail.html'

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.owner:
            return True
        return False

class PowerCounterCreateView(LoginRequiredMixin, CreateView):
    model = PowerCounterModel
    fields = ['value']
    # fields = ['value', 'date', 'monthly_cost', 'monthly_usage']
    template_name = 'power_counter/power_counter_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PowerCounterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PowerCounterModel
    template_name = 'power_counter/power_counter_delete.html'
    success_url = '/power-list/'

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.owner:
            return True
        return False