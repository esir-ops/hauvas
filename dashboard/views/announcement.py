from common.util.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from dashboard.models import Course


class Announcement(View, TemplateView):
    template_name = "dashboard/announcement/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Announcements"
        context["sub_link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
