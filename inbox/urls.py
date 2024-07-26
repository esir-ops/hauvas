from django.urls import path
from . import views

app_name = "inbox"

urlpatterns = [path("", views.InboxDashboardView.as_view(), name="inbox")]
