from django.contrib import admin

from apps.keywords.models import KeyWord


@admin.register(KeyWord)
class KeyWordAdmin(admin.ModelAdmin):
    pass
