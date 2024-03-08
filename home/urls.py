from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("login", views.CustomLoginView.as_view(), name="login"),
    path("logout", views.CustomLogoutView.as_view(), name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
]

