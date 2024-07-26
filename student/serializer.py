from .models import Enrollment, Student
from rest_framework import serializers, viewsets


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student_id",
            "course_id",
            "semester_id",
            "enrollment_date",
            "completion_date",
            "status",
            "created_at",
            "updated_at",
        ]


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class StudentSerializer(serializers.ModelSerializer):
    pass


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
