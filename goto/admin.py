from django.contrib import admin
from django.contrib.auth.models import Permission, User
from goto.models import *
from django.contrib.admin import StackedInline, TabularInline, ModelAdmin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.core.mail import send_mail

from filer.admin.imageadmin import *

models = [Participant, Expert, Page, Answer, Question,
          Project, Assignment, Solution, Settings, Partner,
          MassMediaArticle, FAQuestion]

admin.site.register(Permission)


class AnswerInline(NestedStackedInline):
    # fields = ['text']
    model = Answer
    max_num = 0
    extra = 0


class QuestionInline(NestedStackedInline):
    fields = ['text']
    model = Question
    inlines = [AnswerInline]
    max_num = 0
    extra = 0


class ApplicationInline(NestedStackedInline):
    model = Application
    inlines = [QuestionInline]
    # fk_name = 'answers'
    max_num = 0
    extra = 0


class ExpertInline(NestedStackedInline):
    model = Experting
    extra = 0


class ArrangementInline(NestedStackedInline):
    model = Arrangement
    # inlines = [ExpertInline, ApplicationInline]
    # fk_name = 'answers'
    extra = 0


class DepartmentInline(NestedStackedInline):
    model = Department
    # fk_name = 'answers'
    extra = 0


@admin.register(Event)
class EventAdmin(NestedModelAdmin):
    model = Event
    inlines = [DepartmentInline, ArrangementInline]


@admin.register(Arrangement)
class ArrangementAdmin(NestedModelAdmin):
    model = Arrangement
    inlines = [ExpertInline]


def accept(modeladmin, req, queryset):
    queryset.update(status=1)
    event_name = queryset.get().arrangement.event.name
    send_mail('Подтверждение заявки на мероприятие "%s"' % event_name,
              'Ваша заявка на мероприятие одобрена. Перейдите по ссылке <такой-то> чтобы подтвердить своё участие',
              'events@goto.omrigan.info', [_['participant__email'] for _ in queryset.values('participant__email')],
              fail_silently=False)


def reject(modeladmin, req, queryset):
    queryset.update(status=2)
    event_name = queryset.get().arrangement.event.name
    send_mail('Отклонение заявки на мероприятие "%s"' % event_name,
              'Ваша заявка на мероприятие одобрена. Перейдите по ссылке <такой-то> чтобы подтвердить своё участие',
              'events@goto.omrigan.info', [_['participant__email'] for _ in queryset.values('participant__email')],
              fail_silently=False)


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    def current_age(self, obj):
        return obj.participant.current_age()

    def current_class(self, obj):
        return obj.participant.current_class()

    model = Application

    list_display = ('participant', 'status', 'current_age', 'current_class',)
    list_filter = ('status', 'arrangement', 'participant__gender')
    search_fields = ('participant__last_name', 'participant__first_name')
    actions = [accept, reject]


for model in models:
    admin.site.register(model)


# Register your models here.
