from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
courses = [
    {
        "name": "Data Analysis",
        "course_code": "4714",
        "codename": "DATANALYSIS",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Differentials",
        "course_code": "4396",
        "codename": "DIFFEQUATIONS",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Engineering Economics",
        "course_code": "4399",
        "codename": "ENGGECON",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Ethics",
        "course_code": "4394",
        "codename": "4ETHICS",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Fundamental of Electrical Circuit",
        "course_code": "4400",
        "codename": "ELECIRCUIT",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Fundamental of Electrical Circuit Laboratory",
        "course_code": "4401",
        "codename": "ELECIRCUITL",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Switching and Routing Essentials",
        "course_code": "4403",
        "codename": "INCOMTECH1",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Life and Works of Rizal",
        "course_code": "4395",
        "codename": "4RIZAL",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Objective-Oriented Programming",
        "course_code": "4402",
        "codename": "OBJORPROG",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
    {
        "name": "Physical Education 3",
        "course_code": "9466",
        "codename": "7TPE3",
        "sy": "2024-2025",
        "semester": "1st",
        "link": "https://example.com",
    },
]

page_title = "Events"
page_link = "event"


class EventDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "event/pages/index.html"

    def get_context_data(self, **kwargs):
        user = self.request.user

        context = super().get_context_data(**kwargs)
        context["title"] = page_title
        context["link"] = page_link
        context["user"] = user
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context
