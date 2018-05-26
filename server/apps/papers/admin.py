from django.contrib import admin

from apps.attachments.models import PaperAttachment
from apps.papers.models import ResearchPaper


class PapersAttachmentsInline(admin.TabularInline):
    model = PaperAttachment
    extra = 0


@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    filter_horizontal = ['keywords']
    inlines = [PapersAttachmentsInline]
