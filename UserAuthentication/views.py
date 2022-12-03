from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic.edit import FormView
from UserAuthentication.forms import SignupForm, LoginForm
from UserAuthentication.models import CustomUserAuthentication
from UserAuthentication.addressModel import UserAddress
from django.contrib.auth import authenticate, login, logout

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
        context = {
        }
        return render(request, self.template_name, context)


# Class to handle SIGN UP FORM DATA
class SignupData(FormView):
    form_class = SignupForm
    template_name = 'auth/signup.html'

    def post(self, request):
        form_data = SignupForm(request.POST)

        # Check for the duplicate key
        if self.validateDuplicateKey(request.POST.get('signup_email')):

            # Check whether data entered in the form is valid or not
            if form_data.is_valid():

                # Check for PASSWORD == CONFIRM_PASSWORD
                if self.validatePassword(request.POST.get('signup_password'), request.POST.get('signup_confirm_password')):
                    addressObj = UserAddress()
                    addressObj.house = request.POST.get('signup_street')
                    addressObj.landmark = request.POST.get('signup_additional')
                    addressObj.town = request.POST.get('signup_town')
                    addressObj.country = request.POST.get('signup_zip')
                    addressObj.zipcode = request.POST.get('signup_country')

                    userObj = CustomUserAuthentication()
                    userObj.first_name = request.POST.get('signup_first_name')
                    userObj.last_name = request.POST.get('signup_last_name')
                    userObj.email = request.POST.get('signup_email')
                    userObj.country_code = request.POST.get('signup_code')
                    userObj.phone_number = request.POST.get('signup_phone')
                    userObj.is_active = True
                    userObj.is_staff = False
                    userObj.is_superuser = False
                    userObj.address_id = addressObj
                    userObj.set_password(request.POST.get('signup_password'))

                    addressObj.save()
                    userObj.save()

                    user = authenticate(
                        self.request, email=request.POST['signup_email'], password=request.POST['signup_password'])
                    # if user is not None:
                    login(request, user)

                    uname = request.user.first_name + " " + request.user.last_name

                    context = {
                        "showModel" : "true",
                        "message" : "You are successfully sign up! Now, you can manage your account from the profile page.",
                        "username" : uname
                    }
                    return redirect('index_after_signup')
                    return render(request, 'index/index.html', context)

                else:
                    context = {
                        "error": "true",
                        "message": {"not match": "Password and confirm password must be same!"}
                    }

            else:
                context = {
                    "error": "true",
                    "message": form_data.errors
                }
        else:
            context = {
                "error": "true",
                "message": {"Duplicate key": "Can not create more than one account using same email!"}
            }

        return render(request, self.template_name, context)

    # Method to match password with confirm password
    def validatePassword(self, password, confirmPassword):
        if password == confirmPassword:
            return True
        else:
            return False

    # Method to ensure that cannot create more than one account using same email
    def validateDuplicateKey(self, email):
        if len(CustomUserAuthentication.objects.all().filter(email=email)) == 0:
            return True
        else:
            return False

# Class to handele LOGIN FORM DATA


class LoginData(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def post(self, request):
        form_data = LoginForm(request.POST)

        # Check wether form data is valid or not
        if form_data.is_valid():
            user = authenticate(self.request, email=request.POST['login_email'], password=request.POST['login_password'])

            if user is not None:
                login(request, user)
                
                uname = request.user.first_name + ' ' +request.user.last_name

                context = {
                    "showModel" : "true",
                    "message" : "Successfully logged in!",
                    "username" : uname
                }

                return redirect('index_after_login')
            
            else:
                context = {
                "error": "true",
                "message": {"user not found" : "Enter valid e-mail and password."}
            }

            

        else:
            context = {
                "error": "true",
                "message": form_data.errors
            }

            return render(request, self.template_name, context)


# Class to preform LOGOUT operation

# request.POST.get('signup_first_name)
# form_data.errors


# class LoginForm(FormView):
#     template_name = "login.html"
#     form_class = login_user

#     def get(self , request):
#         return render(request , self.template_name)

#     def post(self , request):
#         form = login_user(request.POST)
#         if form.is_valid():

#             user = authenticate(self.request , email = request.POST['login_email'] , password=request.POST['login_password'])

#             if user is not None:
#                 login(request , user)
#                 return render(request , 'index.html')
#             else:
#                 contex = {
#                     'login_error':True,
#                     'login_email':request.POST['login_email']
#                 }
#                 return render(request , 'login.html' , contex)


# from django.shortcuts import render
# from django.views.generic import FormView
# from django.contrib.auth import logout

class Logout(FormView):
    template_name = 'index/index.html'

    def get(self , request):
        logout(request)
        return render(request , self.template_name)
