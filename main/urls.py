from django.urls import path

from . import views

urlpatterns = [

    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout,name="logout"),
    path("main/",views.main,name="main"),
    path("pay/",views.pay,name="pay"),
    path("person/",views.person,name="person"),
    path("wallet/",views.wallet,name="wallet"),
    path("history/",views.history,name="history"),
    # path("user/<int:num>",views.user,name="user"),
    # path("moneytransfer",views.moneytransfer,name="moneytransfer"),
    # path("createmoney",views.createmoney,name="createmoney"),


]