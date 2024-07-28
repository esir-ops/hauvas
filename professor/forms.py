from django import forms
from .models import Course


class UpdateCourseAboutForm(forms.ModelForm):

    about = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Update your 'About the Course' here...",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Course
        fields = ["about"]
