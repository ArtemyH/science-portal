from django.urls import path

from apps.papers.views import (
    ResearchPaperCreateView, ResearchPaperDetailView, ResearchPaperListView,
    ResearchPaperUpdateView)

app_name = 'papers'
urlpatterns = [
    path('create/', ResearchPaperCreateView.as_view(), name='create'),
    path('', ResearchPaperListView.as_view(), name='list'),
    path('<int:pk>/', ResearchPaperDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', ResearchPaperUpdateView.as_view(), name='edit'),
]
