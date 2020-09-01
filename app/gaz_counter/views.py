from django.shortcuts import render
from django.views.generic import (ListView, CreateView, DeleteView, DetailView, UpdateView)

from .models import GazCounterModel

class GazCounterListView(ListView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_list.html'
    paginate_by = 5
    context_object_name = 'gaz_list'
    ordering = ['-date']

