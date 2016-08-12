from api.command import Command
from cleverbot import Cleverbot

class BotChatCommand(Command):

    client = None
    cb1 = None
    cb2 = None
    toggled = None

    def __init__(self, client):
        super().__init__('Let katrina talk with herself', '[start/stop]', ['bc', 'botchat'], ['owner', 'grandmasters'])
        self.cb1 = Cleverbot()
        self.cb2 = Cleverbot()
        self.client = client;
        pass

    async def onCommand(self, message, args):
        if len(args) < 1:
            fmt = '{0.mention} please provide the correct arguments'
            await self.client.send_message(message.channel, fmt.format(message.author))
            return

        if args[0] == 'start':
            self.toggled = True
            await self.client.send_message(message.channel, 'Started')

        if args[0] == 'stop':
            self.toggled = False

        answer = self.cb2.ask('hey')
        await self.client.send_message(message.channel, '2: ' + answer)

        while self.toggled:
            answer = self.cb1.ask(answer)
            await self.client.send_message(message.channel, '1: ' + answer)
            answer = self.cb2.ask(answer)
            await self.client.send_message(message.channel, '2: ' + answer)

            if not self.toggled:
                await self.client.send_message(message.channel, 'Stopped')
                break
