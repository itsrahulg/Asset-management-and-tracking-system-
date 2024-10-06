from typing import Any

from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm




#login form
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})






#signup form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

    

#to toggle the admin status
class UserRoleForm(forms.ModelForm):
    is_admin = forms.BooleanField(required=False, label="Admin")

    class Meta:
        model = User
        fields = ['is_admin']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['is_admin'].initial = self.instance.is_superuser




#to input an software asset into the database
from .models import Software

# class SoftwareForm(forms.ModelForm):
#     class Meta:
#         model = Software
#         fields = [
#             'ASSET_ID',
#             'brand',
#             'model',
#             'date_of_purchase',
#             'stock_register_number',
#             'account_head',
#             'location',
#             'type_of_asset',
#             'software_version',
#         ]
#         widgets = {
#             'ASSET_ID': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'SW-XXX'
#             }),
#             'brand': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Brand name'
#             }),
#             'model': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Model number'
#             }),
#             'date_of_purchase': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date'
#             }),
#             'stock_register_number': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': '0'
#             }),
#             'account_head': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Acc Head'
#             }),
#             'location': forms.Select(attrs={'class': 'form-control'}),
#             'type_of_asset': forms.HiddenInput(attrs={
#                 'value': 'software'
#             }),  # Hidden field with default value
#             'software_version': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': '1.0'
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super(SoftwareForm, self).__init__(*args, **kwargs)
#         # Optional: Customize form layout or field attributes here
#         for field in self.fields.values():
#             if field.widget.attrs.get('class') != 'form-control':
#                 field.widget.attrs['class'] = 'form-control'

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = [
            'ASSET_ID',
            'brand',
            'model',
            'date_of_purchase',
            'stock_register_number',
            'account_head',
            'location',
            'type_of_asset',
            'software_version',
        ]
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'SW-XXX'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Brand name'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Model number'
            }),
            'date_of_purchase': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'stock_register_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
            'account_head': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Acc Head'
            }),
            'software_version': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '1.0'
            }),
            'type_of_asset': forms.HiddenInput(attrs={
                'value': 'software'
            }),  # Hidden field with default value
        }

    def __init__(self, *args, **kwargs):
        super(SoftwareForm, self).__init__(*args, **kwargs)
        # Ensure all fields have 'form-control' class
        for field in self.fields.values():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'


#to update a software with the updated by field included
from .models import SoftwareUpdateLog
class SoftwareForm(forms.ModelForm):
    class Meta:
        model = SoftwareUpdateLog
        fields = ['ASSET_ID', 'brand', 'model', 'software_version', 'date_of_purchase', 'stock_register_number', 'account_head', 'location', 'updated_by']  # Include the updated_by field

    # Optionally, you can add custom styling or validation for 'updated_by' here.
    # updated_by = forms.CharField(
    #     max_length=100, 
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the person who updated this asset'})
    # )
    
  
    





#to delete a software ( invalid and scrapped )
class DeleteSoftwareForm(forms.Form):
    date_of_movement = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',  # HTML5 date input
                'placeholder': 'Select a date...'
            }
        )
    )
    reason = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter reason for movement...'
            }
        ),
        required=True
    )


#to move the software asset within the college and outside the college
from django import forms
from .models import SoftwareMovement

class SoftwareMovementForm(forms.ModelForm):
    class Meta:
        model = SoftwareMovement
        fields = ['movement_type', 'new_location', 'reason', 'date_of_movement']
        widgets = {
            'movement_type': forms.RadioSelect(attrs={'class': 'form-check-input'}),  # Radio button for movement type
            'new_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter new location'}),  # Text input for new location
            'reason': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter reason for movement', 'rows': 3}),  # Textarea for reason
            'date_of_movement': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Date picker for movement date
        }
        labels = {
            'movement_type': 'Movement Type',
            'new_location': 'New Location',
            'reason': 'Reason for Movement',
            'date_of_movement': 'Date of Movement'
        }




#to delete a computer hardware
class DeleteHardwareForm(forms.Form):
    date_of_movement = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'date',  # This will render an HTML5 date picker
            'placeholder': 'Enter date of movement'
        }),
        required=True
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter reason for movement...'
        }),
        required=True
    )





#to input computer hardware into the database
from .models import ComputerHardware
class ComputerHardwareForm(forms.ModelForm):
    class Meta:
        model = ComputerHardware
        fields = [
            'ASSET_ID', 'hardware_type', 'brand', 'model', 'processor',
            'processor_generation', 'ram', 'rom', 'motherboard', 'power_supply',
            'graphics_card', 'date_of_purchase', 'stock_register_number',
            'account_head', 'location'
        ]
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Asset ID'}),
            'hardware_type': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Computer'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model'}),
            'processor': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Processor'}),
            'processor_generation': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Processor Generation'}),
            'ram': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select RAM'}),
            'rom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ROM'}),
            'motherboard': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Motherboard'}),
            'power_supply': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Power Supply'}),
            'graphics_card': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Graphics Card'}),
            'date_of_purchase': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stock Register Number'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Head'}),
            'location': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select Location'}),
        }

#modified form to update the computer hardware in the system
from .models import ComputerHardwareUpdateLog

class ComputerHardwareUpdateLogForm(forms.ModelForm):
    class Meta:
        model = ComputerHardwareUpdateLog
        fields = [
            'computer_hardware',
            'ASSET_ID',
            'brand',
            'model',
            'processor',
            'processor_generation',
            'ram',
            'rom',
            'motherboard',
            'power_supply',
            'graphics_card',
            'date_of_purchase',
            'stock_register_number',
            'account_head',
            'location',
            'date_of_update',
            'updated_by',
            'logged_by'
        ]
        widgets = {
            'date_of_update': forms.DateInput(attrs={'type': 'date'}),
            'updated_by': forms.TextInput(attrs={'placeholder': 'Enter updater name'}),
        }


#Movement history form form for the computer hardware
from .models import ComputerHardwareMovement

class ComputerHardwareMovementForm(forms.ModelForm):
    class Meta:
        model = ComputerHardwareMovement
        fields = ['movement_type', 'new_location', 'reason', 'date_of_movement']
        widgets = {
            'movement_type': forms.RadioSelect,  # Use radio buttons for movement type
            'date_of_movement': forms.DateInput(attrs={'type': 'date'}),
            'new_location': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'movement_type': 'Movement Type',
            'new_location': 'New Location',
            'reason': 'Reason for Movement',
            'date_of_movement': 'Date of Movement'
        }






#to input projector data into database
from .models import Projector

class ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = [
            'ASSET_ID', 'brand', 'model', 'resolution', 'lumens',
            'contrast_ratio', 'connectivity', 'lamp_life_hours',
            'date_of_purchase', 'stock_register_number', 'account_head',
            'location', 'type_of_asset'
        ]
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Asset ID'}),
            'type_of_asset': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'Type of Asset'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Model'}),
            'resolution': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Resolution'}),
            'lumens': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lumens'}),
            'contrast_ratio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contrast Ratio'}),
            'connectivity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Connectivity'}),
            'lamp_life_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Lamp Life Hours'}),
            'date_of_purchase': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select Date of Purchase'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stock Register Number'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Head'}),
            'location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Location'}),


        }




from .models import ProjectorUpdateLog
class ProjectorUpdateLogForm(forms.ModelForm):
    class Meta:
        model = ProjectorUpdateLog
        fields = [
            'updated_date',
            'updated_by',  # Assuming you have added this field to the model
            'brand',
            'model',
            'resolution',
            'lumens',
            'contrast_ratio',
            'connectivity',
            'lamp_life_hours',
            'date_of_purchase',
            'stock_register_number',
            'account_head',
            'location',
        ]
        widgets = {
            'updated_date': forms.DateInput(attrs={'type': 'date'}),
        }



#to move the projector asset into invalid or scrapped
class DeleteProjectorForm(forms.Form):
    date_of_movement = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter reason for movement...'
        }),
        required=True
    )


#Movement history form for projector assets
from .models import ProjectorMovement
class ProjectorMovementForm(forms.ModelForm):
    class Meta:
        model = ProjectorMovement
        fields = ['movement_type', 'new_location', 'reason', 'date_of_movement']
        widgets = {
            'movement_type': forms.RadioSelect(attrs={'class': 'form-check-input'}),  # Radio buttons with Bootstrap
            'date_of_movement': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'new_location': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'movement_type': 'Movement Type',
            'new_location': 'New Location',
            'reason': 'Reason for Movement',
            'date_of_movement': 'Date of Movement'
        }


#to input the books into the database
from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['ASSET_ID', 'title', 'publisher', 'author', 'publishing_house', 'edition', 'date_of_purchase', 'stock_register_number', 'account_head', 'location']
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Asset ID'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Title'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Publisher'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Author'}),
            'publishing_house': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Publishing House'}),
            'edition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Edition'}),
            'date_of_purchase': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select Date of Purchase'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stock Register Number'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Account Head'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }


#form for the modified update log for book assets
from .models import BookUpdateLog
class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = BookUpdateLog
        fields = [
            'title', 
            'publisher', 
            'author', 
            'publishing_house', 
            'edition', 
            'date_of_purchase', 
            'stock_register_number', 
            'account_head', 
            'location', 
            'date_of_update',  # Manually entered date of update
            'updated_by',      # Manually entered name of person who updated
        ]
        widgets = {
            'date_of_update': forms.DateInput(attrs={'type': 'date'}),
            'updated_by': forms.TextInput(attrs={'placeholder': 'Updated by'}),
        }

#Form to move books to the invalid log
class InvalidBookForm(forms.Form):
    date_of_movement = forms.DateField(
        widget=forms.SelectDateWidget(attrs={
            'class': 'form-control'
        }), 
        label='Date of Movement'
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 3, 
            'placeholder': 'Enter reason for marking as invalid'
        }), 
        label='Reason for Movement'
    )

#form to move books to the scrapped log
class ScrappedBookForm(forms.Form):
    date_of_movement = forms.DateField(
        widget=forms.SelectDateWidget(attrs={
            'class': 'form-control'
        }), 
        label='Date of Movement'
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 3, 
            'placeholder': 'Enter reason for scrapping this asset'
        }), 
        label='Reason for Scrapping'
    )


#movement history form for books
from .models import MovedBooks, Books

class MovedBooksForm(forms.ModelForm):
    class Meta:
        model = MovedBooks
        fields = ['movement_type', 'date_of_movement', 'new_location', 'reason_for_movement']
        widgets = {
            'date_of_movement': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'new_location': forms.TextInput(attrs={'class': 'form-control'}),
            'reason_for_movement': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(MovedBooksForm, self).__init__(*args, **kwargs)
        self.fields['movement_type'].widget = forms.RadioSelect(choices=self.fields['movement_type'].choices)
        self.fields['movement_type'].widget.attrs.update({'class': 'form-check-input'})



#to imput computer peripherals into the database
from .models import ComputerPeripherals

class ComputerPeripheralsForm(forms.ModelForm):
    class Meta:
        model = ComputerPeripherals
        fields = [
            'ASSET_ID', 
            'type_of_asset', 
            'peripheral_type', 
            'brand', 
            'model', 
            'date_of_purchase', 
            'stock_register_number', 
            'account_head', 
            'location'
        ]
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Asset ID'
            }),
            'type_of_asset': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'value': 'Computer Peripheral'  # Assuming type_of_asset is always 'Computer Peripheral'
            }),
            'peripheral_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Peripheral Type'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Brand'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Model'
            }),
            'date_of_purchase': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Select Date of Purchase'
            }),
            'stock_register_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Stock Register Number'
            }),
            'account_head': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Account Head'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Location'
            }),
        }

#Modified form to update the computer peripheral with updated by and logged by
from .models import ComputerPeripheralsUpdateLog

class ComputerPeripheralsUpdateLogForm(forms.ModelForm):
    date_of_update = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    updated_by = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Updated by'}))

    class Meta:
        model = ComputerPeripheralsUpdateLog
        fields = [
            'peripheral',  # You can customize the widget if needed
            'peripheral_type',
            'brand',
            'model',
            'date_of_purchase',
            'stock_register_number',
            'account_head',
            'location',
            'date_of_update',  # Manual update date entry
            'updated_by',  # Text input for 'updated_by'
            # 'logged_by' should not be included here since it will be set automatically
        ] 

#form to get the invalid entry details for computer peripherals 
from .models import InvalidComputerPeripherals

class InvalidComputerPeripheralsForm(forms.Form):
    date_of_movement = forms.DateField(
        widget=forms.SelectDateWidget(attrs={
            'class': 'form-control'
        }), 
        label='Date of Movement'
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 3, 
            'placeholder': 'Enter reason for marking as invalid'
        }), 
        label='Reason for Movement'
    )



#form to get the scrapped asset details
class ScrappedComputerPeripheralsForm(forms.Form):
    date_of_movement = forms.DateField(
        widget=forms.SelectDateWidget(attrs={
            'class': 'form-control'
        }), 
        label='Date of Movement'
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 3, 
            'placeholder': 'Enter reason for scrapping this asset'
        }), 
        label='Reason for Movement'
    )



from .models import MovedComputerPeripherals
class MovedComputerPeripheralsForm(forms.ModelForm):
    class Meta:
        model = MovedComputerPeripherals
        fields = [
            'ASSET_ID', 'type_of_asset', 'peripheral_type', 'brand', 'model', 
            'date_of_purchase', 'stock_register_number', 'account_head', 
            'original_location', 'movement_type', 'new_location', 
            'reason_for_movement', 'date_of_movement'
        ]
        widgets = {
            'reason_for_movement': forms.Textarea(attrs={'class': 'form-control'}),
            'new_location': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_movement': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MovedComputerPeripheralsForm, self).__init__(*args, **kwargs)
        # Set up the RadioSelect widget with Bootstrap classes
        self.fields['movement_type'].widget = forms.RadioSelect()
        
        # Note: Update to use the radio choices properly
        self.fields['movement_type'].widget.choices = self.fields['movement_type'].choices

        # Add Bootstrap classes for the radio buttons
        for key in self.fields['movement_type'].widget.choices:
            self.fields['movement_type'].widget.attrs.update({'class': 'form-check-input'})












#form to enter the furniture asset into the database
from .models import Furniture

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['ASSET_ID', 'type_of_furniture', 'subtype', 'date_of_purchase', 'account_head', 'location']
        
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Asset ID',  # Placeholder for the input field
            }),
            'type_of_furniture': forms.Select(attrs={'class': 'form-control'}),
            'subtype': forms.Select(attrs={'class': 'form-control'}),
            'date_of_purchase': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',  # Use a date input type for better date selection
            }),
            'account_head': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Account Head',  # Placeholder for the input field
            }),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }







