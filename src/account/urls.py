from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.UserLogin.as_view(), name="user-login"),
    path('logout', views.UserLogout.as_view(), name="user-logout"),
]