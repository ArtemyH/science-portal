from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.attachments.models import PaperAttachment
from apps.bookmarks.models import PaperBookmark
from .serializers import PaperBookmarkSerializer


class PermissionAndAuthMixin(object):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


class PaperAttachmentViewSet(PermissionAndAuthMixin, mixins.DestroyModelMixin,
                             GenericViewSet):
    queryset = PaperAttachment.objects.none()

    def get_queryset(self):
        return PaperAttachment.objects.filter(to_object__user=self.request.user)


class PaperBookmarkViewSet(PermissionAndAuthMixin, mixins.CreateModelMixin,
                           mixins.DestroyModelMixin, GenericViewSet):
    queryset = PaperBookmark.objects.none()
    serializer_class = PaperBookmarkSerializer

    def get_queryset(self):
        return PaperBookmark.objects.filter(user=self.request.user)