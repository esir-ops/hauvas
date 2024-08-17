from django.shortcuts import render

from dashboard.util.view import DashboardParentView


class People(DashboardParentView):
    template_name = "dashboard/people/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} People"
        context["sub_link"] = "people"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
