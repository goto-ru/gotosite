from django.db import models
from datetime import date
from django.contrib.auth.models import User
from .subscribe_views import *
from filer.fields.image import FilerImageField


class GotoUser(User):
    # last_name = models.CharField(max_length=40, blank=True)
    # first_name = models.CharField(max_length=40, blank=True)
    SEX = (('M', 'Male'),
           ('F', 'Female'),
           ('N', 'Can\'t say'),)
    sex = models.CharField(choices=SEX, default='M', max_length=2)
    surname = models.CharField(max_length=40, blank=True)
    vk = models.URLField(max_length=240, default='', blank=True)
    github = models.URLField(max_length=240, default='', blank=True)
    about = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='no-photo.jpg',
                                        blank=False, null=False)
    organization = models.CharField(max_length=240, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Participant(GotoUser):
    # Personal data
    graduation_year = models.IntegerField(blank=True, default=2016)
    city = models.CharField(max_length=40, default='Москва', blank=True)
    citizenship = models.CharField(max_length=40, default='Российская Федерация', blank=True)

    birthday = models.DateField(default=date.today)
    phone_number = models.CharField(max_length=40, blank=True)
    parent_phone_number = models.CharField(max_length=40, blank=True)
    health_issues = models.TextField(default='Никаких', blank=True)
    _subscribed_to_email = models.BooleanField(default=False)

    @property
    def subscribed_to_email(self):
        return self._subscribed_to_email

    @subscribed_to_email.setter
    def subscribed_to_email(self, val):
        if val:
            mailchimp_subscribe(self.email)
        else:
            mailchimp_unsubscribe(self.email)
        self._subscribed_to_email = val

    # Public data
    programming_languages = models.TextField(blank=True, )
    experience = models.TextField(blank=True)

    def current_age(self):
        return (date.today() - self.birthday).days // 365

    def current_class(self):

        left = self.graduation_year - date.today().year
        if date.today().month < 5:
            left += 1
        cl = 12 - left
        if cl >= 12:
            cl = 'Выпустился в %s' % self.graduation_year
        return cl

    class Meta():
        verbose_name = 'Participant'
        verbose_name_plural = 'Participants'


class Expert(GotoUser):
    short_description = models.CharField(max_length=256, blank=True)
    position = models.CharField(max_length=140, null=True, blank=True)

    class Meta():
        verbose_name = 'Expert'
        verbose_name_plural = 'Experts'
        permissions = (
            ('view_personal_data', 'Can view personal data'),
            ('leave_private_comments', 'Can leave private comments'),
            ('view_private_comment', 'Can view private comments'),
        )


class FAQuestion(models.Model):
    question = models.CharField(max_length=512)
    answer = models.CharField(max_length=1024)
    question_author = models.ForeignKey(GotoUser, blank=True, null=True)


class Page(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    FORMATS = (
        ('school', 'Школа'),
        ('hackathon', 'Хакатон'),
        ('lecture', 'Лекция'),
        ('other', 'Другое'),
    )
    name = models.CharField(max_length=256, )
    short_description = models.CharField(max_length=512, blank=True)
    full_description = models.TextField(blank=True)

    price = models.CharField(max_length=400, blank=True)
    target_auditory = models.CharField(max_length=400, blank=True)
    format = models.CharField(max_length=400, blank=True, choices=FORMATS)
    place = models.CharField(max_length=400, blank=True)
    partners = models.ManyToManyField('Partner')

    pages = models.ManyToManyField(Page, blank=True)
    applier_questions = models.ManyToManyField('Question', blank=True)

    faquestions = models.ManyToManyField(FAQuestion)

    def experts(self):
        ret = set()
        for ar in self.arrangements.all():
            ret |= set(ar.experts.all())
        return ret

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'


class Arrangement(models.Model):
    event = models.ForeignKey(Event, related_name='arrangements')
    begin_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    participants = models.ManyToManyField(Participant, through='Application')
    experts = models.ManyToManyField(Expert, through='Experting')

    def __str__(self):
        return "%s %s-%s" % (self.event, self.begin_date, self.end_date)


class Departments(models.Model):
    event = models.ForeignKey(Event, related_name='departments')
    title = models.CharField(max_length=256)
    image = FilerImageField(blank=True, null=True)
    description = models.TextField()


class Application(models.Model):
    status_to_text = {
        0: 'Ожидает рассмотрения',
        1: 'Одобрена',
        2: 'Отклонена',
        3: 'Подтверждена',
        4: 'Не подтверждена',
    }
    STATUSES = list(status_to_text.items())
    status_to_class = {
        0: 'info',
        1: 'warning',
        2: 'danger',
        3: 'success',
        4: 'danger',
    }
    arrangement = models.ForeignKey(Arrangement, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=0)
    date_created = models.DateTimeField()

    class Meta:
        ordering = ['-date_created']

    def text_status(self):
        return self.status_to_text[self.status]

    def class_status(self):
        return self.status_to_class[self.status]

    def __str__(self):
        return '%s on %s' % (self.participant, self.arrangement)


class Experting(models.Model):
    arrangement = models.ForeignKey(Arrangement, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    STATUSES = [
        (0, 'In discuss'),
        (1, 'Confirmed'),
        (2, 'Canceled'),
    ]
    status = models.IntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return '%s on %s' % (self.expert, self.arrangement)


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


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    maintainers = models.ManyToManyField(Participant, related_name='projects')
    supervisor = models.ForeignKey(Expert, blank=True, null=True)
    event = models.ForeignKey(Arrangement, blank=True, null=True)

    def __str__(self):
        return self.title


class ParticipantComment(models.Model):
    text = models.TextField(blank=True)
    participant = models.ForeignKey(Participant, related_name='comments')
    author = models.ForeignKey(GotoUser, related_name='left_participant_comments')
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return self.text


class ProjectComment(models.Model):
    text = models.TextField(blank=True)
    project = models.ForeignKey(Project)
    author = models.ForeignKey(GotoUser, related_name='left_project_comments')
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return self.text


class Assignment(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.title


class Solution(models.Model):
    assignment = models.ForeignKey(Assignment)
    participant = models.ForeignKey(Participant)
    file = models.FileField(upload_to='solutions/', blank=True)
    participant_comment = models.CharField(max_length=1000, blank=True)
    date_posted = models.DateTimeField()

    date_verified = models.DateTimeField(blank=True, null=True)
    expert = models.ForeignKey(Expert, blank=True, null=True)
    score = models.FloatField(default=0)
    expert_public_comment = models.CharField(max_length=1000, blank=True, null=True)
    expert_private_comment = models.CharField(max_length=1000, blank=True, null=True)


class Subscriber(models.Model):
    email = models.EmailField(primary_key=True)


class Partner(models.Model):
    name = models.CharField(max_length=512)
    link = models.URLField()
    image = models.ImageField(upload_to='partners', default='no-photo.jpg')

    def __str__(self):
        return self.name


class Settings(models.Model):
    index_partners = models.ManyToManyField(Partner, blank=True, related_name='index_partners')
    about_us_partners = models.ManyToManyField(Partner, blank=True, related_name='about_us_partners')
    about_us_team = models.ManyToManyField(Expert, blank=True)

    current_left_school = models.ForeignKey(Event, blank=True, null=True, related_name='settings_1')
    current_right_school = models.ForeignKey(Event, blank=True, null=True, related_name='settings_2')

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Settings, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class MassMediaArticle(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    link = models.URLField()
    image = models.ImageField(upload_to='mm-pictures')

    def __str__(self):
        return self.title
