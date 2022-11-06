from django.shortcuts import render
from django.views import View

class RenderAbout(View):
    template_name = 'about/about.html'

    def get(self, request):
        return render(request, self.template_name)