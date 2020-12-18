from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, auth


from django.db.models import Q

from django.http import HttpResponse

from django.contrib import messages



from .models import CustomUser,Transiction
from django.db.models import Count,Sum



def currentUserBalnce(user):
    
    login_user=CustomUser.objects.filter(user_id=user)[0]

    return login_user.account_balance


def home(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if(user is not None):

            messages.success(request,'succesfully login')
            auth.login(request,user)
            return redirect('/main')
        else:
            messages.error(request,'wrong username/password')
            # return redirect('/')


        # return redirect('/signup')


        
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
        newUser = User.objects.create_user(username=firstName+lastName,password=password,email=email) 
        newUser.save()


        customuser=CustomUser(user=newUser,mob=mobile,account_balance=0)
        customuser.save()
        messages.success(request,'succesfully register')

        return redirect('/')

    
    return render(request,'signup.html')



@login_required
def main(request):
    # print(user.get_username)
    print("main")
    return render(request,'main.html')

@login_required
def logout(request):
    
    messages.info(request,'loged out')
    auth.logout(request)
    return redirect('/')

@login_required
def person(request,targetUser=None):

    if(request.method=='POST' and request.path_info=='/person/'):
        amount=request.POST['amount']
        
        
        amount=int(amount)

        myAccountBalance=currentUserBalnce(request.user)


        targetUser=CustomUser.objects.filter(user_id=request.user)[0].targetuser

        print("yes")
        print(targetUser)
        if(myAccountBalance>=amount):
            print("semd")


            # RECIEVER UPDATE
            targetUser_mobile=CustomUser.objects.filter(user_id=request.user)[0].targetuser
            targetUser=CustomUser.objects.filter(mob=targetUser_mobile)[0]
            targetUser.account_balance+=amount
            targetUser.save()


            # SENDER UPDATE
            login_user=CustomUser.objects.filter(user_id=request.user)[0]
            login_user.account_balance-=amount
            login_user.targetuser=''
            login_user.save()



            # TRANSICTION CREATE

            newTransiction=Transiction(sender=login_user,reciever=targetUser,amount=amount)
            newTransiction.save()
            messages.success(request,str(amount)+' has beed sended')
            

        else:
            print("you have not enought amount to send")
            messages.error(request,'you have not enought amount to send ')

        return redirect('/main')
        


    context={
        'reciever': targetUser.username
    }
    return render(request,'person.html',context)



@login_required
def pay(request):

    if(request.method=='POST'):
        print("hello")
        print(request)

        mobileNumber=request.POST['mobileNumber']

        if(len(mobileNumber)!=10):
            messages.warning(request,'Number is wrong ')
            return render(request,'pay.html')



        targetUser=CustomUser.objects.filter(mob=mobileNumber)
        print(targetUser)
        if(len(targetUser)==0):
            messages.warning(request,'Number is wrong ')
            return render(request,'pay.html')
        targetUser=targetUser[0]
        login_user=CustomUser.objects.filter(user_id=request.user)[0]

        
        # print(login_user)
        # print(targetUser.user.username)
        login_user.targetuser=mobileNumber
        login_user.save()
        
        # return redirect('/person')
        return person(request,targetUser.user)
    messages.info(request,'Enter number ')
    return render(request,'pay.html')



@login_required
def wallet(request):
    print("fine")
    login_user=request.user

    content={
        'accountBalance':currentUserBalnce(login_user)
    }

    return render(request,'wallet.html',content)



@login_required
def history(request):
    print('hist')

    login_user=CustomUser.objects.filter(user_id=request.user)[0]

    myTransiction=Transiction.objects.filter(sender=login_user)

    transictionArr=[]
    for i in myTransiction:

        dic={}
        dic['mobile']=i.reciever.mob
        dic['user']=User.objects.get(pk=i.reciever.user_id).username
        dic['amount']=i.amount
        dic['sender']=True
        st=i.time
        dic['date'] = st.strftime("%Y-%m-%d %H:%M:%S")
        

        transictionArr.append(dic)
    
    
    
    myTransiction=Transiction.objects.filter(reciever=login_user)
    for i in myTransiction:

        dic={}
        dic['mobile']=i.sender.mob
        dic['user']=User.objects.get(pk=i.sender.user_id).username
        dic['amount']=i.amount
        dic['sender']=False
        st=i.time
        dic['date'] = st.strftime("%Y-%m-%d %H:%M:%S")
        

        transictionArr.append(dic)

    print(transictionArr)

    return render(request,'history.html',{'transiction':transictionArr})