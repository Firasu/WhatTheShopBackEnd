from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Expert, Item, Order
from rest_framework_jwt.settings import api_settings

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data["token"] = token
        return validated_data

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name','description','price','photo']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ExpertListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Expert
        fields = '__all__'

    def get_items(self, obj):
        items = Item.objects.filter(expert=obj)
        return ItemListSerializer(items, many=True).data
