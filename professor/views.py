from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_professor_courses
from .models import Course, ModuleItem
from .forms import UpdateCourseAboutForm, UpdateCourseSyllabusForm, UpdateModuleItemForm
from common.util.get_modules import get_modules


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


class CourseSyllabusUpdateView(CourseView):
    template_name = "professor/pages/course_update_syllabus.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["sub_link"] = "home"
        return context

    def get(self, request, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)

        form = UpdateCourseSyllabusForm()

        context = self.get_context_data()
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)

        form = UpdateCourseSyllabusForm(data=request.POST)
        context = self.get_context_data()
        context["form"] = form

        if form.is_valid():
            self.object.syllabus = form.cleaned_data.get("syllabus")

            self.object.save()

            context["form_success"] = True

            messages.success(request, "Content Updated!")
            return render(request, self.template_name, context)
        else:
            messages.error(request, "Invalid Content!")
            return render(request, self.template_name, context)


class CourseModuleView(CourseView):
    template_name = "professor/pages/course_module.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "module"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)

        context = self.get_context_data()

        modules = get_modules(self.object.modules.all())

        context["modules"] = modules

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


class CourseModuleItemView(CourseView):
    template_name = "professor/pages/course_read_module.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "module"
        return context

    def get(self, request, *args, **kwargs):
        course_pk = kwargs.get("pk")
        module_item_pk = kwargs.get("item_id")
        self.object = self.get_object(pk=course_pk)

        context = self.get_context_data()

        module_item = ModuleItem.objects.get(pk=module_item_pk)

        context["module_item"] = module_item

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


class CourseModuleCreateView(CourseView):
    template_name = "professor/pages/course_create_module.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "module"
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.object = self.get_object(pk=pk)

        context = self.get_context_data()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


class CourseModuleUpdateView(CourseView):
    template_name = "professor/pages/course_update_module.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sub_link"] = "module"
        return context

    def get(self, request, *args, **kwargs):
        course_pk = kwargs.get("pk")
        module_item_pk = kwargs.get("item_id")
        self.object = self.get_object(pk=course_pk)

        module_item = ModuleItem.objects.get(pk=module_item_pk)
        form = UpdateModuleItemForm(module_item=module_item)

        context = self.get_context_data()

        context["module_item"] = module_item
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        course_pk = kwargs.get("pk")
        module_item_pk = kwargs.get("item_id")
        self.object = self.get_object(pk=course_pk)

        module_item = ModuleItem.objects.get(pk=module_item_pk)
        form = UpdateModuleItemForm(module_item=module_item, data=request.POST)

        context = self.get_context_data()

        context["module_item"] = module_item
        context["form"] = form

        if form.is_valid():
            title = form.cleaned_data.get("title")
            short_description = form.cleaned_data.get("short_description")
            description = form.cleaned_data.get("description")
            content_url = form.cleaned_data.get("content_url")
            is_published = form.cleaned_data.get("is_published")

            module_item.title = title
            module_item.short_description = short_description
            module_item.description = description
            module_item.content_url = content_url
            module_item.is_published = is_published

            module_item.save()
            context["form_success"] = True
            messages.success(request, "Module updated!")
        else:
            messages.error(request, "An error occurred when updating the module!")
            print("The form is not valid!")

        return render(request, self.template_name, context)


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
