from django.contrib import admin

# Register your models here.



from django.contrib import admin

from .models import User,Transiction,MoneyType

# Register your models here.


admin.site.register(User)
admin.site.register(Transiction)
admin.site.register(MoneyType)