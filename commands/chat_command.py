from api.command import Command
from cleverbot import Cleverbot


class ChatCommand(Command):

    client = None
    cb = None

    def __init__(self, client):
        super().__init__('Chat with katrina', '[message]', ['c', 'chat'], [])
        self.client = client
        self.cb = Cleverbot()
        pass

    async def onCommand(self, message, args):
        response = self.cb.ask(" ".join(args))
        fmt = '{0.mention} {1}'
        await self.client.send_typing(message.channel)
        await self.client.send_message(message.channel, fmt.format(message.author, response))
