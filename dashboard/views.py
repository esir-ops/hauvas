from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_professor_courses


class View(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        # TODO: Add logic for processing courses both professor and student
        # TODO: Add logic to cache and store the courses generated to request.session
        courses = get_professor_courses(user)

        context["courses"] = courses
        return context


class Dashboard(View):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
