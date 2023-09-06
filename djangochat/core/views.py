from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions

from room.consumers import ChatConsumer
from room.models import Message
# Create your views here.

class SignUp(ViewSet):
    def create(self,request,*args,**kwargs):
        ser=SignUpSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'User Created'})
        return Response(data=ser.errors)
    
class ChatView(ModelViewSet):
    serializer_class=RoomSer
    queryset=Room.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self, request):
        ser=RoomSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Room Created'})
        return Response(data=ser.errors)
    def get_queryset(self):
        return Room.objects.filter(user=self.request.user)

class RoomView(ViewSet):
    serializer_class=ChatConsumer
    queryset=Message.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self, request):
        ChatConsumer(data=request.data)
        return Response({'msg':'Chat Created'})

class RoomAll(ModelViewSet):
    serializer_class=RoomSer
    queryset=Room.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
