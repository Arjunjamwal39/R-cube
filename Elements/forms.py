from dataclasses import fields
from logging import PlaceHolder
from pyexpat import model
from unittest.util import _PLACEHOLDER_LEN
from django.contrib.auth.models import User   #importing user model
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import Customer, practice
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from sympy import false 
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class EnterdaUser(UserCreationForm):  #inherting properties of Usercreationforminto Signup class also provies (password to similar with username) validation
  first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Full Name','style':'margin-bottom:10px', 'size':'39',}))
  password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control','PlaceHolder':'Password','style':'margin-bottom:10px', 'size':'39'}))
  password2 = forms.CharField(label='Enter password again', widget=forms.PasswordInput(attrs={'class':'form-control','PlaceHolder':'Re-enter','style':'margin-bottom:10px', 'size':'39'}))
  email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','PlaceHolder':'Email','style':'margin-bottom:10px', 'size':'39',}))
  
  class Meta:
    model = User
    fields = ['first_name','username','email','password1','password2']
    label = {'email':'Email'}
    widgets = {'username':forms.TextInput(attrs={'class':'form-control','PlaceHolder':'Username','style':'margin-bottom:20px;color: blueviolet','size':'39'})}

class LogindaUser(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
  password = forms.CharField(label=_("Password"), strip = False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class Changedapassword(PasswordChangeForm):
  old_password  =  forms.CharField(label=_("Old password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
  new_password1 = forms.CharField(label=_("New password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
  new_password2 = forms.CharField(label=_("Confirms New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class Forgotpass(PasswordResetForm):
  email = forms.EmailField(label=_('Email'), max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control',}))

class ForgotpassConfirm(SetPasswordForm):
          new_password1 = forms.CharField(label=_("New password"),
          widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
          strip=False,
          help_text=password_validation.password_validators_help_text_html())

          new_password2 = forms.CharField(
          label=_("New password confirmation"),
          strip=False,
          widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))

class Customerprofilee(forms.ModelForm):
  #Contact_number = PhoneNumberField(widget=PhoneNumberPrefixWidget())
  #name = forms.CharField(widget=)
  class Meta:
    model = Customer
    fields = ['name','Contact_number','locality','city','zipcode','state','address_type']
    widgets = {'name':forms.TextInput(attrs= {'class':'form-control'}),
              'Contact_number':PhoneNumberPrefixWidget(attrs = {'class':'form-control', 'style':'margin-top:5px'}),
              'locality':forms.TextInput(attrs= {'class':'form-control'}),
              'city':forms.TextInput(attrs= {'class':'form-control'}),
              'zipcode':forms.NumberInput(attrs= {'class':'form-control'}),
              'state':forms.Select(attrs= {'class':'form-control'}),
              'address_type':forms.Select(attrs= {'class':'form-control'})
              }

