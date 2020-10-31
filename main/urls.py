from django.urls import path

from . import views

urlpatterns = [

    path("home/",views.home,name="home"),
    # path("signin/",views.signin,name="signin"),
    # path("login/",views.login,name="login"),
    # path("user/<int:num>",views.user,name="user"),
    # path("moneytransfer",views.moneytransfer,name="moneytransfer"),
    # path("createmoney",views.createmoney,name="createmoney"),


]