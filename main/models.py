from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    GENDER_CHOICE = [("M", "Male"), ("F", "Female")]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    date_of_birth = models.DateField(max_length=15, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, blank=True)
    contact_number = models.CharField(max_length=11, blank=True)
    bio = models.TextField(blank=True)
    img_url = models.URLField(blank=True)
    zip_code = models.CharField(max_length=4, blank=True)
    city = models.CharField(max_length=50, blank=True)
    province = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True, default="Philippines")
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Department(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    TERM_CHOICES = [("1st", "1st"), ("2nd", "2nd"), ("3rd", "3rd")]
    term = models.CharField(max_length=3, choices=TERM_CHOICES)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.term} {self.start_year}-{self.end_year}"
