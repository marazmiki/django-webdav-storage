import os
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


def upload_to(model_instance, filename):
    return os.path.join('files', '{filename}.{extension}'.format(
        filename=uuid.uuid4(),
        extension=os.path.splitext(filename)[1].lower().strip('.'),
    ))


class File(models.Model):
    file = models.FileField(upload_to=upload_to)

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')
