from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.attachments.models import PaperAttachment


class PaperAttachmentViewSet(mixins.DestroyModelMixin, GenericViewSet):
    queryset = PaperAttachment.objects.none()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        return PaperAttachment.objects.filter(to_object__user=self.request.user)
