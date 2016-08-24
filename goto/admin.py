from django.contrib import admin
from django.contrib.auth.models import Permission, User
from goto.models import *
from django.contrib.admin import StackedInline, TabularInline, ModelAdmin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.core.mail import send_mail
from adminsortable2.admin import SortableAdminMixin

from django.core.urlresolvers import reverse
from filer.admin.imageadmin import *
from import_export.admin import ImportExportMixin, ImportMixin, ExportMixin
from import_export import resources
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from io import StringIO
from django.contrib.admin import AdminSite

import datetime


models = [Participant, Expert, Page, Answer, Question, Application, Project, Assignment, Solution, Settings, Partner,
          MassMediaArticle, FAQuestion, ParticipantComment]

admin.site.register(Permission)

from .application_admin import *

class AnswerInline(StackedInline):
    # fields = ['text']
    model = Answer
    max_num = 0
    extra = 0


class ExpertInline(NestedStackedInline):
    model = Experting
    extra = 0


class ArrangementInline(NestedStackedInline):
    model = Arrangement
    inlines = [ExpertInline]
    extra = 0


class DepartmentInline(NestedStackedInline):
    model = Department
    extra = 0


@admin.register(Event)
class EventAdmin(NestedModelAdmin):
    model = Event
    filter_horizontal = ('partners',)
    inlines = [DepartmentInline, ArrangementInline]


@admin.register(Arrangement)
class ArrangementAdmin(NestedModelAdmin):
    model = Arrangement
    inlines = [ExpertInline]



models = [Participant, Expert, Page, Answer, Question,
          Project, Assignment, Solution, Settings, Partner,
          MassMediaArticle, FAQuestion]
for model in models:
    admin.site.register(model)





