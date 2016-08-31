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

from djangoseo.admin import register_seo_admin, auto_register_inlines
from django.contrib.sites.admin import SiteAdmin, Site
from django.contrib import admin
from goto.seo import MyMetadata

import datetime

models = [Participant, Expert, Page, Answer, Question, Application, Project, Assignment, Solution, Settings, Partner,
          MassMediaArticle, FAQuestion, ParticipantComment, Step]

admin.site.register(Permission)

from .application_admin import *

#auto_register_inlines(admin.site, MyMetadata)



class ExpertInline(TabularInline):
    model = Experting
    extra = 0


class ArrangementInline(TabularInline):
    model = Arrangement
    # inlines = [ExpertInline]
    extra = 0


class DepartmentInline(TabularInline):
    model = Department
    extra = 0


# class StepInline(TabularInline):
#     model = Step
#     extra = 0

class DayInline(TabularInline):
    model = Day
    extra = 0


@admin.register(Event)
class EventAdmin(ModelAdmin):
    model = Event
    filter_horizontal = ('partners', 'steps')
    inlines = [DepartmentInline, ArrangementInline]


@admin.register(Arrangement)
class ArrangementAdmin(ModelAdmin):
    model = Arrangement
    inlines = [ExpertInline]


class BlockEntityAdmin(TabularInline):
    model = BlockEntity
    extra = 0


@admin.register(Block)
class BlockAdmin(ModelAdmin):
    model = Block
    inlines = [BlockEntityAdmin, DayInline]


models = [Participant, Expert, Page, Answer, Question,
          Project, Assignment, Solution, Settings, Partner,
          MassMediaArticle, FAQuestion, Step]
for model in models:
    admin.site.register(model)

#admin.site.register(Site, SiteAdmin)

register_seo_admin(admin.site, MyMetadata)
