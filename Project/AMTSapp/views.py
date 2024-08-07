from django.shortcuts import render,redirect

from django.contrib.auth import login, authenticate

from django.contrib.auth import logout

from .forms import SignUpForm

from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomAuthenticationForm

from django.contrib.auth.decorators import login_required



#for admin creating other superusers
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import SuperUserCreationForm


#for doing google sign in 
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
import requests as http_requests



from .forms import SoftwareForm




# Create your views here.
#---------------------------------------------------------------------



def homepage(request):
    return render(request,'AMTSapp/index.html')





def google_login(request):
    google_client_id = settings.GOOGLE_CLIENT_ID
    redirect_uri = settings.GOOGLE_REDIRECT_URI
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"

    oauth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"response_type=code&"
        f"client_id={google_client_id}&"
        f"redirect_uri={redirect_uri}&"
        f"scope={scope}"
    )
    
    return redirect(oauth_url)

def google_callback(request):
    code = request.GET.get('code')
    client_id = settings.GOOGLE_CLIENT_ID
    client_secret = settings.GOOGLE_CLIENT_SECRET
    redirect_uri = settings.GOOGLE_REDIRECT_URI
    
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }
    
    token_response = http_requests.post(token_url, data=token_data)
    token_response_data = token_response.json()
    
    if 'error' in token_response_data:
        return render(request, 'login_error.html', {'error': token_response_data['error']})
    
    id_info = id_token.verify_oauth2_token(token_response_data['id_token'], requests.Request(), client_id)
    
    user_email = id_info.get('email')
    user_name = id_info.get('name')
    
    # Handle user authentication and session management here
    
    return render(request, 'AMTSapp/user_dashboard.html', {'user_email': user_email, 'user_name': user_name})







def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
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






@login_required
def dashboard_view(request):
    if request.user.is_superuser:
        return render(request, 'AMTSapp/administrator_dashboard.html')
    else:
        return render(request, 'AMTSapp/user_dashboard.html')


@login_required
def updatelog(request):
    return render(request,'AMTSapp/update-log.html')

@login_required
def adduser(request):
    return render(request,'AMTSapp/add-superuser.html')








def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def create_superuser(request):
    if request.method == 'POST':
        form = SuperUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Superuser created successfully.')
            return redirect('dashboard')
    else:
        form = SuperUserCreationForm()
    return render(request, 'AMTSapp/create_superuser.html', {'form': form})






def asset_types(request):
    return render(request, 'AMTSapp/asset_types.html')



#view to render software form
def software_form(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_types')  # Redirect to a success page or home page
    else:
        form = SoftwareForm()

    return render(request, 'AMTSapp/software-asset.html', {'form': form})





#view for adding computer asset
from .forms import ComputerHardwareForm

def add_computer_hardware(request):
    if request.method == 'POST':
        form = ComputerHardwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_types')  # Redirect to a success page or list page
    else:
        form = ComputerHardwareForm()
    return render(request, 'AMTSapp/computer-asset.html', {'form': form})



#to render the projector form
from .forms import ProjectorForm

def add_projector(request):
    if request.method == 'POST':
        form = ProjectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_types')  # Redirect to a dashboard or any other page after successful form submission
    else:
        form = ProjectorForm()
    return render(request, 'AMTSapp/projector-asset.html', {'form': form})




#to render the books form
from .forms import BooksForm

def add_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_types')  # Adjust the redirect URL as needed
    else:
        form = BooksForm()
    return render(request, 'AMTSapp/book-asset.html', {'form': form})


























from .models import ComputerHardware, Projector, Software, Books

def assets_by_location(request, location):
    computer_hardware_assets = ComputerHardware.objects.filter(location=location)
    projector_assets = Projector.objects.filter(location=location)
    software_assets = Software.objects.filter(location=location)
    books_assets = Books.objects.filter(location=location)
    
    grouped_assets = {
        'computer_hardware': computer_hardware_assets,
        'projector': projector_assets,
        'software': software_assets,
        'books': books_assets
    }
    
    return render(request, 'AMTSapp/assets_by_location.html', {
        'grouped_assets': grouped_assets,
        'location': location
    })



