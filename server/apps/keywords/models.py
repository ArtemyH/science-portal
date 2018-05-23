from django.utils.translation import ugettext_lazy as _
from django.db import models


class KeyWord(models.Model):
    value = models.CharField(
        _("Ключевое слово"),
        max_length=100
    )
    
    class Meta:
        verbose_name = _("Ключевое слово")
        verbose_name_plural = _("Ключевые слова")

    def __str__(self):
        return self.value
