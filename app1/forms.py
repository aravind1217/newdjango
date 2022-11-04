from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *
ROLE_CHOICES =(
    ("-------",'------'),
    ("HR", "HR"),
    ("Developer", "Developer"),
    ("Manager", "Manager"),
    ("Reviewer", "Reviewer"),
   
)
  



class UserRegisterForm(UserCreationForm):
    roles=forms.ChoiceField(choices = ROLE_CHOICES)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ,'roles']


class Articleform(forms.ModelForm):
    class Meta:
        model = Articles
        fields ="__all__"
      