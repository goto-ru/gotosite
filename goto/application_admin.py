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


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application
        fields = tuple(('%s' % (f.name,) for f in Application._meta.get_fields())) + \
                 tuple(('participant__%s' % (f.name,) for f in Participant._meta.get_fields()))
        # fields = ('participant__first_name', 'participant__last_name', 'participant__city', 'participant__birthday')

    def get_export_order(self):
        # order = tuple(self._meta.export_order or ())
        ret = self.current_fields
        return ret
        # return order + tuple(k for k in self.fields.keys() if k not in order)


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

    def export_generic(description="Export selected objects as CSV file", children_fields=None, file_format='csv',
                       fields=None, exclude=None, header=True):
        """
        This function returns an export csv action
        'fields' and 'exclude' work like in django ModelForm
        'header' is whether or not to output the column names as the first row
        """

        def export(modeladmin, request, queryset):
            """
            Generic csv export admin action.
            based on http://djangosnippets.org/snippets/1697/
            """
            opts = modeladmin.model._meta
            field_names = set([field.name for field in opts.fields])
            if children_fields:
                for c in children_fields:
                    child = getattr(modeladmin.model, c).field.model
                    child_field_names = set(["%s__%s" % (c, field.name) for field in child._meta.fields])
                    field_names |= child_field_names
            if fields:
                fieldset = set(fields)
                field_names = field_names & fieldset
            elif exclude:
                excludeset = set(exclude)
                field_names = field_names - excludeset

            response = HttpResponse(mimetype='text/csv')
            response['Content-Disposition'] = 'attachment; filename=%s.csv' % opts.replace('.', '_')

            writer = csv.writer(response)
            if header:
                writer.writerow(list(field_names))
            for obj in queryset:
                writer.writerow([getattr(obj, field) for field in field_names])
            return response

        export.short_description = description
        return export

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
    actions = [accept, reject, export_csv, export_xlsx, send_custom_email]
