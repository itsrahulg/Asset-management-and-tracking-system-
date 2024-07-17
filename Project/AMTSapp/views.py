from django.shortcuts import render,redirect

from django.contrib.auth import login, authenticate

from django.contrib.auth import logout

from .forms import SignUpForm

from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

def homepage(request):
    return render(request,'AMTSapp/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'AMTSapp/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'AMTSapp/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('')



def dashboard_view(request):
    if request.user.is_superuser:
        return render(request, 'AMTSapp/administrator_dashboard.html')
    else:
        return render(request, 'AMTSapp/user_dashboard.html')





