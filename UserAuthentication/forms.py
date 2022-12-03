from django import forms
import re

# Method to validate PHONE NUMBER
def validatePhoneNumber(number):
    if len(number) > 10:
        raise forms.ValidationError("Mobile Number Should 10 digit")

# Method to validate ZIPCODE
def validateZipcode(zipcode):
    pattern = "^[1-9]{1}[0-9]{2}\\s{0, 1}[0-9]{3}$"
    if not (re.match(pattern, zipcode)):
        raise forms.ValidationError("Please enter valide zip code!")

# Method to validate TOWN name
def validateTown(town):
    if not any(chr.is_digit() for chr in town):
        raise forms.ValidationError("Town name can not contain digits!")

# Method to validate COUNTRY name
def validateCountry(country):
    if not any(chr.is_digit() for chr in country):
        raise forms.ValidationError("Country name can not contain digits!")

# Form class to make SIGN UP form
class SignupForm(forms.Form):
    # Required fields
    signup_first_name = forms.CharField(error_messages={'required' : 'First Name is required!'}, max_length=20 , required=True)
    signup_last_name = forms.CharField(error_messages={'required' : 'Lase Name is required!'}, max_length=20 , required=True)
    signup_email = forms.EmailField(error_messages={'required' : 'E-mail is required!'}, max_length=100, required=True)
    signup_code = forms.CharField(error_messages={'required' : 'Country-Code is required!'}, max_length=5, required=True)
    signup_phone = forms.CharField(error_messages={'required' : 'Phone Number is required!'}, validators=[validatePhoneNumber], max_length=15, required=True)
    signup_password = forms.CharField(error_messages={'required' : 'Password is required!'}, max_length=40, required=True)
    signup_confirm_password = forms.CharField(error_messages={'required' : 'Confirm Password is required!'}, max_length=40, required=True)

    # Optional fields
    signup_street = forms.CharField(max_length=50, required=False)
    signup_additional = forms.CharField(max_length=50, required=False)
    signup_town = forms.CharField(validators=[validateTown], max_length=50, required=False)
    signup_country = forms.CharField(validators=[validateCountry], max_length=50, required=False)
    signup_zip = forms.CharField(validators=[validateZipcode], max_length=10, required=False)
    

# Form class to make LOGIN form
class LoginForm(forms.Form):
    # Required fields
    login_email = forms.CharField(error_messages={'required' : 'E-mail is required to Sign in!'}, max_length=100, required=True)
    login_password = forms.CharField(error_messages={'required' : 'Password is required to Sign in!'}, max_length=40, required=True)