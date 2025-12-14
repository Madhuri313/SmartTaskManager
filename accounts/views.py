from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

# If you prefer the earlier class-based code, keep it commented as you had it.

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tasks:dashboard')
        else:
            return render(request, 'accounts/login.html', {
                'form': form,
                'error': 'Invalid username or password'
            })

    # GET request: provide an empty form so {{ form.as_p }} renders fields
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def custom_logout(request):
    # Log the user out, then redirect to login
    logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('tasks:dashboard')
    else:
        # This runs for GET requests (page load)
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})