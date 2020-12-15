from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, auth


from django.db.models import Q

from django.http import HttpResponse

# from .models import User,Transiction,MoneyType
# from .models import User
from django.db.models import Count,Sum




def home(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        auth.login(request,user)


        return redirect('/signup')


        return redirect('/main')
    print("jjjjj")
    return render(request,'registration/login.html')


# @login_required
def signup(request):

    if(request.method=='POST'):

        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']

        # newUser = User(firstName=firstName,lastName=lastName,mob=mobile,pas=password,email=email) 
        newUser = User.objects.create_user(username=firstName,password=password,email=email) 
        newUser.save()

        return redirect('/home')
    
    return render(request,'signup.html')



@login_required
def main(request):
    # print(user.get_username)
    print("main")
    return render(request,'main.html')

@login_required
def logout(request):

    auth.logout(request)
    return redirect('/home')



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