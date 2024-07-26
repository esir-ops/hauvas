from django_components import component


@component.register("sidebar")
class Sidebar(component.Component):
    template_name = "template.html"

    def get_context_data(self):
        return {}

    class Media:
        css = "style.css"
        js = "script.js"
