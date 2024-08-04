from django.urls import path
from . import views

app_name = "grade"

urlpatterns = [path("", views.GradeList.as_view(), name="grade")]
