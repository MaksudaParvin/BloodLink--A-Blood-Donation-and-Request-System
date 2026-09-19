from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DonorProfileForm
from .models import DonorProfile


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