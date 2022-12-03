from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Class to render Index page normally


class Index(View):
    template_name = 'index/index.html'

    def get(self, request):
        context = {
            'nbar': 'home'
        }
        if request.user.is_authenticated:
            username = request.user.first_name + " " + request.user.last_name
            context['username'] = username
        return render(request, self.template_name, context)

# Class to render index page after sign up


class IndexAfterSignup(View):
    template_name = 'index/index.html'

    def get(self, request):
        uname = request.user.first_name + " " + request.user.last_name
        context = {
            'nbar': 'home',
            "showModel": "true",
            "message": "You are successfully sign up! Now, you can manage your account from the profile page.",
            "username": uname
        }

        return render(request, self.template_name, context)

# Class to render index page afetr login


class IndexAfterLogin(View):
    template_name = 'index/index.html'

    def get(self, request):
        uname = request.user.first_name + ' ' + request.user.last_name
        context = {
            'nbar': 'home',
            "showModel": "true",
            "message": "Successfully logged in!",
            "username": uname
        }

        return render(request, self.template_name, context)
