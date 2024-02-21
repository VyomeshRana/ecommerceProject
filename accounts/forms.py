from django import forms
from .models import *


class customerForm(forms.ModelForm):
    class Meta:
        model = customerModel
        fields = ['username', 'f_name', 'L_name', 'email', 'phoneNo', 'address1', 'address2', 'street', 'city', 'state', 'pincode', 'password', 'confPass']

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'f_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'L_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'phoneNo' : forms.NumberInput(attrs={'class': 'form-control'}),
            'address1' : forms.TextInput(attrs={'class': 'form-control'}),
            'address2' : forms.TextInput(attrs={'class': 'form-control'}),
            'street' : forms.TextInput(attrs={'class': 'form-control'}),
            'city' : forms.TextInput(attrs={'class': 'form-control'}),
            'state' : forms.TextInput(attrs={'class': 'form-control'}),
            'pincode' : forms.NumberInput(attrs={'class': 'form-control'}),
            'password' : forms.TextInput(attrs={'class': 'form-control'}),
            'confPass' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class vendorForm(forms.ModelForm):
    class Meta:
        model = vendorModel
        fields = [
            'name', 'shopName', 'shopAddress', 'shopLicence', 'longitude', 'latitude', 'vendorMail', 'vendorPhone', 'password', 'confPass' 
        ]

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),  
            'shopName' : forms.TextInput(attrs={'class':'form-control'}), 
            'shopAddress' : forms.TextInput(attrs={'class':'form-control'}),
            'shopLicence' : forms.TextInput(attrs={'class':'form-control'}),
            'longitude' : forms.TextInput(attrs={'class':'form-control'}),
            'latitude'  : forms.TextInput(attrs={'class':'form-control'}),
            'vendorMail' : forms.EmailInput(attrs={'class':'form-control'}),
            'vendorPhone' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'class':'form-control'}),
            'confPass' : forms.TextInput(attrs={'class':'form-control'}), 
        }