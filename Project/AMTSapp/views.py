import datetime
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



#for doing google sign in 
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
import requests as http_requests



#import statements for software add and update functionality
from django.shortcuts import render, get_object_or_404, redirect
from .models import Software, SoftwareUpdateLog
from .forms import SoftwareForm
from django.utils import timezone


#import statement for computer assets update and log functionality
from .models import ComputerHardware, ComputerHardwareUpdateLog


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



from django.views.decorators.cache import never_cache

from django.http import HttpResponse

def logout_view(request):
    logout(request)
    response = redirect('')  # Replace 'home' with your actual homepage URL name
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response





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




#creating and updating superuser
from .forms import UserRoleForm
from django.contrib.auth.models import User

# List users and handle role update
@login_required
def user_list_and_update(request):
    # Exclude the current user from the list of users
    users = User.objects.exclude(pk=request.user.pk)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)

        # Check if 'is_superuser' was posted and update accordingly
        is_superuser = 'is_superuser' in request.POST
        user.is_superuser = is_superuser

        # Update staff status based on whether the user is a superuser
        if is_superuser:
            user.is_staff = True  # Admins are considered staff
        else:
            user.is_staff = False  # Remove staff privileges if not admin

        user.save()

        return redirect('user_list_and_update')

    return render(request, 'AMTSapp/user_list_and_update.html', {'users': users})





def is_superuser(user):
    return user.is_superuser







@login_required
def asset_types(request):
    return render(request, 'AMTSapp/asset_types.html')



@login_required
def scrapped_log(request):
    return render(request,'AMTSapp/delete_and_invalid_log.html')

@login_required
def movement_history(request):
    return render(request,'AMTSapp/movement_history.html')



from .models import InvalidSoftwareEntry, ScrappedSoftwareAsset

def invalid_software_entries(request):
    invalid_entries = InvalidSoftwareEntry.objects.all()
    return render(request, 'AMTSapp/invalid_software_entries.html', {'invalid_entries': invalid_entries})

def scrapped_software_assets(request):
    scrapped_assets = ScrappedSoftwareAsset.objects.all()
    return render(request, 'AMTSapp/scrapped_software_assets.html', {'scrapped_assets': scrapped_assets})






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





#to update the software assets
# def update_software(request, pk):
#     software = get_object_or_404(Software, pk=pk)
    
#     if request.method == 'POST':
#         form = SoftwareForm(request.POST, instance=software)
#         if form.is_valid():
#             updated_software = form.save(commit=False)
#             updated_software.save()  # Save the updated software data
            
#             # Log the updated details in SoftwareUpdateLog with the update_date
#             SoftwareUpdateLog.objects.create(
#                 ASSET_ID=updated_software.ASSET_ID,
#                 brand=updated_software.brand,
#                 model=updated_software.model,
#                 software_version=updated_software.software_version,
#                 date_of_purchase=updated_software.date_of_purchase,
#                 stock_register_number=updated_software.stock_register_number,
#                 account_head=updated_software.account_head,
#                 location=updated_software.location,
#                 update_date=timezone.now()  # Set the update date here
#             )

#             return redirect('dashboard')  # Redirect after update
    
#     else:
#         form = SoftwareForm(instance=software)

#     return render(request, 'AMTSapp/software_asset_update.html', {'form': form, 'software': software})


#modified view to update the software assets
from django.utils import timezone

from django.contrib.auth.models import User  # Ensure this import is present

def update_software(request, pk):
    software = get_object_or_404(Software, pk=pk)
    
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            updated_software = form.save(commit=False)
            updated_software.save()  # Save the updated software data
            
            # Log the updated details in SoftwareUpdateLog with the update_date
            SoftwareUpdateLog.objects.create(
                ASSET_ID=updated_software.ASSET_ID,
                brand=updated_software.brand,
                model=updated_software.model,
                software_version=updated_software.software_version,
                date_of_purchase=updated_software.date_of_purchase,
                stock_register_number=updated_software.stock_register_number,
                account_head=updated_software.account_head,
                location=updated_software.location,
                update_date=request.POST.get('update_date'),  # Get the date from the form
                updated_by=request.POST.get('updated_by'),  # Get the updated_by field from the form
                logged_by=request.user  # Assign the currently logged-in user
            )

            return redirect('dashboard')  # Redirect after update
    
    else:
        form = SoftwareForm(instance=software)

    return render(request, 'AMTSapp/software_asset_update.html', {'form': form, 'software': software})








#to view the software update log
def software_update_log(request):
    logs = SoftwareUpdateLog.objects.all().order_by('-updated_at')
    return render(request, 'AMTSapp/software_update_log.html', {'logs': logs})



def choose_delete_action(request, asset_id):
    asset = get_object_or_404(Software, id=asset_id)
    return render(request, 'AMTSapp/choose_delete_action.html', {'asset': asset})




#view to either make an invalid entry or a scrapped asset
from .models import Software, InvalidSoftwareEntry
from .forms import DeleteSoftwareForm

def confirm_invalid_entry(request, asset_id):
    asset = get_object_or_404(Software, id=asset_id)
    if request.method == 'POST':
        form = DeleteSoftwareForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            
            # Move to Invalid Entry
            InvalidSoftwareEntry.objects.create(
                ASSET_ID=asset.ASSET_ID,
                brand=asset.brand,
                model=asset.model,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.location,
                type_of_asset=asset.type_of_asset,
                software_version=asset.software_version,
                date_of_movement=date_of_movement,
                reason=reason
            )
            asset.delete()
            return redirect('scrapped-log')  # Redirect after moving to invalid entry

    else:
        form = DeleteSoftwareForm()

    return render(request, 'AMTSapp/confirm_invalid_entry.html', {'asset': asset, 'form': form})


from django.shortcuts import get_object_or_404, redirect
from .models import Software, ScrappedSoftwareAsset
from .forms import DeleteSoftwareForm

def confirm_scrapped_asset(request, asset_id):
    asset = get_object_or_404(Software, id=asset_id)
    if request.method == 'POST':
        form = DeleteSoftwareForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            
            # Move to Scrapped Asset
            ScrappedSoftwareAsset.objects.create(
                ASSET_ID=asset.ASSET_ID,
                brand=asset.brand,
                model=asset.model,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.location,
                type_of_asset=asset.type_of_asset,
                software_version=asset.software_version,
                date_of_movement=date_of_movement,
                reason=reason
            )
            asset.delete()
            return redirect('scrapped-log')  # Redirect after moving to scrapped assets

    else:
        form = DeleteSoftwareForm()

    return render(request, 'AMTSapp/confirm_scrapped_asset.html', {'asset': asset, 'form': form})

#view to add the movemet history for software asset
from django.shortcuts import render, get_object_or_404, redirect
from .models import Software, SoftwareMovement
from .forms import SoftwareMovementForm

def move_software(request, id):
    # Get the software asset by its ID
    asset = get_object_or_404(Software, id=id)

    if request.method == 'POST':
        form = SoftwareMovementForm(request.POST)
        if form.is_valid():
            movement = form.save(commit=False)
            movement.software = asset  # Link the movement to the software asset

            # Log the necessary details from the software asset
            movement.asset_id = asset.ASSET_ID
            movement.brand = asset.brand
            movement.model = asset.model
            movement.software_version = asset.software_version
            movement.date_of_purchase = asset.date_of_purchase
            movement.stock_register_number = asset.stock_register_number
            movement.account_head = asset.account_head
            movement.original_location = asset.location

            movement.date_logged = datetime.date.today()  # Log the current date
            movement.save()

            # Delete the original software record (or you can move it elsewhere)
            asset.delete()
            
            # Redirect to the dashboard or another page after moving
            return redirect('movement_history')
        else:
            print(form.errors)  # Debug: print form errors if validation fails
    else:
        form = SoftwareMovementForm()

    return render(request, 'AMTSapp/move_software.html', {'form': form, 'asset': asset})



#view to display the movement history of software assets
from .models import SoftwareMovement

def moved_software_list(request):
    moved_software = SoftwareMovement.objects.all()
    return render(request, 'AMTSapp/moved_software_list.html', {'moved_software': moved_software})











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


#view to update computer assets
# def update_computer_hardware(request, pk):
#     computer_hardware = get_object_or_404(ComputerHardware, pk=pk)
#     if request.method == 'POST':
#         form = ComputerHardwareForm(request.POST, instance=computer_hardware)
#         if form.is_valid():
#             updated_hardware = form.save()

#             # Log the update in ComputerHardwareUpdateLog with the full location name and date of update
#             ComputerHardwareUpdateLog.objects.create(
#                 computer_hardware=updated_hardware,
#                 ASSET_ID=updated_hardware.ASSET_ID,
#                 brand=updated_hardware.brand,
#                 model=updated_hardware.model,
#                 processor=updated_hardware.processor,
#                 processor_generation=updated_hardware.processor_generation,
#                 ram=updated_hardware.ram,
#                 rom=updated_hardware.rom,
#                 motherboard=updated_hardware.motherboard,
#                 power_supply=updated_hardware.power_supply,
#                 graphics_card=updated_hardware.graphics_card,
#                 date_of_purchase=updated_hardware.date_of_purchase,
#                 stock_register_number=updated_hardware.stock_register_number,
#                 account_head=updated_hardware.account_head,
#                 location=updated_hardware.location,  # Use the method here  # Use the full location name
#                 date_of_update=timezone.now(),  # Set the current date as date of update
#             )
#             return redirect('dashboard')  # Redirect to a list or detail view
#     else:
#         form = ComputerHardwareForm(instance=computer_hardware)
    
#     return render(request, 'AMTSapp/update_computer_hardware.html', {'form': form})



#modified view to update the computer hardware
@login_required
def update_computer_hardware(request, pk):
    computer_hardware = get_object_or_404(ComputerHardware, pk=pk)
    if request.method == 'POST':
        form = ComputerHardwareForm(request.POST, instance=computer_hardware)
        if form.is_valid():
            updated_hardware = form.save()

            # Log the update in ComputerHardwareUpdateLog
            ComputerHardwareUpdateLog.objects.create(
                computer_hardware=updated_hardware,
                ASSET_ID=updated_hardware.ASSET_ID,
                brand=updated_hardware.brand,
                model=updated_hardware.model,
                processor=updated_hardware.processor,
                processor_generation=updated_hardware.processor_generation,
                ram=updated_hardware.ram,
                rom=updated_hardware.rom,
                motherboard=updated_hardware.motherboard,
                power_supply=updated_hardware.power_supply,
                graphics_card=updated_hardware.graphics_card,
                date_of_purchase=updated_hardware.date_of_purchase,
                stock_register_number=updated_hardware.stock_register_number,
                account_head=updated_hardware.account_head,
                location=updated_hardware.location,  # Use the location field directly
                date_of_update=timezone.now(),  # Set the current date as date of update
                updated_by=request.POST.get('updated_by'),  # Get updated_by from the form
                logged_by=request.user  # Set the logged-in user
            )
            return redirect('dashboard')  # Redirect to a list or detail view
    else:
        form = ComputerHardwareForm(instance=computer_hardware)
    
    return render(request, 'AMTSapp/update_computer_hardware.html', {'form': form})






#view to display the updated log of computer assets
def computer_hardware_update_log(request):
    logs = ComputerHardwareUpdateLog.objects.all()
    return render(request, 'AMTSapp/computer_hardware_update_log.html', {'logs': logs})




#views to display invalid computer hardware form
from .models import ComputerHardware, InvalidComputerHardwareEntry
from .forms import DeleteHardwareForm

def confirm_invalid_computer_hardware(request, asset_id):
    asset = get_object_or_404(ComputerHardware, id=asset_id)
    if request.method == 'POST':
        form = DeleteHardwareForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            InvalidComputerHardwareEntry.objects.create(
                ASSET_ID=asset.ASSET_ID,
                brand=asset.brand,
                model=asset.model,
                processor=asset.processor,
                processor_generation=asset.processor_generation,
                ram=asset.ram,
                rom=asset.rom,
                motherboard=asset.motherboard,
                power_supply=asset.power_supply,
                graphics_card=asset.graphics_card,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.get_location_display(),
                date_of_movement=date_of_movement,
                reason=reason
            )
            asset.delete()
            return redirect('scrapped-log')  # Adjust redirect as needed
    else:
        form = DeleteHardwareForm()

    return render(request, 'AMTSapp/confirm_invalid_hardware.html', {'asset': asset, 'form': form})


#view to display scrapped computer hardware asset form
from .models import ComputerHardware, ScrappedComputerHardwareAsset
from .forms import DeleteHardwareForm

def confirm_scrapped_computer_hardware(request, asset_id):
    asset = get_object_or_404(ComputerHardware, id=asset_id)
    if request.method == 'POST':
        form = DeleteHardwareForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            ScrappedComputerHardwareAsset.objects.create(
                ASSET_ID=asset.ASSET_ID,
                brand=asset.brand,
                model=asset.model,
                processor=asset.processor,
                processor_generation=asset.processor_generation,
                ram=asset.ram,
                rom=asset.rom,
                motherboard=asset.motherboard,
                power_supply=asset.power_supply,
                graphics_card=asset.graphics_card,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.get_location_display(),
                date_of_movement=date_of_movement,
                reason=reason
            )
            asset.delete()
            return redirect('scrapped-log')  # Adjust redirect as needed
    else:
        form = DeleteHardwareForm()

    return render(request, 'AMTSapp/confirm_scrapped_hardware.html', {'asset': asset, 'form': form})


#views to render the invalid and scrapped data for the computer hardware
def invalid_computer_hardware(request):
    invalid_assets = InvalidComputerHardwareEntry.objects.all()
    return render(request, 'AMTSapp/invalid_computer_hardware.html', {'invalid_assets': invalid_assets})

def scrapped_computer_hardware(request):
    scrapped_assets = ScrappedComputerHardwareAsset.objects.all()
    return render(request, 'AMTSapp/scrapped_computer_hardware.html', {'scrapped_assets': scrapped_assets})




#view to render the movement history form for computer hardware form
from .models import ComputerHardware, ComputerHardwareMovement
from .forms import ComputerHardwareMovementForm

def move_computer_hardware(request, asset_id):
    hardware = get_object_or_404(ComputerHardware, id=asset_id)
    
    if request.method == 'POST':
        form = ComputerHardwareMovementForm(request.POST)
        if form.is_valid():
            movement_type = form.cleaned_data['movement_type']
            new_location = form.cleaned_data['new_location']
            reason = form.cleaned_data['reason']
            date_of_movement = form.cleaned_data['date_of_movement']
            
            # Log the movement
            ComputerHardwareMovement.log_movement(
                hardware=hardware,
                movement_type=movement_type,
                new_location=new_location,
                reason=reason,
                date_of_movement=date_of_movement
            )
            
            # Delete the original hardware record after moving
            hardware.delete()
            
            return redirect('movement_history')
    else:
        form = ComputerHardwareMovementForm()
    
    return render(request, 'AMTSapp/move_computer_hardware.html', {'form': form, 'hardware': hardware})


#view to render the moved computer hardware list
from .models import ComputerHardwareMovement

def moved_computer_hardware_list(request):
    movements = ComputerHardwareMovement.objects.all()
    return render(request, 'AMTSapp/moved_computer_hardware_list.html', {'movements': movements})




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


#to render the projector update form 
from .models import Projector, ProjectorUpdateLog

# def update_projector(request, id):
#     projector = get_object_or_404(Projector, id=id)
#     if request.method == 'POST':
#         form = ProjectorForm(request.POST, instance=projector)
#         if form.is_valid():
#             updated_projector = form.save()

#             # Log the update
#             ProjectorUpdateLog.objects.create(
#                 projector=updated_projector,
#                 updated_date=timezone.now(),
#                 brand=updated_projector.brand,
#                 model=updated_projector.model,
#                 resolution=updated_projector.resolution,
#                 lumens=updated_projector.lumens,
#                 contrast_ratio=updated_projector.contrast_ratio,
#                 connectivity=updated_projector.connectivity,
#                 lamp_life_hours=updated_projector.lamp_life_hours,
#                 date_of_purchase=updated_projector.date_of_purchase,
#                 stock_register_number=updated_projector.stock_register_number,
#                 account_head=updated_projector.account_head,
#                 location=dict(Projector.LOCATIONS)[updated_projector.location]  # Full location name
#             )
#             return redirect('dashboard')

#     else:
#         form = ProjectorForm(instance=projector)
#     return render(request, 'AMTSapp/update_projector.html', {'form': form})



#modified view to update the form and render it
from .forms import ProjectorForm  # Ensure this imports your form

def update_projector(request, id):
    projector = get_object_or_404(Projector, id=id)
    if request.method == 'POST':
        form = ProjectorForm(request.POST, instance=projector)
        if form.is_valid():
            updated_projector = form.save()

            # Log the update
            ProjectorUpdateLog.objects.create(
                projector=updated_projector,
                updated_date=timezone.now(),
                brand=updated_projector.brand,
                model=updated_projector.model,
                resolution=updated_projector.resolution,
                lumens=updated_projector.lumens,
                contrast_ratio=updated_projector.contrast_ratio,
                connectivity=updated_projector.connectivity,
                lamp_life_hours=updated_projector.lamp_life_hours,
                date_of_purchase=updated_projector.date_of_purchase,
                stock_register_number=updated_projector.stock_register_number,
                account_head=updated_projector.account_head,
                location=updated_projector.location,  # Use the location directly
                updated_by=request.POST.get('updated_by'),  # Capture updated_by from form
                logged_by=request.user.username  # Get the currently logged-in user's username
            )
            return redirect('dashboard')

    else:
        form = ProjectorForm(instance=projector)

    return render(request, 'AMTSapp/update_projector.html', {'form': form})






#view to display the projector update log
def projector_update_log(request):
    logs = ProjectorUpdateLog.objects.all()
    return render(request, 'AMTSapp/projector-update-log.html', {'logs': logs})

from .models import Projector, InvalidProjectorEntry, ScrappedProjectorAsset
from .forms import DeleteProjectorForm

# View to move a specific projector to invalid
def invalid_projector(request, asset_id):
    asset = get_object_or_404(Projector, id=asset_id)
    if request.method == 'POST':
        form = DeleteProjectorForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            InvalidProjectorEntry.objects.create(
                ASSET_ID=asset.ASSET_ID,
                brand=asset.brand,
                model=asset.model,
                resolution=asset.resolution,
                lumens=asset.lumens,
                contrast_ratio=asset.contrast_ratio,
                connectivity=asset.connectivity,
                lamp_life_hours=asset.lamp_life_hours,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.get_location_display(),
                type_of_asset=asset.type_of_asset,
                date_of_movement=date_of_movement,
                reason=reason
            )
            asset.delete()
            return redirect('scrapped-log')
    else:
        form = DeleteProjectorForm()
    
    return render(request, 'AMTSapp/confirm_invalid_projector.html', {'asset': asset, 'form': form})

# View to move a specific projector to scrapped
def scrapped_projector(request, asset_id):
    asset = get_object_or_404(Projector, id=asset_id)
    if request.method == 'POST':
        form = DeleteProjectorForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            ScrappedProjectorAsset.objects.create(
                ASSET_ID=asset.ASSET_ID,
                brand=asset.brand,
                model=asset.model,
                resolution=asset.resolution,
                lumens=asset.lumens,
                contrast_ratio=asset.contrast_ratio,
                connectivity=asset.connectivity,
                lamp_life_hours=asset.lamp_life_hours,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.get_location_display(),
                type_of_asset=asset.type_of_asset,
                date_of_movement=date_of_movement,
                reason=reason,
                # date_logged = date_logged,
            )
            asset.delete()
            return redirect('scrapped-log')
    else:
        form = DeleteProjectorForm()
    
    return render(request, 'AMTSapp/confirm_scrapped_projector.html', {'asset': asset, 'form': form})

# Views to display invalid and scrapped assets
def invalid_projector_log(request):
    invalid_projectors = InvalidProjectorEntry.objects.all()
    return render(request, 'AMTSapp/invalid_projector_list.html', {'invalid_projectors': invalid_projectors})

def scrapped_projector_log(request):
    scrapped_projectors = ScrappedProjectorAsset.objects.all()
    return render(request, 'AMTSapp/scrapped_projector_list.html', {'scrapped_projectors': scrapped_projectors})




#view to display the movement history form for projector assets
from .models import Projector, ProjectorMovement
from .forms import ProjectorMovementForm
from django.urls import reverse

from .models import Projector, ProjectorMovement
from .forms import ProjectorMovementForm

def move_projector(request, id):
    projector = get_object_or_404(Projector, id=id)
    
    if request.method == 'POST':
        form = ProjectorMovementForm(request.POST)
        if form.is_valid():
            movement = form.save(commit=False)  # Create the movement instance but don't save yet
            ProjectorMovement.log_movement(
                projector=projector,
                movement_type=movement.movement_type,
                new_location=movement.new_location,
                reason=movement.reason,
                date_of_movement=movement.date_of_movement
            )
            projector.delete()  # Delete the projector after logging movement
            return redirect('movement_history')  # Redirect after successful save
        else:
            print(form.errors)  # Debugging: Print errors to console
    else:
        form = ProjectorMovementForm()

    return render(request, 'AMTSapp/move_projector.html', {'form': form, 'projector': projector})



def moved_projector_list(request):
    movements = ProjectorMovement.objects.all()
    return render(request, 'AMTSapp/moved_projector_list.html', {'movements': movements})















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



#to render the update books form 
from .models import Books, BookUpdateLog

# def update_book(request, pk):
#     book = get_object_or_404(Books, pk=pk)
    
#     if request.method == 'POST':
#         form = BooksForm(request.POST, instance=book)
#         date_of_update = request.POST.get('date_of_update')  # Get the update date from the form

#         if form.is_valid() and date_of_update:
#             updated_book = form.save()

#             # Create log entry
#             BookUpdateLog.objects.create(
#                 book=book,
#                 title=updated_book.title,
#                 publisher=updated_book.publisher,
#                 author=updated_book.author,
#                 publishing_house=updated_book.publishing_house,
#                 edition=updated_book.edition,
#                 date_of_purchase=updated_book.date_of_purchase,
#                 stock_register_number=updated_book.stock_register_number,
#                 account_head=updated_book.account_head,
#                 location=updated_book.get_location_display(),
#                 date_logged=timezone.now(),
#                 date_of_update=date_of_update  # Manually entered date
#             )

#             return redirect('dashboard')

#     else:
#         form = BooksForm(instance=book)

#     return render(request, 'AMTSapp/update_book.html', {'form': form, 'book': book})


#modified view to accomodate the two extra fields in update book model

from .forms import BookUpdateForm  # Ensure you're importing the correct form

def update_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            updated_book = form.save()

            # Log the update
            BookUpdateLog.objects.create(
                book=updated_book,  # Set the book instance here
                date_of_update=form.cleaned_data['date_of_update'],  # Use cleaned data for date of update
                title=updated_book.title,
                publisher=updated_book.publisher,
                author=updated_book.author,
                publishing_house=updated_book.publishing_house,
                edition=updated_book.edition,
                date_of_purchase=updated_book.date_of_purchase,
                stock_register_number=updated_book.stock_register_number,
                account_head=updated_book.account_head,
                location=updated_book.location,
                updated_by=form.cleaned_data['updated_by'],  # Capture updated_by from form
                logged_by=request.user.username  # Get the currently logged-in user's username
            )
            return redirect('dashboard')
        else:
            print(form.errors)  # Print form errors to understand what went wrong
    else:
        form = BookUpdateForm(instance=book)

    return render(request, 'AMTSapp/update_book.html', {'form': form})









#view to render the books update log
def book_update_log(request):
    logs = BookUpdateLog.objects.all()
    return render(request, 'AMTSapp/book_update_log.html', {'logs': logs})



#view to render the invalid entry book form
from .models import InvalidBookEntry
from .forms import InvalidBookForm

def invalid_book(request, asset_id):
    book = get_object_or_404(Books, id=asset_id)
    
    if request.method == 'POST':
        form = InvalidBookForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            
            InvalidBookEntry.objects.create(
                ASSET_ID=book.ASSET_ID,
                title=book.title,
                publisher=book.publisher,
                author=book.author,
                publishing_house=book.publishing_house,
                edition=book.edition,
                date_of_purchase=book.date_of_purchase,
                stock_register_number=book.stock_register_number,
                account_head=book.account_head,
                location=book.get_location_display(),
                date_of_movement=date_of_movement,
                reason=reason
            )
            book.delete()
            return redirect('scrapped-log')
    else:
        form = InvalidBookForm()
    
    return render(request, 'AMTSapp/confirm_invalid_book.html', {'book': book, 'form': form})



#view to render the scrapped book form
from .models import ScrappedBookAsset
from .forms import ScrappedBookForm

def scrapped_book(request, asset_id):
    book = get_object_or_404(Books, id=asset_id)
    
    if request.method == 'POST':
        form = ScrappedBookForm(request.POST)
        if form.is_valid():
            date_of_movement = form.cleaned_data['date_of_movement']
            reason = form.cleaned_data['reason']
            
            ScrappedBookAsset.objects.create(
                ASSET_ID=book.ASSET_ID,
                title=book.title,
                publisher=book.publisher,
                author=book.author,
                publishing_house=book.publishing_house,
                edition=book.edition,
                date_of_purchase=book.date_of_purchase,
                stock_register_number=book.stock_register_number,
                account_head=book.account_head,
                location=book.get_location_display(),
                date_of_movement=date_of_movement,
                reason=reason
            )
            book.delete()
            return redirect('scrapped-log')
    else:
        form = ScrappedBookForm()
    
    return render(request, 'AMTSapp/confirm_scrapped_book.html', {'book': book, 'form': form})




# View to display the list of invalid books
def list_invalid_books(request):
    invalid_books = InvalidBookEntry.objects.all()
    return render(request, 'AMTSapp/invalid_books_list.html', {'invalid_books': invalid_books})

# View to display the list of scrapped books
def list_scrapped_books(request):
    scrapped_books = ScrappedBookAsset.objects.all()
    return render(request, 'AMTSapp/scrapped_books_list.html', {'scrapped_books': scrapped_books})



#view to render the movement history form for books
from .models import Books, MovedBooks
from .forms import MovedBooksForm

def move_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = MovedBooksForm(request.POST)
        if form.is_valid():
            moved_book = form.save(commit=False)
            # Populate fields with data from the original book
            moved_book.ASSET_ID = book.ASSET_ID
            moved_book.type_of_asset = book.type_of_asset
            moved_book.title = book.title
            moved_book.publisher = book.publisher
            moved_book.author = book.author
            moved_book.publishing_house = book.publishing_house
            moved_book.edition = book.edition
            moved_book.date_of_purchase = book.date_of_purchase
            moved_book.stock_register_number = book.stock_register_number
            moved_book.account_head = book.account_head
            moved_book.original_location = book.location  # Set original location

            moved_book.save()  # Save the moved book to the database
            
            # Delete the original book entry after moving
            book.delete()
            return redirect('movement_history')  # Adjust the redirect as necessary
    else:
        form = MovedBooksForm()  # No need to pass book if it's not used

    return render(request, 'AMTSapp/move_book.html', {'form': form, 'book': book})



#view to render the moved books list
def moved_books_list(request):
    moved_books = MovedBooks.objects.all()
    return render(request, 'AMTSapp/moved_book_list.html', {'moved_books': moved_books})



#to render the computer peripherals form
from .forms import ComputerPeripheralsForm

def add_peripheral(request):
    if request.method == 'POST':
        form = ComputerPeripheralsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_types')  # Replace 'asset_types' with your desired redirect URL
    else:
        form = ComputerPeripheralsForm()
    return render(request, 'AMTSapp/computer-peripherals.html', {'form': form})


#to render the computer peripheral update form
from .models import ComputerPeripherals, ComputerPeripheralsUpdateLog

# def update_computer_peripheral(request, pk):
#     peripheral = get_object_or_404(ComputerPeripherals, pk=pk)

#     if request.method == 'POST':
#         form = ComputerPeripheralsForm(request.POST, instance=peripheral)
#         if form.is_valid():
#             # Save the form
#             form.save()

#             # Create a log entry
#             ComputerPeripheralsUpdateLog.objects.create(
#                 peripheral=peripheral,
#                 peripheral_type=peripheral.peripheral_type,
#                 brand=peripheral.brand,
#                 model=peripheral.model,
#                 date_of_purchase=peripheral.date_of_purchase,
#                 stock_register_number=peripheral.stock_register_number,
#                 account_head=peripheral.account_head,
#                 location=peripheral.location,
#                 date_of_update=request.POST.get('date_of_update')  # Manual update date entry
#             )

#             return redirect('dashboard')  # Redirect to the list of peripherals

#     else:
#         form = ComputerPeripheralsForm(instance=peripheral)

#     return render(request, 'AMTSapp/update_computer_peripheral.html', {'form': form, 'peripheral': peripheral})



#modified view to render the update form for computer peripherals
from .models import ComputerPeripherals, ComputerPeripheralsUpdateLog
from .forms import ComputerPeripheralsForm

def update_computer_peripheral(request, pk):
    peripheral = get_object_or_404(ComputerPeripherals, pk=pk)

    if request.method == 'POST':
        form = ComputerPeripheralsForm(request.POST, instance=peripheral)
        if form.is_valid():
            # Save the updated peripheral
            updated_peripheral = form.save()

            # Create a log entry
            ComputerPeripheralsUpdateLog.objects.create(
                peripheral=updated_peripheral,
                peripheral_type=updated_peripheral.peripheral_type,
                brand=updated_peripheral.brand,
                model=updated_peripheral.model,
                date_of_purchase=updated_peripheral.date_of_purchase,
                stock_register_number=updated_peripheral.stock_register_number,
                account_head=updated_peripheral.account_head,
                location=updated_peripheral.location,
                date_of_update=request.POST.get('date_of_update'),  # Manual update date entry
                updated_by=request.POST.get('updated_by'),  # Capture updated_by from form
                logged_by=request.user.username  # Get the currently logged-in user's username
            )

            return redirect('dashboard')  # Redirect to the list of peripherals

    else:
        form = ComputerPeripheralsForm(instance=peripheral)

    return render(request, 'AMTSapp/update_computer_peripheral.html', {'form': form, 'peripheral': peripheral})













#to render the computer peripherals update log
def all_peripheral_update_logs(request):
    logs = ComputerPeripheralsUpdateLog.objects.all().order_by('-date_logged')  # List all logs, ordered by the most recent log first
    return render(request, 'AMTSapp/peripheral_update_log.html', {'logs': logs})



#to render the form for invalid computer peripherals form and the scrapped assets form
from django.shortcuts import render, get_object_or_404, redirect
from .models import ComputerPeripherals, InvalidComputerPeripherals, ScrappedComputerPeripherals
from .forms import InvalidComputerPeripheralsForm, ScrappedComputerPeripheralsForm

# View for moving an asset to invalid entry
def move_to_invalid_computer_peripherals(request, asset_id):
    asset = get_object_or_404(ComputerPeripherals, id=asset_id)
    
    if request.method == 'POST':
        form = InvalidComputerPeripheralsForm(request.POST)
        if form.is_valid():
            # Create an InvalidComputerPeripherals object
            invalid_asset = InvalidComputerPeripherals.objects.create(
                ASSET_ID=asset.ASSET_ID,
                peripheral_type=asset.peripheral_type,
                brand=asset.brand,
                model=asset.model,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.location,
                date_of_movement=form.cleaned_data['date_of_movement'],
                reason=form.cleaned_data['reason'],
                date_logged=datetime.date.today()
            )
            invalid_asset.save()
            asset.delete()  # Remove from main table
            return redirect('scrapped-log')
    else:
        form = InvalidComputerPeripheralsForm()
    
    return render(request, 'AMTSapp/confirm_invalid_computer_peripheral.html', {'asset': asset, 'form': form})

# View for moving an asset to scrapped assets
def move_to_scrapped_computer_peripherals(request, asset_id):
    asset = get_object_or_404(ComputerPeripherals, id=asset_id)
    
    if request.method == 'POST':
        form = ScrappedComputerPeripheralsForm(request.POST)
        if form.is_valid():
            # Create a ScrappedComputerPeripherals object
            scrapped_asset = ScrappedComputerPeripherals.objects.create(
                ASSET_ID=asset.ASSET_ID,
                peripheral_type=asset.peripheral_type,
                brand=asset.brand,
                model=asset.model,
                date_of_purchase=asset.date_of_purchase,
                stock_register_number=asset.stock_register_number,
                account_head=asset.account_head,
                location=asset.location,
                date_of_movement=form.cleaned_data['date_of_movement'],
                reason=form.cleaned_data['reason'],
                date_logged=datetime.date.today()
            )
            scrapped_asset.save()
            asset.delete()  # Remove from main table
            return redirect('scrapped-log')
    else:
        form = ScrappedComputerPeripheralsForm()
    
    return render(request, 'AMTSapp/confirm_scrapped_computer_peripherals.html', {'asset': asset, 'form': form})




#views to render the invalid and scrapped computer peripherals asset list
def invalid_computer_peripherals_list(request):
    invalid_assets = InvalidComputerPeripherals.objects.all()
    return render(request, 'AMTSapp/invalid_computer_peripherals_list.html', {'invalid_assets': invalid_assets})

def scrapped_computer_peripherals_list(request):
    scrapped_assets = ScrappedComputerPeripherals.objects.all()
    return render(request, 'AMTSapp/scrapped_computer_peripherals.html', {'scrapped_assets': scrapped_assets})


#view to render the movement history form for computer peripherals
from .models import ComputerPeripherals, MovedComputerPeripherals
from .forms import MovedComputerPeripheralsForm

# View to move a computer peripheral
def move_peripheral(request, pk):
    peripheral = get_object_or_404(ComputerPeripherals, pk=pk)
    if request.method == 'POST':
        form = MovedComputerPeripheralsForm(request.POST)
        if form.is_valid():
            moved_peripheral = form.save(commit=False)
            # Copying data from the original model
            moved_peripheral.original_location = peripheral.location
            moved_peripheral.ASSET_ID = peripheral.ASSET_ID
            moved_peripheral.type_of_asset = peripheral.type_of_asset
            moved_peripheral.peripheral_type = peripheral.peripheral_type
            moved_peripheral.brand = peripheral.brand
            moved_peripheral.model = peripheral.model
            moved_peripheral.date_of_purchase = peripheral.date_of_purchase
            moved_peripheral.stock_register_number = peripheral.stock_register_number
            moved_peripheral.account_head = peripheral.account_head

            # Save the moved peripheral
            moved_peripheral.save()

            # Delete the original peripheral record
            peripheral.delete()

            return redirect('movement_history')
        else:
            print(form.errors)  # Debugging line to print form errors
    else:
        form = MovedComputerPeripheralsForm()

    return render(request, 'AMTSapp/move_peripheral.html', {'form': form, 'peripheral': peripheral})


# View to list all moved computer peripherals list
def moved_peripherals_list(request):
    moved_peripherals = MovedComputerPeripherals.objects.all()
    return render(request, 'AMTSapp/moved_peripherals.html', {'moved_peripherals': moved_peripherals})



#to add a furniture asset into the database
#view to enter the furniture asset into the database
from .forms import FurnitureForm  # Import your form
from django.contrib import messages

def add_furniture(request):
    if request.method == 'POST':
        form = FurnitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_types')  # Replace 'asset_types' with your desired redirect URL
        else:
            print(form.errors) 
    else:
        form = FurnitureForm()
    return render(request, 'AMTSapp/furniture-asset.html', {'form': form})




#View to render the update form for a furniture asset 
from .models import Furniture, FurnitureUpdateLog
from .forms import FurnitureUpdateLogForm

def update_furniture(request, pk):
    furniture = get_object_or_404(Furniture, pk=pk)

    if request.method == 'POST':
        form = FurnitureForm(request.POST, instance=furniture)
        if form.is_valid():
            updated_furniture = form.save()

            # Create an update log entry and make sure to set the furniture field
            FurnitureUpdateLog.objects.create(
                furniture=updated_furniture,  # Set the furniture instance
                type_of_furniture=updated_furniture.type_of_furniture,
                subtype=updated_furniture.subtype,
                date_of_purchase=updated_furniture.date_of_purchase,
                account_head=updated_furniture.account_head,
                location=updated_furniture.location,
                date_of_update=request.POST.get('date_of_update'),  # Manual date entry
                updated_by=request.POST.get('updated_by'),  # Get the updated_by field
                logged_by=request.user.username  # Get the currently logged-in user
            )

            return redirect('dashboard')  # Redirect after updating
    else:
        form = FurnitureForm(instance=furniture)

    return render(request, 'AMTSapp/update_furniture.html', {'form': form, 'furniture': furniture})




#view to render the update log 
def furniture_update_logs(request):
    logs = FurnitureUpdateLog.objects.all()
    return render(request, 'AMTSapp/furniture_update_logs.html', {'logs': logs})







#view to render the invalid and scrapped assets form 
from .forms import InvalidFurnitureForm, ScrappedFurnitureForm
from .models import Furniture, InvalidFurniture, ScrappedFurniture

# View for moving furniture to invalid
# View for moving furniture to invalid
def move_to_invalid_furniture(request, asset_id):
    furniture = get_object_or_404(Furniture, ASSET_ID=asset_id)

    if request.method == 'POST':
        form = InvalidFurnitureForm(request.POST)
        if form.is_valid():
            invalid_furniture = form.save(commit=False)
            invalid_furniture.ASSET_ID = furniture.ASSET_ID
            invalid_furniture.type_of_furniture = furniture.type_of_furniture
            invalid_furniture.subtype = furniture.subtype
            invalid_furniture.date_of_purchase = furniture.date_of_purchase
            invalid_furniture.account_head = furniture.account_head
            invalid_furniture.location = furniture.location
            invalid_furniture.save()
            furniture.delete()
            return redirect('scrapped-log')
    else:
        form = InvalidFurnitureForm()

    return render(request, 'AMTSapp/confirm_invalid_furniture.html', {
        'form': form,
        'furniture': furniture
    })






# View for moving furniture to scrapped
def move_to_scrapped_furniture(request, asset_id):
    furniture = get_object_or_404(Furniture, ASSET_ID=asset_id)  # Fetch the original furniture

    if request.method == 'POST':
        form = ScrappedFurnitureForm(request.POST)
        if form.is_valid():
            scrapped_furniture = form.save(commit=False)
            scrapped_furniture.ASSET_ID = furniture.ASSET_ID  # Set non-editable fields manually
            scrapped_furniture.type_of_furniture = furniture.type_of_furniture
            scrapped_furniture.subtype = furniture.subtype
            scrapped_furniture.date_of_purchase = furniture.date_of_purchase
            scrapped_furniture.account_head = furniture.account_head
            scrapped_furniture.location = furniture.location
            scrapped_furniture.save()  # Save scrapped entry
            furniture.delete()  # Delete original furniture record
            return redirect('scrapped-log')  # Redirect after successful movement
    else:
        form = ScrappedFurnitureForm()

    return render(request, 'AMTSapp/confirm_scrapped_furniture.html', {
        'form': form,
        'furniture': furniture,  # Pass the original furniture data for display
    })





#view to display the invalid and scrapped furniture assets
from .models import InvalidFurniture, ScrappedFurniture

def invalid_furniture_list(request):
    invalid_furniture = InvalidFurniture.objects.all()
    return render(request, 'AMTSapp/invalid_furniture_list.html', {'invalid_furniture': invalid_furniture})

def scrapped_furniture_list(request):
    scrapped_furniture = ScrappedFurniture.objects.all()
    return render(request, 'AMTSapp/scrapped_furniture_list.html', {'scrapped_furniture': scrapped_furniture})









#view to enter the staff room assets
from .models import ProfessorAssets
from .forms import ProfessorAssetsForm
from django.contrib.auth.decorators import login_required

@login_required
def add_professor_assets(request):
    if request.method == 'POST':
        form = ProfessorAssetsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a suitable page after saving
    else:
        form = ProfessorAssetsForm()

    return render(request, 'AMTSapp/add_professor_assets.html', {'form': form})




from django.shortcuts import render
from .models import ProfessorAssets

def professor_assets_list(request):
    professor_assets = ProfessorAssets.objects.all()
    return render(request, 'AMTSapp/professor_assets.html', {
        'professor_assets': professor_assets,
    })


# from django.shortcuts import render, get_object_or_404
# from .models import ProfessorAssets  # Import your model here

# def display_professor_assets(request, professor_id):
#     # Get the professor's assets based on the professor's ID
#     professor_assets = get_object_or_404(ProfessorAssets, id=professor_id)

#     context = {
#         'professor_assets': professor_assets,
#     }

#     return render(request, 'AMTSapp/professor_assets.html', context)


















# from .models import ComputerHardware, Projector, Software, Books, ComputerPeripherals

# def assets_by_location(request, location):
#     computer_hardware_assets = ComputerHardware.objects.filter(location=location)
#     projector_assets = Projector.objects.filter(location=location)
#     software_assets = Software.objects.filter(location=location)
#     books_assets = Books.objects.filter(location=location)
#     computer_peripherals_assets = ComputerPeripherals.objects.filter(location=location)
    
#     grouped_assets = {
#         'computer_hardware': computer_hardware_assets,
#         'projector': projector_assets,
#         'software': software_assets,
#         'books': books_assets,
#         'computer_peripherals': computer_peripherals_assets,
#     }
    
#     return render(request, 'AMTSapp/assets_by_location.html', {
#         'grouped_assets': grouped_assets,
#         'location': location
#     })
















from .models import ComputerHardware, Projector, Software, Books, ComputerPeripherals, Furniture  # Make sure to import Furniture

def assets_by_location(request, location):
    computer_hardware_assets = ComputerHardware.objects.filter(location=location)
    projector_assets = Projector.objects.filter(location=location)
    software_assets = Software.objects.filter(location=location)
    books_assets = Books.objects.filter(location=location)
    computer_peripherals_assets = ComputerPeripherals.objects.filter(location=location)
    furniture_assets = Furniture.objects.filter(location=location)  # Added this line for furniture

    grouped_assets = {
        'computer_hardware': computer_hardware_assets,
        'projector': projector_assets,
        'software': software_assets,
        'books': books_assets,
        'computer_peripherals': computer_peripherals_assets,
        'furniture': furniture_assets,  # Added furniture to the grouped assets
    }

    return render(request, 'AMTSapp/assets_by_location.html', {
        'grouped_assets': grouped_assets,
        'location': location
    })






#to render the user dashboard without the icons
# from django.shortcuts import render
# from .models import ComputerHardware, Projector, Software, Books, ComputerPeripherals  # Import your models

# def assets_by_location_user(request, location):
#     # Fetch assets for the specified location
#     computer_hardware_assets = ComputerHardware.objects.filter(location=location)
#     projector_assets = Projector.objects.filter(location=location)
#     software_assets = Software.objects.filter(location=location)
#     books_assets = Books.objects.filter(location=location)
#     computer_peripherals_assets = ComputerPeripherals.objects.filter(location=location)
    
#     # Group assets for rendering
#     grouped_assets = {
#         'computer_hardware': computer_hardware_assets,
#         'projector': projector_assets,
#         'software': software_assets,
#         'books': books_assets,
#         'computer_peripherals': computer_peripherals_assets,
#     }
    
#     # Render the user view template
#     return render(request, 'AMTSapp/assets_by_location_user.html', {
#         'grouped_assets': grouped_assets,
#         'location': location
#     })


from .models import ComputerHardware, Projector, Software, Books, ComputerPeripherals, Furniture  # Import Furniture model

def assets_by_location_user(request, location):
    # Fetch assets for the specified location
    computer_hardware_assets = ComputerHardware.objects.filter(location=location)
    projector_assets = Projector.objects.filter(location=location)
    software_assets = Software.objects.filter(location=location)
    books_assets = Books.objects.filter(location=location)
    computer_peripherals_assets = ComputerPeripherals.objects.filter(location=location)
    furniture_assets = Furniture.objects.filter(location=location)  # Added line to fetch furniture assets

    # Group assets for rendering
    grouped_assets = {
        'computer_hardware': computer_hardware_assets,
        'projector': projector_assets,
        'software': software_assets,
        'books': books_assets,
        'computer_peripherals': computer_peripherals_assets,
        'furniture': furniture_assets,  # Added furniture to the grouped assets
    }
    
    # Render the user view template
    return render(request, 'AMTSapp/assets_by_location_user.html', {
        'grouped_assets': grouped_assets,
        'location': location
    })









