from django.urls import path
from .views import home, login, signup

urlpatterns = [
    path('store/', home.store, name="store"),
    path('orders/', home.orders, name="order"),
    path('signup/', signup.Signup.as_view(), name="signup"),
    path('login/', login.Login.as_view(), name="login"),
    # path('product/',views.product, name="product")
]
