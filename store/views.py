from django.shortcuts import render
from django.views import View

class RenderStore(View):
    template_name = 'store/store.html'

    def get(self, request):
        return render(request, self.template_name)