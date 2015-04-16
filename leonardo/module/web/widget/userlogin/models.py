# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget


LOGIN_TYPE_CHOICES = (
    (1, _("Admin")),
    (2, _("Public")),
)


class UserLoginWidget(Widget):
    inline = models.BooleanField(verbose_name=_("inline"), default=False)
    type = models.PositiveIntegerField(verbose_name=_(
        "type"), choices=LOGIN_TYPE_CHOICES, default="Admin")

    class Meta:
        abstract = True
        verbose_name = _("user login")
        verbose_name_plural = _("user logins")
