from django.urls import path
from .views.views import Dashboard
from .views.home import Home


app_name = "dashboard"

urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path("<int:course_id>/home/", Home.as_view(), name="course-home"),
    path("<int:course_id>/syllabus/", Dashboard.as_view(), name="course-syllabus"),
    path(
        "<int:course_id>/announcements/",
        Dashboard.as_view(),
        name="course-announcement",
    ),
    path("<int:course_id>/modules/", Dashboard.as_view(), name="course-module"),
    path(
        "<int:course_id>/assignments/",
        Dashboard.as_view(),
        name="course-assignment",
    ),
]
