from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ExampleAppConfig(AppConfig):
    name = 'example_app'
    verbose_name = _('The example application')
