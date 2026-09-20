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


def request_list(request):

    blood_group = request.GET.get("blood_group", "")
    location = request.GET.get("location", "")
    status = request.GET.get("status", "")

    requests = BloodRequest.objects.select_related(
        "requester"
    ).all()

    # Blood group filter
    if blood_group:
        requests = requests.filter(
            blood_group=blood_group
        )

    # Location filter
    if location:
        requests = requests.filter(
            hospital_location__icontains=location
        )

    # Status filter
    if status:
        requests = requests.filter(
            status=status
        )

    paginator = Paginator(requests, 6)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "requests": page_obj.object_list,
        "blood_group": blood_group,
        "location": location,
        "status": status,
    }

    # AJAX request 
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(
            request,
            "requests/request_results.html",
            context
        )

    return render(
        request,
        "requests/request_list.html",
        context
    )


def request_detail(request, pk):

    blood_request = get_object_or_404(
        BloodRequest,
        pk=pk
    )

    return render(
        request,
        "requests/request_detail.html",
        {
            "blood_request": blood_request
        }
    )



@login_required
def edit_request(request, pk):

    blood_request = get_object_or_404(
        BloodRequest,
        pk=pk,
        requester=request.user
    )

    if request.method == "POST":

        form = BloodRequestForm(
            request.POST,
            instance=blood_request
        )

        if form.is_valid():

            form.save()

            return redirect(
                "requests_app:detail",
                pk=blood_request.pk
            )

    else:

        form = BloodRequestForm(
            instance=blood_request
        )

    return render(
        request,
        "requests/request_edit.html",
        {
            "form": form,
            "blood_request": blood_request,
        }
    )


@login_required
def delete_request(request, pk):

    blood_request = get_object_or_404(
        BloodRequest,
        pk=pk,
        requester=request.user
    )

    if request.method == "POST":

        blood_request.delete()

        return redirect(
            "requests_app:my_requests"
        )

    return redirect(
        "requests_app:detail",
        pk=blood_request.pk
    )