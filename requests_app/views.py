from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BloodRequestForm
from .models import BloodRequest


@login_required
def create_request(request):

    if request.method == "POST":
        form = BloodRequestForm(request.POST)

        if form.is_valid():
            blood_request = form.save(commit=False)

            blood_request.requester = request.user

            blood_request.save()

            messages.success(
                request,
                "Blood request created successfully."
            )

            return redirect("requests_app:my_requests")

    else:
        form = BloodRequestForm()

    return render(
        request,
        "requests/create_request.html",
        {"form": form}
    )


@login_required
def my_requests(request):

    requests = BloodRequest.objects.filter(
        requester=request.user
    )

    paginator = Paginator(requests, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "requests/my_requests.html",
        {
            "requests": page_obj,
            "page_obj": page_obj,
        }
    )