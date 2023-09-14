from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions

from room.consumers import ChatConsumer
from room.models import Message
from rest_framework.decorators import action



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

class RoomView(ModelViewSet):
    serializer_class=ChatSer
    queryset=Message.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self, request,*args,**kwargs):
        id=request.data.get('room') 
        print(request.user)
        us=request.data.get('User')        
        room=Room.objects.get(id=id)
        ser=ChatSer(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user,room=room)
            # Message.objects.create()
            return Response({'msg':'Message sent successfully'})
        return Response(data=ser.errors)
    @action(detail=False, methods=['POST'], name='Get Highlight')
    def msgret(self, request, *args, **kwargs):
        id=request.data.get('room')
        rm=Room.objects.get(id=id)
        msg=Message.objects.filter(room=rm)
        dser=ChatSer(msg,many=True)
        return Response(data=dser.data)

class RoomAll(ModelViewSet):
    serializer_class=RoomSer
    queryset=Room.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


