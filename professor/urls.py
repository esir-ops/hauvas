from django.urls import path
from . import views

app_name = "professor"

urlpatterns = [
    path("", views.ProfessorDashboardView.as_view(), name="dashboard"),
    path("<int:pk>/course/", views.CourseHomeView.as_view(), name="course"),
    path(
        "<int:pk>/course/update/",
        views.CourseHomeUpdateView.as_view(),
        name="course-update-about",
    ),
    path(
        "<int:pk>/course/announcements/",
        views.CourseAnnouncementView.as_view(),
        name="course-announcement",
    ),
    path(
        "<int:pk>/course/syllabus/",
        views.CourseSyllabusView.as_view(),
        name="course-syllabus",
    ),
    path(
        "<int:pk>/course/modules/",
        views.CourseModuleView.as_view(),
        name="course-modules",
    ),
    path(
        "<int:pk>/course/assignments/",
        views.CourseAssignmentView.as_view(),
        name="course-assignments",
    ),
    path(
        "<int:pk>/course/about",
        views.CourseAboutView.as_view(),
        name="course-about",
    ),
]
