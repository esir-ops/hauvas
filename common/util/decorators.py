from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Group, Permission


def admin_only(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):

        # TODO: Add logic for admin only roles

        return view_func(request, *args, **kwargs)

    return wrapper


def professor_only(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):

        # TODO: Add logic for professor only roles

        return view_func(request, *args, **kwargs)

    return wrapper


def student_only(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):

        # TODO: Add logic for student only roles

        return view_func(request, *args, **kwargs)

    return wrapper
