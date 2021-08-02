from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category
from django.core.paginator import Paginator
from django.views import View


class Orders(View):
    def get(self, request):
        return render(request, 'orders/orders.html')
