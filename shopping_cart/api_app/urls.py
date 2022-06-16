from django.urls import include, path
from .views import CartItemViews
from .views import ContactView
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView
from .views import authenticate_user


urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('contacts/', ContactView.as_view()),
    path('contacts/<int:id>', ContactView.as_view()),
    path('users/create', CreateUserAPIView.as_view()),
    path('users/update', UserRetrieveUpdateAPIView.as_view()),
    path('users/login', authenticate_user),
]