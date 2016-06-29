from django import forms
from .models import *


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = GotoUser
        fields = ['surname',
                  'organization',
                  'sex',
                  'vk',
                  'github',
                  'about',
                  'profile_picture', ]
