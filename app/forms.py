from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User
from .models import User

from django import forms

from .models import Zayavka

class CreateZayavkaForm(forms.ModelForm):
    class Meta:
        model = Zayavka
        fields = ['type', 'date', 'payment', 'status']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password1', 'password2']