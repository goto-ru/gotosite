from import_export import resources
from goto.models import Application


class ApplicationResource(resources.ModelResource):
    class Meta:
        model = Application
        fields = ('id', 'name')
