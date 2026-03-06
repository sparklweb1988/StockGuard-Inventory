from django.contrib import admin
from . models import User,Product,Batch,Customer,Order,OrderItem


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Batch)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

