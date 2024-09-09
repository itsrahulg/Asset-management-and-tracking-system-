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
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_purchase': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'type_of_asset': forms.HiddenInput(attrs={'value': 'software'}),  # Hidden field with default value
            'software_version': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SoftwareForm, self).__init__(*args, **kwargs)
        # Optional: Customize form layout or field attributes here
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'





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
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'hardware_type': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'processor': forms.Select(attrs={'class': 'form-select'}),
            'processor_generation': forms.Select(attrs={'class': 'form-select'}),
            'ram': forms.Select(attrs={'class': 'form-select'}),
            'rom': forms.TextInput(attrs={'class': 'form-control'}),
            'motherboard': forms.TextInput(attrs={'class': 'form-control'}),
            'power_supply': forms.TextInput(attrs={'class': 'form-control'}),
            'graphics_card': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_purchase': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
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
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_asset': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'resolution': forms.Select(attrs={'class': 'form-control'}),
            'lumens': forms.NumberInput(attrs={'class': 'form-control'}),
            'contrast_ratio': forms.TextInput(attrs={'class': 'form-control'}),
            'connectivity': forms.Select(attrs={'class': 'form-control'}),
            'lamp_life_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_purchase': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            
        }






#to input the books into the database
from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['ASSET_ID', 'title', 'publisher', 'author', 'publishing_house', 'edition', 'date_of_purchase', 'stock_register_number', 'account_head', 'location']
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publishing_house': forms.TextInput(attrs={'class': 'form-control'}),
            'edition': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_purchase': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }





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
            'ASSET_ID': forms.TextInput(attrs={'placeholder': 'Enter Asset ID'}),
            'peripheral_type': forms.Select(attrs={'placeholder': 'Select Peripheral Type'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Enter Brand'}),
            'model': forms.TextInput(attrs={'placeholder': 'Enter Model'}),
            'stock_register_number': forms.TextInput(attrs={'placeholder': 'Enter Stock Register Number'}),
            'account_head': forms.TextInput(attrs={'placeholder': 'Enter Account Head'}),
            'location': forms.Select(),
        }




























