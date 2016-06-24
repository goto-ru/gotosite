from django.db import models
from datetime import date


class Participant(models.Model):

    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    birthday = models.DateField(default=date.today)

    place_of_birth = models.CharField(max_length=140, null=True, blank=True)

    city = models.CharField(max_length=40, default='Москва', blank=True)
    citizenship = models.CharField(max_length=40, default='Российская Федерация', blank=True)

    phone_number = models.CharField(max_length=40, null=True, blank=True)
    parents_phone_number = models.CharField(max_length=40, null=True, blank=True)

    occupation = models.CharField(max_length=250, blank=True, default='', null=True)
    programming_languages = models.CharField(max_length=250, blank=True, default='', null=True)

    document = models.CharField(max_length=40, blank=True, default='', null=True)
    document_number = models.IntegerField(blank=True, null=True)
    police_number = models.IntegerField(blank=True, null=True)

    vk = models.URLField(max_length=240, default='', blank=True)
    github = models.URLField(max_length=240, default='', blank=True)

    health_issues = models.CharField(max_length=40, default='Никаких', blank=True)

    experience = models.CharField(max_length=700, default='', blank=True)
    about = models.CharField(max_length=500, default='', blank=True)

class Expert(models.Model):
    description = models.CharField(max_length=500, )
    teacher_image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)


class Staff(models.Model):






# Create your models here.
