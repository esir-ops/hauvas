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
        "<int:pk>/course/syllabus/update/",
        views.CourseSyllabusUpdateView.as_view(),
        name="course-update-syllabus",
    ),
    path(
        "<int:pk>/course/modules/",
        views.CourseModuleView.as_view(),
        name="course-modules",
    ),
    path(
        "<int:pk>/course/modules/<int:item_id>/",
        views.CourseModuleItemView.as_view(),
        name="course-view-module",
    ),
    path(
        "<int:pk>/course/modules/create/",
        views.CourseModuleCreateView.as_view(),
        name="course-create-module",
    ),
    path(
        "<int:pk>/course/modules/<int:item_id>/update/",
        views.CourseModuleUpdateView.as_view(),
        name="course-update-module",
    ),
    path(
        "<int:pk>/course/assignments/",
        views.CourseAssignmentView.as_view(),
        name="course-assignments",
    ),
]
