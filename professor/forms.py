from django import forms
from .models import Course


class UpdateCourseAboutForm(forms.ModelForm):

    about = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "class": "form-control d-none",
                "placeholder": "Update your 'About the Course' here...",
                # TODO: Remove value after testing
                "value": "Test value for About",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Course
        fields = ["about"]


class UpdateCourseSyllabusForm(forms.ModelForm):

    syllabus = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "class": "form-control d-none",
                "placeholder": "Update your 'syllabus' here...",
                # TODO: Remove value after testing
                "value": "Test value for syllabus",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Course
        fields = ["syllabus"]
