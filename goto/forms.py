from django import forms
from .models import *


class UserEditForm(forms.ModelForm):
    class Meta:
        model = GotoUser
        fields = [

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

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title',
                  'description',
                  'link',
                  'maintainers',
                  'supervisor',
                  'arrangement']
