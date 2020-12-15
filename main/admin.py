from django.contrib import admin

# Register your models here.



from django.contrib import admin

from .models import Transiction,MoneyType,CustomUser

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Transiction)
admin.site.register(MoneyType)