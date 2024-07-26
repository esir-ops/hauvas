from .models import Announcement
from rest_framework import serializers, viewsets


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            "id",
            "course_id",
            "title",
            "content",
            "posted_at",
            "created_at",
            "updated_at",
        ]


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
