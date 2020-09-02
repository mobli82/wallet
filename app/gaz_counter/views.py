from django.db.models.aggregates import Max, Sum
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_gaz_cost = GazCounterModel.objects.filter(owner=self.request.user).aggregate(Sum('monthly_cost'))
        if total_gaz_cost['monthly_cost__sum'] is None:
            total_gaz_cost['monthly_cost__sum'] = 0.00
        context["total_gaz_cost"] = float(total_gaz_cost['monthly_cost__sum'])
        return context
    

class GazCounterDetailView(DetailView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_detail.html'

class GazCounterCreateView(CreateView):
    model = GazCounterModel
    fields = ['value']
    template_name = 'gaz_counter/gaz_counter_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class GazCounterDeletelView(DeleteView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_delete.html'
    success_url = '/gaz-list/'

class GazCounterUpdateView(UpdateView):
    model = GazCounterModel
    fields = ['value']
    template_name = 'gaz_counter/gaz_counter_update.html'