from django.db import models

# Create your models here.


# class User(models.Model):
#     User=models.CharField(max_length=10,default='')
    
#     mob=models.CharField(max_length=10)
    

#     accoun_balanch=models.IntegerField(default=0)


#     def __str__(self):
#         return self.firstName

from django.contrib.auth.models import User, auth




class CustomUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    
    mob=models.CharField(max_length=10)

    targetuser=models.CharField(max_length=10 ,default='0000000000')
    

    account_balance=models.IntegerField(default=0)


    def __str__(self):
        return self.mob







class MoneyType(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    identity=models.CharField(max_length=10)


    def __str__(self):
        return '--'+str(self.owner)+'--'



class Transiction(models.Model):

    to = models.ForeignKey(User, related_name='RECIEVER',on_delete=models.CASCADE)
    fromm = models.ForeignKey(User, related_name='SENDER',on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField(default=0)
    typeof=models.ForeignKey(MoneyType,related_name='moneytype',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fromm)+">>>>"+str(self.to)




