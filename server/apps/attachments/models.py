from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class AbsctractAttachment(TimeStampedModel):
    file = models.FileField(_('Файл'), upload_to='attachment')

    class Meta:
        abstract = True


class PaperAttachment(AbsctractAttachment):
    to_object = models.ForeignKey(
        'papers.ResearchPaper',
        on_delete=models.PROTECT,
        verbose_name=_('Научная работа')
    )

    class Meta:
        verbose_name = _('Вложение научной работы')
        verbose_name_plural = _('Вложения научной работы')
