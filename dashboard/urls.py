from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.Dashboard.as_view(), name="dashboard"),
    path("<int:course_id>/home/", views.Dashboard.as_view(), name="course-home"),
    path(
        "<int:course_id>/syllabus/", views.Dashboard.as_view(), name="course-syllabus"
    ),
    path(
        "<int:course_id>/announcements/",
        views.Dashboard.as_view(),
        name="course-announcement",
    ),
    path("<int:course_id>/modules/", views.Dashboard.as_view(), name="course-module"),
    path(
        "<int:course_id>/assignments/",
        views.Dashboard.as_view(),
        name="course-assignment",
    ),
]
