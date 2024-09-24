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
                update_date=timezone.now()  # Set the update date here
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
def update_computer_hardware(request, pk):
    computer_hardware = get_object_or_404(ComputerHardware, pk=pk)
    if request.method == 'POST':
        form = ComputerHardwareForm(request.POST, instance=computer_hardware)
        if form.is_valid():
            updated_hardware = form.save()

            # Log the update in ComputerHardwareUpdateLog with the full location name and date of update
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
                location=updated_hardware.location,  # Use the method here  # Use the full location name
                date_of_update=timezone.now(),  # Set the current date as date of update
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
                location=dict(Projector.LOCATIONS)[updated_projector.location]  # Full location name
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

def update_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        date_of_update = request.POST.get('date_of_update')  # Get the update date from the form

        if form.is_valid() and date_of_update:
            updated_book = form.save()

            # Create log entry
            BookUpdateLog.objects.create(
                book=book,
                title=updated_book.title,
                publisher=updated_book.publisher,
                author=updated_book.author,
                publishing_house=updated_book.publishing_house,
                edition=updated_book.edition,
                date_of_purchase=updated_book.date_of_purchase,
                stock_register_number=updated_book.stock_register_number,
                account_head=updated_book.account_head,
                location=updated_book.get_location_display(),
                date_logged=timezone.now(),
                date_of_update=date_of_update  # Manually entered date
            )

            return redirect('dashboard')

    else:
        form = BooksForm(instance=book)

    return render(request, 'AMTSapp/update_book.html', {'form': form, 'book': book})


#view to render the books update log
def book_update_log(request):
    logs = BookUpdateLog.objects.all()
    return render(request, 'AMTSapp/book_update_log.html', {'logs': logs})




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

def update_computer_peripheral(request, pk):
    peripheral = get_object_or_404(ComputerPeripherals, pk=pk)

    if request.method == 'POST':
        form = ComputerPeripheralsForm(request.POST, instance=peripheral)
        if form.is_valid():
            # Save the form
            form.save()

            # Create a log entry
            ComputerPeripheralsUpdateLog.objects.create(
                peripheral=peripheral,
                peripheral_type=peripheral.peripheral_type,
                brand=peripheral.brand,
                model=peripheral.model,
                date_of_purchase=peripheral.date_of_purchase,
                stock_register_number=peripheral.stock_register_number,
                account_head=peripheral.account_head,
                location=peripheral.location,
                date_of_update=request.POST.get('date_of_update')  # Manual update date entry
            )

            return redirect('dashboard')  # Redirect to the list of peripherals

    else:
        form = ComputerPeripheralsForm(instance=peripheral)

    return render(request, 'AMTSapp/update_computer_peripheral.html', {'form': form, 'peripheral': peripheral})



#to render the computer peripherals update log
def all_peripheral_update_logs(request):
    logs = ComputerPeripheralsUpdateLog.objects.all().order_by('-date_logged')  # List all logs, ordered by the most recent log first
    return render(request, 'AMTSapp/peripheral_update_log.html', {'logs': logs})













from .models import ComputerHardware, Projector, Software, Books, ComputerPeripherals

def assets_by_location(request, location):
    computer_hardware_assets = ComputerHardware.objects.filter(location=location)
    projector_assets = Projector.objects.filter(location=location)
    software_assets = Software.objects.filter(location=location)
    books_assets = Books.objects.filter(location=location)
    computer_peripherals_assets = ComputerPeripherals.objects.filter(location=location)
    
    grouped_assets = {
        'computer_hardware': computer_hardware_assets,
        'projector': projector_assets,
        'software': software_assets,
        'books': books_assets,
        'computer_peripherals': computer_peripherals_assets,
    }
    
    return render(request, 'AMTSapp/assets_by_location.html', {
        'grouped_assets': grouped_assets,
        'location': location
    })




