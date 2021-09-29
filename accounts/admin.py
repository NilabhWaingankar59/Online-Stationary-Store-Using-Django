from django.contrib import admin
from .models import category, customer,products

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('contact', 'address', 'pin',
                    'district')

admin.site.register(customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stock',
                    'price')


admin.site.register(products, ProductAdmin)


class categoryAdmin(admin.ModelAdmin):
    list_display = ('catid', 'name')


admin.site.register(category, categoryAdmin)
