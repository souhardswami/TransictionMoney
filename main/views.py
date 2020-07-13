from django.shortcuts import render,redirect


from django.db.models import Q

from django.http import HttpResponse

from .models import User,Transiction




def home(request):

    

    return render(request,'home.html')


    
def signin(request):
    if(request.method=='POST'):
        name=request.POST['nam']
        pas=request.POST['pas']
        new_user=User.objects.create(name=name,pas=pas)
        new_user.save()
        print(name+pas)
        return redirect("/main/home/")

    
    

    return render(request, 'signin.html')
    
def login(request):
    if(request.method=='POST'):
        name=request.POST['nam']
        pas=request.POST['pas']
        
        user=User.objects.get(name=name,pas=pas)
        idd=user.id
        
        return redirect("/main/user/"+str(idd))
    
    

    return render(request, 'login.html', {'content':{}})





def moneytransfer(request):

    if(request.method=='POST'):
        to=request.POST['to']
        amount=request.POST['amount']
        user=request.POST['user']
        
        
        
        

        amount=int(amount)
        


        reciever=User.objects.get(name=to)
        
        reciever.accoun_balanch+=amount
        
        reciever.save()
        

        
        sender=User.objects.get(id=int(user))
        
        sender.accoun_balanch-=amount
        
        sender.save()
        
        new_transiction=Transiction.objects.create(to=reciever,fromm=sender,amount=amount)
        
        new_transiction.save()


        
        return redirect("/main/user/"+str(user))


    
    

    



def user(request,num):
    print(num)
    
    

    
    user=User.objects.get(id=num)
    history=Transiction.objects.filter(Q(to=user)|Q(fromm=user))

    
    
    print(history)

    content={

        'history':history,
        'user':user
    }

    
    

    

    return render(request, 'user.html',{'content':content})



def createmoney(request):

    if(request.method=='POST'):
        
        money=request.POST['money']
        user=request.POST['user']
        
        
        
        

        money=int(money)
        


        activeuser=User.objects.get(id=user)
        
        activeuser.accoun_balanch+=money
        
        activeuser.save()
        

        
        print("fine")


        
        return redirect("/main/user/"+str(user))

    