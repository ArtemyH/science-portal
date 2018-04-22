from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_extensions.db.models import TimeStampedModel


class ResearchPaper(TimeStampedModel):
    title = models.TextField(
        _("Название работы")
    )
    url = models.URLField(
        _("Ссылка на работу на сайте источника")
    )
    author = models.TextField(
        _("Автор работы")
    )

    class Meta:
        verbose_name = _("Научная статья")
        verbose_name_plural = _("Научные статьи")
