from django.shortcuts import render
from django.views import View

class RenderContactUs(View):
    template_name = 'contactus/contact.html'

    def get(self, request):
        return render(request, self.template_name)