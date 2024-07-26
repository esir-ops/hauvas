from .models import Department, Profile, Semester
from rest_framework import serializers, viewsets


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "abbr", "created_at", "updated_at"]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user_id",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "contact_number",
            "bio",
            "img_url",
            "zip_code",
            "city",
            "province",
            "country",
            "is_student",
            "is_professor",
            "created_at",
            "updated_at",
        ]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
