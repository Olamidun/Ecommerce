from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text,DjangoUnicodeDecodeError
from users.utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
# Create your views here.


def register(request):
    if request.method == "POST":
        # data = request.POST
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        full_name = request.POST.get('fullname')
        # try:
        #     if User.objects.get(email=email):
        #         messages.success(request, 'This Email Address already exist!')
        # except Exception:
        #     pass
        if password == password2 and len(password) > 6:
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.first_name = full_name
            user.last_name = full_name
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate your account'
            email_message = render_to_string('users/activate_account.html',
                                             {
                                                 'user': user,
                                                 'domain': current_site.domain,
                                                 'uid': urlsafe_base64_encode(force_bytes(user.id)),
                                                 'token': generate_token.make_token(user)
                                             })

            activation_mail = EmailMessage(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            activation_mail.send()
            messages.success(request, 'Your account has been created successfully,'
                                      ' please check your mail to verify your account!')
            return redirect('users:login')
        elif password != password2:
            messages.success(request, 'Please ensure your passwords are the same.')
            return redirect('users:register')
        elif len(password) <= 6:
            messages.success(request, 'Passwords must have a minimum of 7 characters!')
            return redirect('users:register')
    else:
        return render(request, 'users/register.html')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except Exception:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your Account has been activated successfully")
            return redirect('users:login')
        return render(request, 'users/activate_failed.html', status=401)
