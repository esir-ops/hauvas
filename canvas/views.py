from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.views.generic import TemplateView
from .forms import UserLoginForm
from main.forms import ProfileForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from common.util.get_courses import get_professor_courses
from dashboard.views.views import View


# Create your views here.
class LoginPageView(TemplateView):
    template_name = "pages/login.html"

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("dashboard:dashboard")

        form = UserLoginForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):

        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard:dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, self.template_name, {"form": form})


class LogoutPageView(TemplateView):
    def get(self, request, *args, **kwargs):

        logout(request)
        return redirect("login")


class ProfilePageView(View, TemplateView):
    template_name = "pages/profile.html"

    def get(self, request, *args, **kwargs):
        form = ProfileForm()

        context = self.get_context_data(*args, **kwargs)

        context["title"] = "Profile"
        context["link"] = "profile"
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # TODO: Update profile data
        return redirect("profile")


class SecurityPageView(View, TemplateView):
    template_name = "pages/security.html"

    def get(self, request, *args, **kwargs):
        form = ChangePasswordForm(self.request.user)

        context = self.get_context_data(*args, **kwargs)

        context["title"] = "Security"
        context["link"] = "security"
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(self.request.user, data=request.POST)

        context = self.get_context_data(*args, **kwargs)

        context["title"] = "Security"
        context["link"] = "security"
        context["form"] = form

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed successfully.")
            return render(request, self.template_name, context)
        else:
            messages.error(request, "An error occurred when changing password.")
            return render(request, self.template_name, context)
