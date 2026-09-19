from django.shortcuts import render

from django.shortcuts import render

from donors.models import DonorProfile
from requests_app.models import BloodRequest


def home(request):

    blood_groups = [
        "A+",
        "A-",
        "B+",
        "B-",
        "AB+",
        "AB-",
        "O+",
        "O-",
    ]

    blood_group_data = []

    for blood_group in blood_groups:

        available_count = DonorProfile.objects.filter(
            user__blood_group=blood_group,
            availability="available"
        ).count()

        blood_group_data.append({
            "name": blood_group,
            "count": available_count,
        })

    context = {
        "registered_donors": DonorProfile.objects.count(),

        "available_donors": DonorProfile.objects.filter(
            availability="available"
        ).count(),

        "total_requests": BloodRequest.objects.count(),

        "pending_requests": BloodRequest.objects.filter(
            status="pending"
        ).count(),

        "blood_group_data": blood_group_data,

        "latest_requests": BloodRequest.objects.filter(
            status="pending"
        )[:3],
    }

    return render(
        request,
        "core/home.html",
        context
    )