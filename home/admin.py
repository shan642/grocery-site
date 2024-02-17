from django.contrib import admin

from .models import user,product,cart
admin.site.register(user)
admin.site.register(product)
admin.site.register(cart)