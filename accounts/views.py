from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistrationForm, LoginForm, ProfileUpdateForm
from donors.models import DonorProfile


def register_view(request):

    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()

            DonorProfile.objects.create(
                user=user
            )

            messages.success(
                request,
                "Your account has been created successfully."
            )

            return redirect("accounts:login")

    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                "Successfully logged in. Welcome back!"
            )

            return redirect("core:home")

    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )


@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("core:home")


@login_required
def profile_view(request):

    donor_profile, created = DonorProfile.objects.get_or_create(
        user=request.user
    )

    request_count = request.user.blood_requests.count()

    initials = "".join(
        [
            name[0].upper()
            for name in request.user.full_name.split()
            if name
        ]
    )[:2]

    return render(
        request,
        "accounts/profile.html",
        {
            "donor_profile": donor_profile,
            "request_count": request_count,
            "initials": initials,
        }
    )


@login_required
def profile_edit_view(request):

    donor_profile, created = DonorProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = ProfileUpdateForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your profile has been updated successfully."
            )

            return redirect(
                "accounts:profile"
            )

    else:

        form = ProfileUpdateForm(
            instance=request.user
        )

    request_count = request.user.blood_requests.count()

    initials = "".join(
        [
            name[0].upper()
            for name in request.user.full_name.split()
            if name
        ]
    )[:2]

    return render(
        request,
        "accounts/profile_edit.html",
        {
            "form": form,
            "donor_profile": donor_profile,
            "request_count": request_count,
            "initials": initials,
        }
    )