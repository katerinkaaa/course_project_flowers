from django.contrib import admin
from .models import *
from django.contrib import admin


admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(Orders)
admin.site.register(PaymentType)
admin.site.register(Delivery)
admin.site.register(OrderStatus)
admin.site.register(Client)
admin.site.register(FlowerList)
admin.site.register(Flower)
admin.site.register(Category)


admin.site.site_header = 'Флористический магазин "ArtFlowers"'
admin.site.site_title = 'Флористический магазин "ArtFlowers"'
