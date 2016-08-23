from import_export import resources
from goto.models import Application

from goto.utils import modeladmin_fields
from goto.models import Application

class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application
        fields = modeladmin_fields(Application,children_fields=['participant'])
        # fields = ('participant__first_name', 'participant__last_name', 'participant__city', 'participant__birthday')

    def get_export_order(self):
        # order = tuple(self._meta.export_order or ())
        ret = self.current_fields
        return ret
        # return order + tuple(k for k in self.fields.keys() if k not in order)
