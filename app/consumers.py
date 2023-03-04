import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync
from time import sleep


class FileShareConsumer(AsyncWebsocketConsumer):
    count_root =0
    async def connect(self):
        print("==================")
        await self.accept()
         
        # ChatConsumer.count = ChatConsumer.count +1
        print("id...............")
        room = self.scope['url_route']['kwargs']['id']
        self.room = room
         
        await self.channel_layer.group_add(room, self.channel_name)
    
    async def disconnect(self, close_code):
         
        await self.disconnect()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
                self.room,
                {
                    'type':'send.text',
                    'msg':text_data
                }
            )
    async def send_text(self,event):
        print(event['msg'])
        await  self.send(event['msg'])