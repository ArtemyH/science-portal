import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.documentation import include_docs_urls

from core.views import MainTemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.user.urls')),
    path('papers/', include('apps.papers.urls', namespace='papers')),
    path('api/', include('api.urls', namespace='api')),
]

if settings.DEBUG:

    urlpatterns += [
        path('docs/', include_docs_urls(title='Portal API Docs')),
        path('<path>', MainTemplateView.as_view(), name='path'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if int(os.getenv('ENABLE_DEBUG_TOOLBAR', 1)):
        import debug_toolbar

        urlpatterns = [
            path(r'__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
