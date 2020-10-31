from django.shortcuts import render,redirect


from django.db.models import Q

from django.http import HttpResponse

from .models import User,Transiction,MoneyType
from django.db.models import Count,Sum




def home(request):
    print("jjjjj")
    return render(request,'home.html')



def signin(request):
    print("pass")

def login(request):
    print("pass")


def moneytransfer(request):

    print("pass")



def user(request,num):
    print("pass")

