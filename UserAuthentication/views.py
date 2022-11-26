from django.shortcuts import render
from django.views import View

# Class to render authentication page
class RenderUserAuthentication(View):
    template_name = 'auth/auth.html'

    def get(self, request):
        return render(request, self.template_name)

# Class to render login page
class RenderLogin(View):
    template_name = 'auth/login.html'

    def get(self, request):
        return render(request, self.template_name)

# Class to render sign up page
class RenderSignup(View):
    template_name = 'auth/signup.html'

    def get(self, request):
        return render(request, self.template_name)