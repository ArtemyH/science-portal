from django.views.generic import TemplateView


class MainTemplateView(TemplateView):

    def get_template_names(self):
        return [self.kwargs.get('path', 'base.html')]
