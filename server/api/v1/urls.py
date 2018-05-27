from rest_framework.routers import DefaultRouter

from .views import PaperAttachmentViewSet, PaperBookmarkViewSet

app_name = 'v1'

router = DefaultRouter()

router.register('paper-attachment', PaperAttachmentViewSet)
router.register('paper-bookmark', PaperBookmarkViewSet)

urlpatterns = router.urls
