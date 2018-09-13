from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer, ExpertListSerializer, OrderCreateSerializer, OrderListSerializer
from .models import Expert, Order, OrderItem, Item
from .permissions import IsExpertorStaff
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import redirect


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(expert=self.request.user)

class ExpertListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        expert_list = Expert.objects.all()
        json_expert_list = ExpertListSerializer(expert_list, many=True, context={"request":request}).data
        return Response(json_expert_list)

class OrderCreateView(APIView):
    def post(self, request):
        cart = request.data
        user = request.user
        order = Order.objects.create(user=user)
        for order_item in cart:
            OrderItem.objects.create(
                item = Item.objects.get(id=order_item["id"]),
                quantity = order_item["quantity"],
                order=order
            )
        return JsonResponse({'Message': "Order created","id": order.id})

class OrderListView(APIView):
    permission_classes =[AllowAny]

    def get(self, request, *args, **kwargs):
            orderitem_list = Order.objects.all()
            order_items = OrderListSerializer(orderitem_list, many=True, context={"request":request}).data
            return Response(order_items)
