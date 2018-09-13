from django.urls import path
from .views import UserCreateAPIView, ExpertListAPIView, OrderCreateView, OrderListView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ExpertListAPIView.as_view(), name='list'),
    path('order/', OrderCreateView.as_view(), name='order-create'),
    path('orderlist/', OrderListView.as_view(), name='order-list'),
]
