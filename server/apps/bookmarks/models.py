from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class AbsctractBookmark(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Пользователь'),
    )

    class Meta:
        abstract = True


class PaperBookmark(AbsctractBookmark):
    to_object = models.ForeignKey(
        'papers.ResearchPaper',
        on_delete=models.PROTECT,
        verbose_name=_('Научная работа')
    )

    class Meta:
        verbose_name = _('Закладка (научная работа)')
        verbose_name_plural = _('Закладки (научные работы)')
