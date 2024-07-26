from django.urls import path
from . import views

app_name = "event"

urlpatterns = [path("", views.EventDashboardView.as_view(), name="event")]
