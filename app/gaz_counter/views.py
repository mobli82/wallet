from django.contrib.auth.mixins import UserPassesTestMixin
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gaz_list = GazCounterModel.objects.all().filter(owner=self.request.user).order_by('-date')
        context["gaz_list"] = gaz_list
        print(context)
        return context
   

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     total_gaz_cost = GazCounterModel.objects.filter(owner=self.request.user).aggregate(Sum('monthly_cost'))
    #     if total_gaz_cost['monthly_cost__sum'] is None:
    #         total_gaz_cost['monthly_cost__sum'] = 0.00
    #     context["total_gaz_cost"] = float(total_gaz_cost['monthly_cost__sum'])
    #     return context
    

class GazCounterDetailView(DetailView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_detail.html'

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.owner:
            return True
        return False

class GazCounterCreateView(CreateView):
    model = GazCounterModel
    fields = ['value']
    template_name = 'gaz_counter/gaz_counter_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class GazCounterDeletelView(UserPassesTestMixin, DeleteView):
    model = GazCounterModel
    template_name = 'gaz_counter/gaz_counter_delete.html'
    success_url = '/gaz-list/'

    def test_func(self):
        object = self.get_object()
        if self.request.user == object.owner:
            return True
        return False

class GazCounterUpdateView(UpdateView):
    model = GazCounterModel
    fields = ['value']
    template_name = 'gaz_counter/gaz_counter_update.html'

    def test_func(self):
        object = self.get_object()
        if self.request.user == object.owner:
            return True
        return False