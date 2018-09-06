from django.urls import path
from .views import UserCreateAPIView, ExpertListAPIView, OrderCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ExpertListAPIView.as_view(), name='list'),
    path('order/', OrderCreateAPIView.as_view(), name='order-create'),
]
