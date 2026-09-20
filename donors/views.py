from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DonorProfileForm
from .models import DonorProfile
from django.core.paginator import Paginator


@login_required
def donor_edit(request):
    donor_profile, created = DonorProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = DonorProfileForm(
            request.POST,
            instance=donor_profile
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Donor profile updated successfully."
            )

            return redirect(
                "donors:detail",
                pk=donor_profile.pk
            )

    else:
        form = DonorProfileForm(
            instance=donor_profile
        )

    return render(
        request,
        "donors/profile_edit.html",
        {
            "form": form,
            "donor_profile": donor_profile,
        }
    )


@login_required
def donor_detail(request, pk):
    donor_profile = get_object_or_404(
        DonorProfile.objects.select_related("user"),
        pk=pk
    )

    return render(
        request,
        "donors/profile_detail.html",
        {
            "donor_profile": donor_profile,
        }
    )


@login_required
def donor_delete(request, pk):
    donor_profile = get_object_or_404(
        DonorProfile,
        pk=pk
    )

    if donor_profile.user != request.user:
        messages.error(
            request,
            "You can only delete your own donor profile."
        )

        return redirect(
            "donors:detail",
            pk=donor_profile.pk
        )

    if request.method == "POST":
        donor_profile.delete()

        messages.success(
            request,
            "Donor profile deleted successfully."
        )

        return redirect("core:home")

    return redirect(
        "donors:detail",
        pk=donor_profile.pk
    )




def donor_list(request):

    donors = DonorProfile.objects.select_related("user").all()

    # Blood group filter
    blood_group = request.GET.get("blood_group", "")

    if blood_group:
        donors = donors.filter(
            user__blood_group=blood_group
        )

    # Location filter
    location = request.GET.get("location", "").strip()

    if location:
        donors = donors.filter(
            user__location__icontains=location
        )

    # Availability filter
    availability = request.GET.get("availability", "")

    if availability:
        donors = donors.filter(
            availability=availability
        )

    # Pagination
    paginator = Paginator(donors, 6)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    # Keep filters while changing pages
    query_params = request.GET.copy()

    if "page" in query_params:
        query_params.pop("page")

    return render(
        request,
        "donors/donor_list.html",
        {
            "page_obj": page_obj,
            "donors": page_obj.object_list,
            "blood_group": blood_group,
            "location": location,
            "availability": availability,
            "query_params": query_params.urlencode(),
            "total_donors": paginator.count,
        }
    )


# def donor_detail(request, pk):

#     donor = get_object_or_404(
#         DonorProfile.objects.select_related("user"),
#         pk=pk
#     )

#     return render(
#         request,
#         "donors/donor_detail.html",
#         {
#             "donor": donor
#         }
#     )