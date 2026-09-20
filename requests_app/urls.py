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

]