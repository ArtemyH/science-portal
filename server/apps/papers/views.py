import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from apps.attachments.models import PaperAttachment
from apps.bookmarks.models import PaperBookmark
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


class AttachmentCreateMixin(object):
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.files = request.FILES.getlist('attachments')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        for f in self.files:
            PaperAttachment.objects.create(file=f, to_object=self.object)
        return HttpResponseRedirect(self.get_success_url())


class ResearchPaperListView(ListView):
    model = ResearchPaper


class ResearchPaperCreateView(AttachmentCreateMixin, LoginRequiredMixin,
                              KeyWordsOptionsMixin, CreateView):
    model = ResearchPaper
    form_class = ResearchPaperForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ResearchPaperUpdateView(AttachmentCreateMixin, LoginRequiredMixin,
                              KeyWordsOptionsMixin, UpdateView):
    model = ResearchPaper
    form_class = ResearchPaperForm

    def get_success_url(self):
        return reverse_lazy('papers:edit', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class ResearchPaperDetailView(DetailView):
    model = ResearchPaper

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bookmark'] = PaperBookmark.objects.filter(
            user=self.request.user,
            to_object=self.object
        ).first() or None
        return ctx



