from django.contrib import admin
from store.models import CakeVarient,Cake,Weight,Flavour,Shape,Occassion,OrderItems,Order,Tag

# Register your models here.
admin.site.register(Cake)
admin.site.register(Weight)
admin.site.register(Flavour)
admin.site.register(Shape)
admin.site.register(Occassion)
admin.site.register(CakeVarient)
admin.site.register(OrderItems)
admin.site.register(Order)
admin.site.register(Tag)