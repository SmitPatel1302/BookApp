from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Index(View):
    template_name = './index/index.html'

    def get(self, request):
        context={
            'nbar':'home'
        }
        return render(request, self.template_name, context)
