from django.urls import path

from . import views

app_name = 'demo3'

urlpatterns = [
    path(
        "person/update/<uuid:person_uuid>/",
        views.PersonUpdateView.as_view(),
        name="person-update",
    ),
    path(
        "person/create/",
        views.PersonCreateView.as_view(),
        name="person-create",
    ),
    path("person/list/", views.PersonListView.as_view(), name="person-list"),
    path(
        "person/detail/<uuid:person_uuid>/",
        views.PersonDetailView.as_view(),
        name="person-detail",
    ),
    path("", views.index, name="index"),
]
