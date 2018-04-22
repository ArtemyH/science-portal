from django.views.generic import ListView

from .models import ResearchPaper


class PaperListView(ListView):
    model = ResearchPaper



