from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category
from django.core.paginator import Paginator


# Create your views here.
def store(request):
    # products=None
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
    print('you are:',request.session.get('email'))
    return render(request, 'store/store.html', context)


# def product(request):

#     return render(request, 'store/product.html')

def orders(request):
    return render(request, 'orders/orders.html')





