from typing import Any

from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from .models import Asset


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
    






#to input an asset into the database
class AddAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'ASSET_ID', 'type_of_asset', 'hardware_type', 'brand', 'model', 
            'processor', 'ram', 'rom', 'motherboard', 'power_supply', 
            'graphics_card', 'specifications', 'date_of_purchase', 
            'make_and_model', 'stock_register_number', 'account_head', 'location'
        ]
        widgets = {
            'ASSET_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_asset': forms.Select(attrs={'class': 'form-control'}),
            'hardware_type': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'processor': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'rom': forms.TextInput(attrs={'class': 'form-control'}),
            'motherboard': forms.TextInput(attrs={'class': 'form-control'}),
            'power_supply': forms.TextInput(attrs={'class': 'form-control'}),
            'graphics_card': forms.TextInput(attrs={'class': 'form-control'}),
            'specifications': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_of_purchase': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'make_and_model': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_register_number': forms.TextInput(attrs={'class': 'form-control'}),
            'account_head': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hardware_type'].required = False
        self.fields['processor'].required = False
        self.fields['ram'].required = False
        self.fields['rom'].required = False
        self.fields['motherboard'].required = False
        self.fields['power_supply'].required = False
        self.fields['graphics_card'].required = False
        self.fields['brand'].required = False
        self.fields['model'].required = False