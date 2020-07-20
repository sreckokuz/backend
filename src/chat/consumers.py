import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        print(other_user)
        print(me)
        thread_obj = await self.get_thread(me, other_user)
        print(thread_obj)
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("receive", event)
        front_text = event.get('text', None)
        if front_text is not None:
            dict_loaded_data = json.loads(front_text)
            msg = dict_loaded_data.get('message')
            print(msg)
            me = self.scope['user']
            username = 'default'
            if me.is_authenticated:
                username = me.username
            myResponse = {
                "message":  msg,
                "username": username
            }
            await self.send({
                "type": "websocket.send",
                "text": json.dumps(myResponse)
            })

    async def websocket_disconnect(self, event):
        print("disconect", event)

    @database_sync_to_async
    def get_thread(self, user, other_username):
        return Thread.objects.get_or_new(user, other_username)[0]
