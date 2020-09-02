from django.shortcuts import render
from django.views.generic import (ListView, CreateView, DeleteView, DetailView, UpdateView)

from .forms import GazCounterForm
from .models import GazCounterModel

class GazCounterListView(ListView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_list.html'
    paginate_by = 5
    context_object_name = 'gaz_list'
    ordering = ['-date']

class GazCounterDetailView(DetailView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_detail.html'

class GazCounterCreateView(CreateView):
    model = GazCounterModel
    fields = ['value', 'monthly_usage', 'unit_price']
    template_name = 'gaz_counter/gaz_counter_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class GazCounterDeletelView(DeleteView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_delete.html'
    success_url = '/gaz-list/'