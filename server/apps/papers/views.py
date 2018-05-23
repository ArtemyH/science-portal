import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from apps.keywords.models import KeyWord
from apps.papers.forms import ResearchPaperForm
from .models import ResearchPaper


class KeyWordsOptionsMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        keywords_options = KeyWord.objects.values_list('value', flat=True)
        keywords_options = [
            {'value': value, 'text': value} for value in keywords_options]

        if self.object:
            keywords_values = ','.join(
                self.object.keywords.values_list('value', flat=True))
            ctx['keywords_values'] = keywords_values
        ctx['keywords_options'] = json.dumps(keywords_options)

        return ctx


class ResearchPaperListView(ListView):
    model = ResearchPaper


class ResearchPaperCreateView(LoginRequiredMixin, KeyWordsOptionsMixin,
                              CreateView):
    model = ResearchPaper
    form_class = ResearchPaperForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ResearchPaperUpdateView(LoginRequiredMixin, KeyWordsOptionsMixin,
                              UpdateView):
    model = ResearchPaper
    form_class = ResearchPaperForm

    def get_success_url(self):
        return reverse_lazy('papers:edit', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ResearchPaperDetailView(DetailView):
    model = ResearchPaper


