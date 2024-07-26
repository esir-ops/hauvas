from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("", views.StudentDashboardView.as_view(), name="dashboard"),
    path("courses/<slug:slug>", views.StudentCourseView.as_view()),
    path("bookmarks/", views.StudentBookmarkView.as_view(), name="bookmark"),
    path("schedules/", views.StudentScheduleView.as_view(), name="schedule"),
    path("grades/", views.StudentGradeView.as_view(), name="grade"),
]
