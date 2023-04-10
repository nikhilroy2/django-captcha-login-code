from django.shortcuts import render

# Create your views here.
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .forms import SignupForm


from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from django.shortcuts import redirect

def Index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Validate the reCAPTCHA response
            recaptcha_response = request.POST.get('g-recaptcha-response')
            captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'dark'}))
            if not captcha.verify(recaptcha_response, request.META.get('REMOTE_ADDR')):
                form.add_error(None, 'Invalid reCAPTCHA. Please try again.')
                return render(request, 'signup.html', {'form': form})
            else:
                # Process the signup request
                return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'app1/index.html', {'form': form})


# def Index(request):
#     return render(request, 'app1/index.html')
    #return render(request, 'index.html')