from .models import Professor, Course
from rest_framework import serializers, viewsets


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = [
            "id",
            "user_id",
            "department_id",
            "hire_date",
            "academic_rank",
            "created_at",
            "updated_at",
        ]


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "professor_id",
            "department_id",
            "semester_id",
            "title",
            "code",
            "codename",
            "syllabus",
            "unit",
            "created_at",
            "updated_at",
        ]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
