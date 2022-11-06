from django.shortcuts import render
from django.views import View

class RenderAuth(View):
    template_name = 'auth/auth.html'

    def get(self, request):
        return render(request, self.template_name)