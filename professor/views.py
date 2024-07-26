from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_professor_courses
from .models import Course


page_title = "Courses"
page_link = "course"


# Create your views here.
class ProfessorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "professor/pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = "Dashboard"
        context["link"] = "dashboard"
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())


class ProfessorCourseView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "professor/pages/course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = page_title
        context["link"] = page_link
        context["sub_link"] = "home"
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())


class ProfessorCourseAnnouncementView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "professor/pages/course_announcement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = page_title
        context["link"] = page_link
        context["sub_link"] = "announcement"
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())


class ProfessorCourseSyllabusView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "professor/pages/course_syllabus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = page_title
        context["link"] = page_link
        context["sub_link"] = "syllabus"
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())


class ProfessorCourseModuleView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "professor/pages/course_module.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = page_title
        context["link"] = page_link
        context["sub_link"] = "module"
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())


class ProfessorCourseAssignmentView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "professor/pages/course_assignment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = page_title
        context["link"] = page_link
        context["sub_link"] = "assignment"
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())


class ProfessorCourseAboutView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "professor/pages/course_about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = page_title
        context["link"] = page_link
        context["sub_link"] = "about"
        # TODO: Create a fetch function for getting the enrolled courses of each student
        context["courses"] = courses
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, self.template_name, self.get_context_data())
