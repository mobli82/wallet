from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from gaz_counter.models import GazCounterModel

def home(request):
    return render(request, 'wallet/home.html')

def counters_list(request):
    return render(request, 'wallet/counters_list.html')

def gaz_counter_summary(request):
    context = GazCounterModel.objects.filter(owner=request.user).order_by('date')

    summary = {}

    for record in context:
        date = f'{record.date.month}/{record.date.year}'
        summary[date] = record.monthly_usage

    return JsonResponse({'summary': summary,}, safe=False)

def statistics(request):
    return render(request, 'wallet/statistics_list.html')

def suppliers_list(request):
    return render(request, 'wallet/suppliers_list.html')