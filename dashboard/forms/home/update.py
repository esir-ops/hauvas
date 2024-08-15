from django import forms


class HomeUpdateForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())
