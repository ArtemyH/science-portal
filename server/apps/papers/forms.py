from django import forms

from apps.keywords.models import KeyWord
from apps.papers.models import ResearchPaper


class ResearchPaperCreateForm(forms.ModelForm):
    keywords = forms.CharField()
    
    class Meta:
        model = ResearchPaper
        fields = ['title', 'abstract', 'keywords']

    def __init__(self, user, **kwargs):
        self.user = user
        super().__init__(**kwargs)

    def clean(self):
        return super().clean()

    def clean_keywords(self):
        import pudb; pudb.set_trace()
        data = self.cleaned_data['keywords']
        values = data.split(',')
        
        def get_keywords_by_value(value):
            keyword, created = KeyWord.objects.get_or_create(
                value=value, defaults={'value': value}
            )
            return keyword
        
        return [get_keywords_by_value(v).id for v in values]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        return super().save(commit)
