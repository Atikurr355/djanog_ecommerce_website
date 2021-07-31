from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer


# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display=['lname', 'email']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer,CustomerAdmin)
