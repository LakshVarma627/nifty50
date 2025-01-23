import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import AlertRule

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'alerts'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        alert_id = data.get('alert_id')
        if alert_id:
            alert_rule = await self.get_alert_rule(alert_id)
            if alert_rule:
                await self.send_alert(alert_rule)

    async def send_alert(self, alert_rule):
        await self.send(text_data=json.dumps({
            'alert_id': alert_rule.id,
            'name': alert_rule.name,
            'condition': alert_rule.condition,
        }))

    @database_sync_to_async
    def get_alert_rule(self, alert_id):
        try:
            return AlertRule.objects.get(id=alert_id)
        except AlertRule.DoesNotExist:
            return None
