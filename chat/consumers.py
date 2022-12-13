# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import datetime
from accounts.models import User
from .models import Room, Message
from channels.db import database_sync_to_async
import asyncio

x = datetime.datetime.now()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room"]
        self.room_group_name = "chat_%s" % self.room_name
        print(self.room_name,'room_name')
        print(self.room_group_name,'group_name')

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self):
        # Leave room group
        print(self)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data,'9999999999999999')
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message,
                'username':username,
                'room':room,
            }
        )
    # send message from room group
    async def chat_message(self, event):
        print(event,'00000000000000000000000000')
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message': message,
            'username':username,
            'room':room,
        }))

    @database_sync_to_async
    def save_message(self, username, room, message):
        if '입장하였습니다' in message:
            pass
        else:
            user = User.objects.get(username=username)
            print(user)
            Message.objects.create(user=user, room=room, content=message)