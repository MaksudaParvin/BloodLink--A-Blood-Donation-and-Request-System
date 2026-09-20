from django.urls import path

from . import views


app_name = "donors"


urlpatterns = [
    path(
        "profile/edit/",
        views.donor_edit,
        name="edit"
    ),

    path(
        "profile/<int:pk>/",
        views.donor_detail,
        name="detail"
    ),

    path(
        "profile/<int:pk>/delete/",
        views.donor_delete,
        name="delete"
    ),

    path(
        "",
        views.donor_list,
        name="list"
    ),

    # path(
    #     "profile/<int:pk>/",
    #     views.donor_detail,
    #     name="detail"
    # ),
]