# This is the views.py of LIBRARIAN app
from django.shortcuts import render
from django.views import View

class RanderLibrarian(View):
    template_name =  'librarian/librarian.html'

    def get(self, request):
        return render(request, self.template_name)