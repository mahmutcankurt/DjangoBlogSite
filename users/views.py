from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm, LoginForm
from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from .models import Profile
from django.urls import reverse


def signupView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('category:index'))
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
            })
            auth.login(request, user)
            profile = Profile()
            profile.user = user
            user.email_user(subject, message)
            return HttpResponseRedirect(reverse('index.html'))
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'users/account_activation_email.html')


def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('category:index'))

    next = request.GET.get('next', None)

    form = LoginForm(request.POST)
    if form.is_valid():
        next = (request.POST.get('nextt', None))
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user:
            #user = User.objects.get(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            login(request, user)
            if next:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect(reverse('category:index'))
        else:
            error_message = 'Username or Password incorrect ! '
            return render(request, 'users/user_login.html', context={'form': form, 'error_message': error_message})

    return render(request, 'users/user_login.html', context={'form': form, 'next':next})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
