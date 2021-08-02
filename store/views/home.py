from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.core.paginator import Paginator
from django.views import View


class Store(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        result = request.session['cart'] = cart

        print('cart: ', result)
        return redirect('store')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categoris()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)

        else:
            products = Product.get_all_products()

        paginator = Paginator(products, 8, orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'categories': categories,
        }
        print('you are:', request.session.get('email'))
        return render(request, 'store/store.html', context)

# def product(request):

#     return render(request, 'store/product.html')
