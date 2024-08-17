from django.shortcuts import render

from dashboard.util.view import DashboardParentView
from dashboard.forms.home.update import HomeUpdateForm


class Home(DashboardParentView):
    template_name = "dashboard/home/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Home"
        context["sub_link"] = "home"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class HomeUpdate(DashboardParentView):
    template_name = "dashboard/home/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"Update {context['title']} About"
        context["sub_link"] = "home"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        context["form"] = HomeUpdateForm()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
