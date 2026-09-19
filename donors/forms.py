from django import forms

from accounts.models import CustomUser
from .models import DonorProfile


class DonorProfileForm(forms.ModelForm):
    full_name = forms.CharField()
    phone = forms.CharField()
    location = forms.CharField()
    blood_group = forms.ChoiceField(
        choices=CustomUser.BLOOD_GROUP_CHOICES
    )

    class Meta:
        model = DonorProfile
        fields = [
            "full_name",
            "phone",
            "location",
            "blood_group",
            "availability",
            "last_donation_date",
            "description",
        ]

        widgets = {
            "last_donation_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Tell people a little about your availability..."
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["full_name"].initial = self.instance.user.full_name
            self.fields["phone"].initial = self.instance.user.phone
            self.fields["location"].initial = self.instance.user.location
            self.fields["blood_group"].initial = self.instance.user.blood_group

    def save(self, commit=True):
        donor_profile = super().save(commit=False)

        user = donor_profile.user

        user.full_name = self.cleaned_data["full_name"]
        user.phone = self.cleaned_data["phone"]
        user.location = self.cleaned_data["location"]
        user.blood_group = self.cleaned_data["blood_group"]

        if commit:
            user.save()
            donor_profile.save()

        return donor_profile