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

    




#to create other admins in the app
class SuperUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password_confirm'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_superuser = True
        user.is_staff = True
        if commit:
            user.save()
        return user
    






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
