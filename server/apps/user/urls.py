from django.urls import path, include

from apps.user.views import UserEditView


urlpatterns = [
    path('accounts/profile/', UserEditView.as_view(), name='user_edit'),
    path('accounts/', include('allauth.urls')),
]
