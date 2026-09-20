from django import forms
from .models import BloodRequest


class BloodRequestForm(forms.ModelForm):

    class Meta:
        model = BloodRequest

        fields = [
            "patient_name",
            "blood_group",
            "bags_required",
            "hospital_name",
            "hospital_location",
            "required_date",
            "contact_number",
            "description",
        ]

        widgets = {
            "patient_name": forms.TextInput(
                attrs={
                    "placeholder": "Rahim Ahmed"
                }
            ),

            "blood_group": forms.Select(),

            "bags_required": forms.NumberInput(
                attrs={
                    "min": 1,
                    "placeholder": "1"
                }
            ),

            "hospital_name": forms.TextInput(
                attrs={
                    "placeholder": "Dhaka Medical College Hospital"
                }
            ),

            "hospital_location": forms.TextInput(
                attrs={
                    "placeholder": "Dhaka"
                }
            ),

            "required_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "contact_number": forms.TextInput(
                attrs={
                    "placeholder": "01xxxxxxxxx"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe the situation briefly...",
                    "rows": 4
                }
            ),
        }