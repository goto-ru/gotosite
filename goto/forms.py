from django import forms
from .models import *


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = GotoUser
        fields = ['surname', 'vk', 'github', 'about', 'profile_picture']
