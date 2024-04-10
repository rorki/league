from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("team/<int:id>", views.team, name="team"),
    path("admin", views.admin, name="admin")
]