from allauth.account.views import EmailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import ContextMixin

from .forms import ProfileEditForm

User = get_user_model()


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileEditForm
    success_url = reverse_lazy('account_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(profile_form=form))

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_form()
        return super(ContextMixin).get_context_data(**kwargs)


class ProfileView(LoginRequiredMixin, EmailView):
    success_url = reverse_lazy('account_profile')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['profile_form'] = ProfileEditForm(instance=self.request.user)
        return ctx

    def post(self, request, *args, **kwargs):
        if 'action_profile_edit' in request.POST:
            return self._action_profile_edit(request)
        return super().post(request, *args, **kwargs)

    def _action_profile_edit(self, request):
        profile_form = ProfileEditForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(self.success_url)


