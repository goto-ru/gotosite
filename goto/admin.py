from django.contrib import admin
from django.contrib.auth.models import Permission, User
from goto.models import *

from nested_inline.admin import NestedStackedInline, NestedModelAdmin

models = [Participant, Expert, Page, Answer, Question, Application, Project, Assignment, Solution, Settings, Partner,
          MassMediaArticle]

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
    inlines = [AnswerInline]
    # fk_name = 'answers'
    max_num = 0
    extra = 0


class EventAdmin(NestedModelAdmin):
    model = Event
    inlines = [ApplicationInline]


admin.site.register(Event, EventAdmin)

for model in models:
    admin.site.register(model)
1

# Register your models here.
