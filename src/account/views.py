from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView    


class UserLogin(LoginView):
    template_name = 'account/login_view.html'
    next_page = "/"

class UserLogout(LogoutView ):
    template_name = "registration/logged_out.html"
    next_page = "/"
