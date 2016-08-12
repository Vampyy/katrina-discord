from api.command import Command

class PruneCommand(Command):

    client = None

    def __init__(self, client):
        super().__init__('Prune a certain amount of messages', '[amount]', ['prune'], ['owner', 'admin', 'grandmasters'])
        self.client = client
        pass

    async def onCommand(self, message, args):
        pruneAmount = None
        if len(args) > 0:
            pruneAmount = int(args[0])
        else:
            pruneAmount = 50
        pruned = await self.client.purge_from(message.channel, limit=pruneAmount, check=None)
        await self.client.send_message(message.channel, 'Deleted {} message(s)'.format(len(pruned)))
