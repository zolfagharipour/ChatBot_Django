import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connected to chatbot!"}))

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_message = data.get("message", "")

        bot_response = self.get_response(user_message)

        await self.send(text_data=json.dumps({"response": bot_response}))

    async def disconnect(self, close_code):
        print("WebSocket disconnected")

    def get_response(self, message):
        responses = {
            "hello": "Hello Stranger, I wish you are doing fine today.",
            "bye": "Goodbye! Have a nice day!",
            "help": "My consciousness is very limited, I only can understand hello and bye :(",
        }
        return responses.get(message.lower(), "I don't understand that.")
