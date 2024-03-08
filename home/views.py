from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator


class SignUpView(CreateView):
    template_name = "home/signup.html"
    form_class = UserCreationForm
    success_url ="/smart/notes"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("notes.list")
        return super().get(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = "home/login.html"


class CustomLogoutView(LogoutView):
    template_name = "home/logout.html"


class HomePageView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "home/authorized.html"
    login_url = "/admin"

