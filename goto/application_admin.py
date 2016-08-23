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
import datetime, csv
from goto.resources import ApplicationResource





class GradeFilter(admin.SimpleListFilter):
    title = 'Grade'
    parameter_name = 'grade'

    def lookups(self, request, model_admin):
        grades = [(i, str(i)) for i in range(1, 12)]
        return grades

    def queryset(self, request, queryset):
        if self.value():
            ids = [part.id for part in queryset.all() if part.participant.grade == self.value()]
            return Participant.objects.filter(id__in=ids)
        else:
            return queryset


@admin.register(Application)
class ApplicationAdmin(SortableAdminMixin, ModelAdmin):
    def accept(self, req, queryset):
        queryset.update(status=1)
        event_name = queryset.get().arrangement.event.name
        send_mail('Подтверждение заявки на мероприятие "%s"' % event_name,
                  'Ваша заявка на мероприятие одобрена. Перейдите по ссылке <такой-то> чтобы подтвердить своё участие',
                  settings.EMAIL_FROM, [_['participant__email'] for _ in queryset.values('participant__email')],
                  fail_silently=False)

    def reject(self, req, queryset):
        queryset.update(status=2)
        event_name = queryset.get().arrangement.event.name
        send_mail('Отклонение заявки на мероприятие "%s"' % event_name,
                  'Ваша заявка на мероприятие одобрена. Перейдите по ссылке <такой-то> чтобы подтвердить своё участие',
                  settings.EMAIL_FROM, [_['participant__email'] for _ in queryset.values('participant__email')],
                  fail_silently=False)

    def send_custom_email(self, req, queryset):
        return HttpResponseRedirect(
            reverse('askletter',
                    args=[','.join([_['participant__email'] for _ in queryset.values('participant__email')])])
        )

    def export_css(self, req, queryset):
        s = StringIO()
        s.write(ApplicationResource().export(queryset=queryset).csv)
        s.seek(0)
        response = HttpResponse(FileWrapper(s), content_type='application/csv')
        response['Content-Disposition'] = datetime.datetime.now().strftime(
            'attachment; filename=Applications-%d.%m.%y.csv')
        return response



    def export(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        request.session['ids']=[inst.pk for inst in queryset.all()]
        request.session.modified = True
        return HttpResponseRedirect(reverse('export'))


    def current_age(self, obj):
        return obj.participant.current_age()

    def grade(self, obj):
        return obj.participant.grade()

    def city(self, obj):
        return obj.participant.city

    def stage(self, obj):
        return obj.participant.get_education_type_display()

    def date_sended(self, obj):
        return obj.date_created.strftime("%b %d")

    def status_admin(self, obj):
        statuses = {
            0: ('Await', 'info'),
            1: ('Accepted', 'primary'),
            2: ('Rejected', 'danger'),
            3: ('Confirmed', 'success'),
            4: ('Unconfirmed', 'danger')
        }
        return '<h3><a href={2}><span class="label label-{1}" >{0}</span></a></h3>'. \
            format(*statuses[obj.status],
                   reverse("admin:goto_application_change", args=[obj.pk]))

    status_admin.allow_tags = True

    def guy(self, obj):
        return "<a href='%s'>%s</a>" % (
            reverse("admin:goto_participant_change", args=[obj.participant.pk]), obj.participant)

    guy.allow_tags = True

    def been(self, obj):
        return obj.participant.ever_been_before()

    been.boolean = True

    model = Application
    # inlines = [AnswerInline]

    list_display = (
        'guy', 'city', 'current_age', 'stage', 'grade', 'date_sended', 'been',
        'status_admin')

    list_filter = ('status', 'arrangement', 'participant__gender', 'participant__education_type',
                   # GradeFilter
                   )
    search_fields = ('participant__last_name', 'participant__first_name')
    list_display_links = tuple()
    actions = [accept, reject, export, send_custom_email]
