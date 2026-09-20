from django.urls import path

from . import views


app_name = "requests_app"


urlpatterns = [

    path(
        "create/",
        views.create_request,
        name="create"
    ),

    path(
        "my/",
        views.my_requests,
        name="my_requests"
    ),

    path(
        "",
        views.request_list,
        name="list"
    ),

    path(
        "<int:pk>/",
        views.request_detail,
        name="detail"
    ),

    path(
        "<int:pk>/edit/",
        views.edit_request,
        name="edit"
    ),

    path(
        "<int:pk>/delete/",
        views.delete_request,
        name="delete"
    ),
]