from .models import Todo
from rest_framework import serializers, viewsets


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "id",
            "course_id",
            "user_id",
            "title",
            "description",
            "due_date",
            "is_complete",
            "created_at",
            "updated_at",
        ]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
