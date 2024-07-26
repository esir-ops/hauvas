from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.views import View
from .forms import UserLoginForm
from main.forms import ProfileForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


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


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return redirect("login")


class LoginPageView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        form = UserLoginForm()
        return render(request, "pages/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "pages/login.html", {"form": form})


class LogoutPageView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")


class DashboardPageView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_student:
                return redirect("student:dashboard")
            elif request.user.profile.is_professor:
                return redirect("professor:dashboard")
            else:
                return redirect("login")
        else:
            return redirect("login")


class ProfilePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()

        context = {
            "title": "Profile",
            "link": "profile",
            "courses": courses,
            "form": form,
        }

        return render(request, "pages/profile.html", context)

    def post(self, request, *args, **kwargs):
        # TODO: Update profile data
        return redirect("profile")


class SecurityPageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ChangePasswordForm(self.request.user)

        context = {
            "title": "Security",
            "link": "security",
            "courses": courses,
            "form": form,
        }

        return render(
            request,
            "pages/security.html",
            context,
        )

    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(self.request.user, data=request.POST)

        context = {
            "title": "Security",
            "link": "security",
            "courses": courses,
            "form": form,
        }

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed successfully.")
            return render(
                request,
                "pages/security.html",
                context,
            )
        else:
            messages.error(request, "An error occurred when changing password.")
            return render(
                request,
                "pages/security.html",
                context,
            )
