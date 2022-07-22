from dataclasses import fields
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,DateField, SelectDateWidget
from .models import Profile
from django import forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class ProfileForm(ModelForm):
    year_range = tuple([i for i in range(1950, 2010)])
    dob = DateField(widget=SelectDateWidget(years=year_range))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ('dob','mobile')
        