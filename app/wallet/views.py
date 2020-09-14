from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wallet/home.html')

def counters_list(request):
    return render(request, 'wallet/counters_list.html')
