from django.urls import path
from . import views

app_name = "announcement"

urlpatterns = [path("", views.AnnouncementDashboardView.as_view(), name="announcement")]
