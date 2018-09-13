from django.contrib import admin
from .models import Expert, Item, Order, OrderItem

admin.site.register(Expert)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
