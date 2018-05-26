from rest_framework.routers import DefaultRouter

from .views import PaperAttachmentViewSet


app_name = 'v1'

router = DefaultRouter()

router.register('paper-attachment', PaperAttachmentViewSet)

urlpatterns = router.urls
