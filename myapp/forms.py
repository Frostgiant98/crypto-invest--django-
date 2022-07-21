from django import forms
from django.forms import fields, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Profile, deposits_table, withdrawal_table, notifications_table




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a Valid Email')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class profile_form(forms.ModelForm):
    
    class Meta:

        model = Profile
        fields = [
            
            'phone_number'
        ]


class user_profile_form(forms.ModelForm):
    
    class Meta:

        model = User
        fields = [
            'first_name',
            'last_name'
        ]


class admin_profile_form(forms.ModelForm):
    
    class Meta:

        model = Profile
        fields = '__all__'

class admin_user_profile_form(forms.ModelForm):
    
    class Meta:

        model = User
        fields = [
            'first_name',
            'last_name',
        ]


class deposits_form(forms.ModelForm):
    
    class Meta:

        model = deposits_table
        fields = [
            
            'amount'
        ]


class withdrawal_form(forms.ModelForm):
    
    class Meta:

        model = withdrawal_table
        fields = [
            
            'amount',
            'withdrawal_wallet'
        ]
        
class notification_form(forms.ModelForm):
    class Meta:
        model = notifications_table
        fields = '__all__'
        
