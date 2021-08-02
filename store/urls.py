from django.urls import path
from .views import home, orders, login, signup
from .views.login import logout

urlpatterns = [
    path('store/', home.Store.as_view(), name="store"),
    path('orders/', orders.Orders.as_view(), name="order"),
    path('signup/', signup.Signup.as_view(), name="signup"),
    path('login/', login.Login.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    # path('product/',views.product, name="product")
]
