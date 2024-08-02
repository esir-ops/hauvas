from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_professor_courses


# Create your views here.
class GradeView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["courses"] = courses
        return context


class GradeDashboardView(GradeView):
    template_name = "grade/pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Grades"
        context["link"] = "grade"
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())
