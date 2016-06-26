from django.db import models
from datetime import date
from django.contrib.auth.models import User


class GotoUser(User):
    # last_name = models.CharField(max_length=40, blank=True)
    # first_name = models.CharField(max_length=40, blank=True)
    surname = models.CharField(max_length=40, blank=True)


class Participant(GotoUser):
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

    class Meta():
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'


class Expert(GotoUser):
    description = models.CharField(max_length=500, )
    teacher_image = models.ImageField(upload_to='teacher_images/', null=True, blank=True)

    class Meta():
        verbose_name = 'Expert'
        verbose_name_plural = 'Experts'


class Staff(GotoUser):
    class Meta():
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'


class Event(models.Model):
    name = models.CharField(max_length=256, )
    description = models.CharField(max_length=2000, )
    begin_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    format = models.CharField(max_length=400, blank=True, default='')
    place = models.CharField(max_length=400, blank=True, default='')
    participants = models.ManyToManyField(Participant, through='Application')
    experts = models.ManyToManyField(Expert, through='Experting')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'


class Application(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    STATUSES = [
        (0, 'In review'),
        (1, 'Approved'),
        (2, 'Declined'),
        (3, 'Confirmed'),
    ]
    status = models.IntegerField(choices=STATUSES, default=0)


class Experting(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    STATUSES = [
        (0, 'In discuss'),
        (1, 'Confirmed'),
        (2, 'Canceled'),
    ]
    status = models.IntegerField(choices=STATUSES, default=0)

