from django.db import models
from django.conf import settings


# Create your models here.
class Professor(models.Model):
    ACADEMIC_RANK_CHOICES = [
        ("Professor", "Professor"),
        ("Assistant Professor", "Assistant Professor"),
        ("Associate Professor", "Associate Professor"),
        ("Full Professor", "Full Professor"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="professor",
    )
    department = models.ForeignKey(
        "main.Department",
        on_delete=models.CASCADE,
        related_name="professors",
    )
    hire_date = models.DateTimeField()
    academic_rank = models.CharField(
        max_length=254, choices=ACADEMIC_RANK_CHOICES, default="Professor"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.department.name}"


class Course(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="courses"
    )
    department = models.ForeignKey(
        "main.Department",
        on_delete=models.CASCADE,
        related_name="department",
    )
    semester = models.ForeignKey(
        "main.Semester", on_delete=models.CASCADE, related_name="semester"
    )
    title = models.CharField(max_length=254)
    code = models.CharField(max_length=6)
    codename = models.CharField(max_length=20)
    syllabus = models.TextField()
    unit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.professor.user.profile.first_name} | {self.code}:{self.codename} - {self.title}"
