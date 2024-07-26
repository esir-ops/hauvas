from .models import Event
from rest_framework import serializers, viewsets


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "course_id",
            "title",
            "description",
            "location",
            "date",
            "start_time",
            "end_time",
            "created_at",
            "updated_at",
        ]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
