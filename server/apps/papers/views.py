import json

from django.views.generic import ListView, CreateView, DetailView

from apps.keywords.models import KeyWord
from apps.papers.forms import ResearchPaperCreateForm
from .models import ResearchPaper


class ResearchPaperListView(ListView):
    model = ResearchPaper


class ResearchPaperCreateView(CreateView):
    model = ResearchPaper
    form_class = ResearchPaperCreateForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        keywords_options = KeyWord.objects.values_list('value', flat=True)
        keywords_options = [{'value': value, 'text': value} for value in keywords_options]
        ctx['keywords_options'] = json.dumps(keywords_options)

        return ctx

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ResearchPaperDetailView(DetailView):
    model = ResearchPaper


