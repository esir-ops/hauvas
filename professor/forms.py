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
                "value": "Test Value",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Course
        fields = ["about"]
