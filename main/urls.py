from django.urls import path

from . import views

urlpatterns = [
    # path("",views.home,name="home"),
    # path("regi",views.registor,name="registor"),
    path("home/",views.home,name="home"),
    path("signin/",views.signin,name="signin"),
    path("login/",views.login,name="login"),
    path("user/<int:num>",views.user,name="user"),
    path("moneytransfer",views.moneytransfer,name="moneytransfer"),


]