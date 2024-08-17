from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from dashboard.models import Course
from common.util.views import View
from dashboard.decorator.validation import role_have_course_access


@method_decorator(role_have_course_access, name="dispatch")
class DashboardParentView(View, TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)

        if not course_id:
            raise Http404("Course Not found!")

        course = get_object_or_404(Course, pk=course_id)

        context["title"] = f"{course.title}"
        context["link"] = "course"
        context["course"] = course

        return context
