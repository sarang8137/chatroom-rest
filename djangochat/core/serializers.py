from rest_framework import serializers
from django.contrib.auth.models import User
from room.models import Room



class SignUpSer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class RoomSer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'