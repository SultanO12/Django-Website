from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile

User = get_user_model()

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = PhoneNumberField(region="UZ", required=True)

    class Meta:
        model = User
        fields = ("email", "phone", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email'] 
        if commit:
            user.save()
        return user

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', "phone")
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', "phone")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("picture", "bio")