from django.shortcuts import render
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm(request.POST or None,)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'users/registration.html', {'form': form})