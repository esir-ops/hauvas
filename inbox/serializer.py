from .models import Inbox
from rest_framework import serializers, viewsets


class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = [
            "id",
            "receiver_id",
            "sender_id",
            "is_starred",
            "subject",
            "content",
            "is_archived",
            "is_read",
            "sent_at",
            "read_at",
            "created_at",
            "updated_at",
        ]


class InboxViewSet(viewsets.ModelViewSet):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer
