from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, ExpertListSerializer, OrderCreateSerializer
from .models import Expert
from .permissions import IsExpertorStaff
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(expert=self.request.user)

class ExpertListAPIView(ListAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertListSerializer
    permission_classes = [AllowAny]

class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
