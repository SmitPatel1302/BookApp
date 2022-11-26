from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from contactus.models import ContactUs
from django.http import JsonResponse

# Class to render contact us page
class RenderContactUs(View):
    template_name = 'contactus/contact.html'

    def get(self, request):
        context = {
            'nbar':'contact'
        }
        return render(request, self.template_name, context)

# Class to handle contact us data
class SubmitContactForm(View):

     def post(self, request):
        contactObj = ContactUs()
        contactObj.fullname = request.POST.get('contact_name')
        contactObj.email = request.POST.get('contact_email')
        contactObj.subject = request.POST.get('contact_subject')
        contactObj.message = request.POST.get('contact_message')
        contactObj.save()

        context = {
            'success':'true',
            'message':'Your Response hasbeen submitted successfully!'
        }
        return JsonResponse(context)