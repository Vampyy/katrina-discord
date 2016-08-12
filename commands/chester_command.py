from api.command import Command
import requests


class ChesterCommand(Command):

    client = None

    def __init__(self, client):
        super().__init__('Talk to chester', '[message]', ['cc', 'chester'], [])
        self.client = client
        pass

    async def onCommand(self, message, args):
        payload = {'q': " ".join(args)}
        response = requests.get('https://chester.paulb.gd/api', params=payload)
        res = response.json()['response']
        fmt = '{0.mention} {1}'
        reply = fmt.format(message.author, res)
        await self.client.send_message(message.channel, reply)
