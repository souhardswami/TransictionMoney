from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=10)
    pas=models.CharField(max_length=10)
    accoun_balanch=models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Transiction(models.Model):

    to = models.ForeignKey(User, related_name='RECIEVER',on_delete=models.CASCADE)
    fromm = models.ForeignKey(User, related_name='SENDER',on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField(default=0)

    def __str__(self):
        return str(self.fromm)+">>>>"+str(self.to)