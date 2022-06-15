from django.urls import path
from .views import CartItemViews
from .views import ContactView

urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('contacts/', ContactView.as_view()),
    path('contacts/<int:id>', ContactView.as_view())
]