from django.shortcuts import render,redirect


from django.db.models import Q

from django.http import HttpResponse

from .models import User,Transiction,MoneyType
from django.db.models import Count,Sum




def home(request):
    if(request.method=='POST'):
        print("hello")
        print(request)
        return redirect('/main')
    print("jjjjj")
    return render(request,'home.html')



def signup(request):
    print("nn")
    if(request.method=='POST'):
        print("hello")
        print(request)
        return redirect('/home')
    
    return render(request,'signup.html')

def main(request):
    print("main")
    return render(request,'main.html')

def pay(request):

    if(request.method=='POST'):
        print("hello")
        print(request)
        return redirect('/person')

    return render(request,'pay.html')


def person(request):


    return render(request,'person.html')

def login(request):
    print("pass")



    



def user(request,num):
    print("pass")


def wallet(request):
    print("fine")
    return render(request,'wallet.html')


def history(request):
    print('hist')
    return render(request,'history.html')