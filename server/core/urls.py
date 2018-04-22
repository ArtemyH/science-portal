import os

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls

from core.views import MainTemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.papers.urls', namespace='papers')),
] + i18n_patterns(
    path('api/', include('api.urls', namespace='api')),
)

if settings.DEBUG:

    urlpatterns += [
        path('<path>', MainTemplateView.as_view(), name='path'),
    ]

    urlpatterns = i18n_patterns(
        path('docs/', include_docs_urls(title='Portal API Docs')),
    ) + urlpatterns

    if int(os.getenv('ENABLE_DEBUG_TOOLBAR', 1)):
        import debug_toolbar

        urlpatterns = [
            path(r'__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
