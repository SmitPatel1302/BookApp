from django.shortcuts import render
from django.views import View

class RenderContactUs(View):
    template_name = 'contactus/contact.html'

    def get(self, request):
        context = {
            'nbar':'contact'
        }
        return render(request, self.template_name, context)