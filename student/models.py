from django.db import models
from django.conf import settings


# Create your models here.
class Student(models.Model):
    ACADEMIC_STATUS_CHOICES = [
        ("Active", "Active"),
        ("On leave", "On leave"),
        ("Suspended", "Suspended"),
        ("Excused", "Excused"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student"
    )
    block = models.ForeignKey(
        "main.Block", on_delete=models.CASCADE, related_name="students"
    )
    department = models.ForeignKey(
        "main.Department",
        on_delete=models.CASCADE,
        related_name="students",
    )
    major = models.CharField(max_length=254)
    year = models.IntegerField()
    academic_status = models.CharField(
        max_length=254, choices=ACADEMIC_STATUS_CHOICES, default="Active"
    )
    is_graduated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.department.name}"


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ("Enrolled", "Enrolled"),
        ("Withdrawn", "Withdrawn"),
        ("Dropped", "Dropped"),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        "professor.Course",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    semester = models.ForeignKey(
        "main.Semester",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    enrollment_date = models.DateTimeField()
    completion_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
