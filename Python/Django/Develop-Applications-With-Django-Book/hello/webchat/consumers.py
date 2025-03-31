import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class WebchatConsumer(AsyncJsonWebsocketConsumer):
    async def invia_messaggio(self, event):
        messaggio = event['messaggio']
        username = event['username']
        await self.send(text_data=json.dumps(
            {"messaggio": messaggio,
             'username': username}
        ))

    async def receive(self, text_data):
        data = json.loads(text_data)
        messaggio = data['messaggio']
        username = data['username']
        await self.channel_layer.group_send(
            self.nome_stanza, {
                "type": "invia_messaggio",
                "messaggio": messaggio,
                "username": username,
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.nome_stanza, self.channel_name)

    async def connect(self):
        self.nome_stanza = "webchat"
        await self.channel_layer.group_add(self.nome_stanza, self.channel_name)
        await self.accept()

