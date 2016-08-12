from api.command import Command
from py_expression_eval import Parser

class MathCommand(Command):

    client = None

    def __init__(self, client):
        super().__init__('Evaluate mathematical expressions', '[expression]', ['math'], [])
        self.client = client
        pass

    async def onCommand(self, message, args):
        if len(args) < 1:
            fmt = '{0.mention} please provide a mathematical expression'
            await self.client.send_message(message.channel, fmt.format(message.author))
            return
        parser = Parser()
        expr = " ".join(args)
        parsed = None
        try:
            parsed = str(parser.parse(expr).evaluate({}))
            await self.client.send_message(message.channel, parsed)
        except:
            await self.client.send_message(message.channel, message.author.mention + ' An error occurred while trying to evaluate your esexpression')
