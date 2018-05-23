from django.contrib import admin

from apps.papers.models import ResearchPaper


@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    filter_horizontal = ['keywords']
