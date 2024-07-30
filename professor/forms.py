from django import forms
from .models import Course, ModuleList, ModuleItem


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


class UpdateModuleListForm(forms.ModelForm):
    class Meta:
        model = ModuleList
        fields = ["title"]


class UpdateModuleItemForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    content_url = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    is_published = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    def __init__(self, *args, **kwargs):
        course_pk = kwargs.pop("course_pk", "")

        super(UpdateModuleItemForm, self).__init__(*args, **kwargs)

        self.fields["module_list"] = forms.ModelChoiceField(
            queryset=ModuleList.objects.filter(course_id=course_pk),
            widget=forms.Select(attrs={"class": "form-control"}),
        )

    class Meta:
        model = ModuleItem
        fields = [
            "title",
            "description",
            "content_url",
            "is_published",
        ]
