# yourapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom, ChatMessage
from datetime import datetime
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Fetch the chat room, if it doesn't exist, create it
        room, created = await database_sync_to_async(ChatRoom.objects.get_or_create)(name=self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Send previous messages to the user
        previous_messages = await database_sync_to_async(self.get_previous_messages)(room)

        # Send previous messages
        for message in previous_messages:
            await self.send(text_data=json.dumps({
                'message': message.message,
                'user': message.user,
                'timestamp': message.timestamp.isoformat()
            }))

            


            

        await self.accept()

    def get_previous_messages(self, room):
        # Fetch the last 10 messages from the database for the given room
        return room.messages.all().order_by('timestamp')[:10]

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['user']  # Assuming the message includes the user's name or ID

    # Save the message to the database
        room = await database_sync_to_async(ChatRoom.objects.get)(name=self.room_name)
        chat_message = ChatMessage.objects.create(room=room, user=user, message=message)

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
                'timestamp': chat_message.timestamp.isoformat()
            }
        )

        async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'timestamp': timestamp
        }))




    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

   