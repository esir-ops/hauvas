from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_courses


class View(LoginRequiredMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        user = self.request.user
        session = self.request.session
        session_course_key = f"{user.id}-courses"

        if session_course_key in session:
            context["courses"] = session.get(session_course_key)
        else:
            courses = get_courses(user)

            session[session_course_key] = courses

            context["courses"] = courses

        return context


class Dashboard(View, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["link"] = "dashboard"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
