from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = [
            "full_name",
            "email",
            "phone",
            "blood_group",
            "location",
            "date_of_birth",
            "profile_picture",
        ]

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):

    username = forms.EmailField(
        label="Email Address"
    )