from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm(request.POST or None,)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'users/registration.html', {'form': form})

@login_required
def logout(request):
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')
