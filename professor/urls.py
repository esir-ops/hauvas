from django.urls import path
from . import views

app_name = "professor"

urlpatterns = [
    path("", views.ProfessorDashboardView.as_view(), name="dashboard"),
    path("<int:pk>/course/", views.ProfessorCourseView.as_view(), name="course"),
    path(
        "<int:pk>/course/announcements/",
        views.ProfessorCourseAnnouncementView.as_view(),
        name="course-announcement",
    ),
    path(
        "<int:pk>/course/syllabus/",
        views.ProfessorCourseSyllabusView.as_view(),
        name="course-syllabus",
    ),
    path(
        "<int:pk>/course/modules/",
        views.ProfessorCourseModuleView.as_view(),
        name="course-modules",
    ),
    path(
        "<int:pk>/course/assignments/",
        views.ProfessorCourseAssignmentView.as_view(),
        name="course-assignments",
    ),
    path(
        "<int:pk>/course/about",
        views.ProfessorCourseAboutView.as_view(),
        name="course-about",
    ),
]
