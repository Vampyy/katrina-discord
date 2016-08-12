from api.command import Command

class ShutdownCommand(Command):

    client = None

    def __init__(self, client):
        super().__init__('Shutdown the bot', '', ['stop', 'shutdown'], ['owner', 'grandmasters'])
        self.client = client
        pass

    async def onCommand(self, message, args):
        await self.client.send_message(message.channel, 'Shutting down, goodbye.')
        print('Forced shutdown initated')
        await self.client.logout()
        pass
