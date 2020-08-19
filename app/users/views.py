from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm


# Create your views here.

def register(request):
    form = UserRegistrationForm(request.POST or None,)

    if form.is_valid():
        form.save()

        messages.success(request, f'Account has been created')
        return redirect('login')

    return render(request, 'users/registration.html', {'form': form})

@login_required
def logout(request):
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updeted')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context ={
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
