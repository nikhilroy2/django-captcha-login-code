from django import forms
from captcha.fields import ReCaptchaField

class SignupForm(forms.Form):
    # Add your form fields here
    captcha = ReCaptchaField()