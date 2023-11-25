from rest_framework import serializers
from ..models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'date_joined', 'is_active',
                  'is_staff')
        read_only_fields = ('id', 'date_joined', 'is_active', 'is_staff')
