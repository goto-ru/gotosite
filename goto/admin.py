from django.contrib import admin
from django.contrib.auth.models import Permission, User
from goto.models import *
from django.contrib.admin import StackedInline, TabularInline, ModelAdmin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.core.mail import send_mail

from django.core.urlresolvers import reverse
from filer.admin.imageadmin import *
from import_export.admin import ImportExportMixin, ImportMixin, ExportMixin
from import_export import resources
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from io import StringIO
import datetime

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


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application
        fields = ('participant__first_name', 'participant__last_name', 'participant__city', 'participant__birthday')


def export_css(modeladmin, req, queryset):
    s = StringIO()
    s.write(ApplicationResource().export(queryset=queryset).csv)
    s.seek(0)
    response = HttpResponse(FileWrapper(s), content_type='application/csv')
    response['Content-Disposition'] = datetime.datetime.now().strftime('attachment; filename=Applications-%d.%m.%y.csv')
    return response


@admin.register(Application)
class ApplicationAdmin(ExportMixin, ModelAdmin):
    def export_xlsx(self, req, queryset):
        s = StringIO()
        s.write(ApplicationResource().export(queryset=queryset).xlsx)
        s.seek(0)
        response = HttpResponse(FileWrapper(s), content_type='application/xlsx')
        response['Content-Disposition'] = datetime.datetime.now().strftime(
            'attachment; filename=Applications-%d.%m.%y.xlsx')
        return response

    def send_custom_email(self, req, queryset):
        return HttpResponseRedirect(
            reverse('askletter',
                    args=[','.join([_['participant__email'] for _ in queryset.values('participant__email')])])
        )

    def current_age(self, obj):
        return obj.participant.current_age()

    def grade(self, obj):
        return obj.participant.grade()

    def city(self, obj):
        return obj.participant.city

    def stage(self, obj):
        return str(obj.participant.education_type)

    def date_sended(self, obj):
        return obj.date_created.strftime("%b %d")

    def status_admin(self, obj):
        statuses = {
            0: ('Await', '#000'),
            1: ('Accepted', '#0044FF'),
            2: ('Rejected', '#990000'),
            3: ('Confirmed', '#00FF00'),
            4: ('Unconfirmed', '#990000')
        }

        return '<span style="color: {1};">{0}</span>'.format(*statuses[obj.status])

    def ever_been_before(self, obj):
        return obj.participant.ever_been_before()

    ever_been_before.boolean = True

    status_admin.allow_tags = True
    model = Application

    list_display = (
        'participant', 'city', 'current_age', 'stage', 'grade', 'date_sended', 'ever_been_before',
        'status_admin')
    list_filter = ('status', 'arrangement', 'participant__gender')
    search_fields = ('participant__last_name', 'participant__first_name')
    actions = [accept, reject, export_css, export_xlsx, send_custom_email]


for model in models:
    admin.site.register(model)


# Register your models here.
