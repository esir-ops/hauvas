from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from dashboard.models import Course
from dashboard.forms.home.update import HomeUpdateForm
from common.util.views import View


class HomeParent(View, TemplateView):
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


class Home(HomeParent):
    template_name = "dashboard/home/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Home"
        context["sub_link"] = "home"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class HomeUpdate(HomeParent):
    template_name = "dashboard/home/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"Update {context['title']} About"
        context["sub_link"] = "home"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        context["form"] = HomeUpdateForm()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
