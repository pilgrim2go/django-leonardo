# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget


class DownloadListWidget(Widget):
    folder = models.ForeignKey('filer.Folder', verbose_name=_("folder"))

    class Meta:
        abstract = True
        verbose_name = _("download list")
        verbose_name_plural = _('download lists')
