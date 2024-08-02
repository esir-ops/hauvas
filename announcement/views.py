from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_professor_courses


# Create your views here.
class AnnouncementView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["courses"] = courses
        return context


class AnnouncementDashboardView(AnnouncementView):
    template_name = "announcement/pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Announcements"
        context["link"] = "announcement"
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())
