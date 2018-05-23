from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.keywords.models import KeyWord

User = get_user_model()


class ResearchPaper(TimeStampedModel):
    title = models.TextField(
        _("Название работы")
    )
    url = models.URLField(
        _("Ссылка на работу на сайте источника"),
        null=True,
        blank=True
    )
    author = models.TextField(
        _("Автор работы")
    )
    user = models.ForeignKey(
        User,
        models.PROTECT,
        verbose_name=_("Пользователь")
    )
    keywords = models.ManyToManyField(
        KeyWord,
        verbose_name=_("Ключевые слова")
    )
    abstract = models.TextField(
        _("Аннотация"),
        blank=True
    )

    class Meta:
        verbose_name = _("Научная статья")
        verbose_name_plural = _("Научные статьи")

    def get_absolute_url(self):
        return reverse('papers:detail', kwargs={'pk': self.pk})
