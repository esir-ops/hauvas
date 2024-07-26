from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile


class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "First Name",
                "required": True,
            }
        ),
    )

    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Middle Name",
                "required": True,
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Last Name",
                "required": True,
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Email Address",
                "required": True,
            }
        )
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        )
    )

    gender = forms.CharField(
        widget=forms.Select(
            choices=[("", "---"), ("M", "Male"), ("F", "Female")],
            attrs={
                "type": "text",
                "class": "form-select",
                "placeholder": "Last Name",
                "required": True,
            },
        )
    )

    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Contact No",
                "required": True,
            }
        )
    )

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Your Bio",
                "required": True,
            }
        )
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "City",
                "required": True,
            }
        )
    )

    province = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Province",
                "required": True,
            }
        )
    )

    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "country",
                "required": True,
            }
        )
    )

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "contact_number",
            "bio",
            "city",
            "province",
            "country",
        ]


class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Current password",
                "required": True,
            }
        ),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Enter new password",
                "required": True,
            }
        ),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Confirm new password",
                "required": True,
            }
        ),
    )
