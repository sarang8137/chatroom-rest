from rest_framework import serializers
from django.contrib.auth.models import User
from room.models import Room,Message



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

class ChatSer(serializers.ModelSerializer):
    # room_id=RoomSer()
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Message
        fields='__all__'
      
