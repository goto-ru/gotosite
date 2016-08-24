from django.contrib import admin
from django.contrib.auth.models import Permission, User
from goto.models import *
from django.contrib.admin import StackedInline, TabularInline, ModelAdmin

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from filer.admin.imageadmin import *

models = [Participant, Expert, Page, Answer, Question, Application, Project, Assignment, Solution, Settings, Partner,
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


class EventAdmin(NestedModelAdmin):
    model = Event
    inlines = [DepartmentInline, ArrangementInline]


class ArrangementAdmin(NestedModelAdmin):
    model = Arrangement
    inlines = [ExpertInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Arrangement, ArrangementAdmin)

for model in models:
    admin.site.register(model)


# Register your models here.
