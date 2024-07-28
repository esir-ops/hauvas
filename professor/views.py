from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_professor_courses
from .models import Course
from .forms import UpdateCourseAboutForm


page_link = "course"


class ProfessorView(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        courses = get_professor_courses(user)

        context["title"] = "Dashboard"
        context["link"] = "dashboard"
        context["courses"] = courses
        return context


class CourseView(LoginRequiredMixin, DetailView):
    model = Course

    def get_object(self, pk):
        return self.model.objects.get(pk=pk)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        user = self.request.user
        courses = get_professor_courses(user)

        context["title"] = self.object.title
        context["link"] = page_link
        context["courses"] = courses
        return context


# Create your views here.
class ProfessorDashboardView(ProfessorView):
    template_name = "professor/pages/index.html"

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())


class CourseHomeView(CourseView):
    template_name = "professor/pages/course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "home"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        pass


class CourseHomeUpdateView(CourseView):
    template_name = "professor/pages/course_update_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["sub_link"] = "home"
        return context

    def get(self, request, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)

        form = UpdateCourseAboutForm()

        context = self.get_context_data()
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)

        form = UpdateCourseAboutForm(data=request.POST)
        context = self.get_context_data()
        context["form"] = form

        if form.is_valid():
            self.object.about = form.cleaned_data.get("about")

            self.object.save()

            context["form_success"] = True

            messages.success(request, "Content Updated!")
            return render(request, self.template_name, context)
        else:
            messages.error(request, "Invalid Content!")
            return render(request, self.template_name, context)


class CourseAnnouncementView(CourseView):
    template_name = "professor/pages/course_announcement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "announcement"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        pass


class CourseSyllabusView(CourseView):
    template_name = "professor/pages/course_syllabus.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "syllabus"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        pass


class CourseModuleView(CourseView):
    template_name = "professor/pages/course_module.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "module"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        pass


class CourseAssignmentView(CourseView):
    template_name = "professor/pages/course_assignment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "assignment"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        pass


class CourseAboutView(CourseView):
    template_name = "professor/pages/course_about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "about"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        pass
