from django.urls import reverse
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.bookmarks.models import PaperBookmark


class PaperBookmarkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    delete_url = serializers.SerializerMethodField()

    class Meta:
        model = PaperBookmark
        fields = ['user', 'to_object', 'delete_url']

    def get_delete_url(self, obj):
        return reverse('api:v1:paperbookmark-detail', args=[obj.id])
