from django.conf import settings
from django.db import models


class DonorProfile(models.Model):

    AVAILABILITY_CHOICES = [
        ("available", "Available"),
        ("not_available", "Not Available"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="donor_profile"
    )

    last_donation_date = models.DateField(
        null=True,
        blank=True
    )

    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default="available"
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.full_name} - {self.user.blood_group}"