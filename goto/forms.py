from django import forms
from .models import *


class UserEditForm(forms.ModelForm):
    class Meta:
        model = GotoUser
        fields = [
            'last_name_tmp',
            'first_name_tmp',

            'surname',
            'organization',
            'sex',
            'vk',
            'github',
            'about',
            'profile_picture', ]


class ParticipantEditForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['graduation_year',
                  'city',
                  'citizenship',
                  'birthday',
                  'phone_number',
                  'parent_phone_number',
                  'health_issues',
                  'programming_languages',
                  'experience']
