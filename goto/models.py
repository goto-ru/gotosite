from django.db import models
from datetime import date
from django.contrib.auth.models import User


class GotoUser(User):
    # last_name = models.CharField(max_length=40, blank=True)
    # first_name = models.CharField(max_length=40, blank=True)
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Can\'t say'),
    )
    sex = models.CharField(choices=SEX, default='M', max_length=2)
    surname = models.CharField(max_length=40, blank=True)
    vk = models.URLField(max_length=240, default='', blank=True)
    github = models.URLField(max_length=240, default='', blank=True)
    about = models.CharField(max_length=500, default='', blank=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/',
                                        default='media/profile_pictures/no-photo.jpg', blank=False,
                                        null=False)
    organization = models.CharField(max_length=240, blank=True)


    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Participant(GotoUser):
    # Personal data
    birthday = models.DateField(default=date.today)
    city = models.CharField(max_length=40, default='Москва', blank=True)
    citizenship = models.CharField(max_length=40, default='Российская Федерация', blank=True)
    phone_number = models.CharField(max_length=40, null=True, blank=True)
    health_issues = models.CharField(max_length=40, default='Никаких', blank=True)

    # Public data
    programming_languages = models.CharField(max_length=250, blank=True, default='', null=True)
    experience = models.CharField(max_length=700, default='', blank=True)

    class Meta():
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'


class Expert(GotoUser):
    company = models.CharField(max_length=140, null=True, blank=True)

    class Meta():
        verbose_name = 'Expert'
        verbose_name_plural = 'Experts'


class Staff(GotoUser):
    class Meta():
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'


class Page(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=256, )
    description = models.CharField(max_length=2000, )
    begin_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    format = models.CharField(max_length=400, blank=True, default='')
    place = models.CharField(max_length=400, blank=True, default='')
    participants = models.ManyToManyField(Participant, through='Application')
    experts = models.ManyToManyField(Expert, through='Experting')
    pages = models.ManyToManyField(Page, blank=True)
    questions = models.ManyToManyField('Question', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'


class Application(models.Model):
    STATUSES = [
        (0, 'In review'),
        (1, 'Approved'),
        (2, 'Declined'),
        (3, 'Confirmed'),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return '%s on %s' % (self.participant, self.event)



class Experting(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    STATUSES = [
        (0, 'In discuss'),
        (1, 'Confirmed'),
        (2, 'Canceled'),
    ]
    status = models.IntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return '%s on %s' % (self.expert, self.event)


class Question(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text


class Answer(models.Model):
    application = models.ForeignKey(Application, related_name='answers')
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=512)

    def __str__(self):
        return self.text
