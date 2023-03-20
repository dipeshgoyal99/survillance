from django import forms
from .models import *
class UserCreateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name","last_name","email","phone","address","password")
