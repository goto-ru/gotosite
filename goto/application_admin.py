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


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application
        fields = ('participant__first_name', 'participant__last_name', 'participant__city', 'participant__birthday')


# admin.py
class CountryFilter(admin.SimpleListFilter):
    title = 'Class'  # or use _('country') for translated title
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        countries = set([c.country for c in model_admin.model.objects.all()])
        return [(c.id, c.name) for c in countries]
        # You can also use hardcoded model name like "Country" instead of
        # "model_admin.model" if this is not direct foreign key filter

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(country__id__exact=self.value())
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

    def export_xlsx(self, req, queryset):
        s = StringIO()
        s.write(ApplicationResource().export(queryset=queryset).xlsx)
        s.seek(0)
        response = HttpResponse(FileWrapper(s), content_type='application/xlsx')
        response['Content-Disposition'] = datetime.datetime.now().strftime(
            'attachment; filename=Applications-%d.%m.%y.xlsx')
        return response

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

    list_filter = ('status', 'arrangement', 'participant__gender', 'participant__education_type')
    search_fields = ('participant__last_name', 'participant__first_name')
    list_display_links = tuple()
    actions = [accept, reject, export_css, export_xlsx, send_custom_email]
