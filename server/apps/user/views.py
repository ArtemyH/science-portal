from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView


User = get_user_model()


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['last_name', 'first_name', 'middle_name', 'text_about']

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        # возвращаемся на страницу, с которой пришли
        return self.request.get_full_path()
