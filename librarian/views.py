# This is the views.py of LIBRARIAN app
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views import View

# Class to render index page of the librarian
class RanderLibrarian(View):
    template_name =  'librarian/librarian.html'

    def get(self, request):
        return render(request, self.template_name)

# Class to render add book form
class addBookForm(View):

    def get(self, request, page_name):

        # Generating the template path according to variable passed in url
        template_name = "librarian/" + page_name + ".html"

        # Rendering desired page as a string
        page = render_to_string(template_name)

        context = {
            'pageContent' : page
        }

        return JsonResponse(context)
