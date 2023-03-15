from django import forms
from django.contrib.auth.hashers import make_password


class BaseUserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=8)

    def clean(self):
        super().clean()
        if self.cleaned_data.get("password1") != self.cleaned_data.get("password2"):
            msg = "Passwords do not match"
            self.add_error("password1", msg)
            self.add_error("password2", msg)

    def save(self, commit: bool):
        self.password = make_password(self.cleaned_data.get("password1"))
        return super().save(commit)
