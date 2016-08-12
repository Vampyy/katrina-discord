from api.command import Command
from io import StringIO
import re
import sys
import js2py

class EvalCommand(Command):

    client = None

    def __init__(self, client):
        super().__init__('Evaluate code in selected language', '[langauge] [code]', ['eval', 'code'], ['owner', 'grandmasters'])
        self.client = client
        pass

    async def onCommand(self, message, args):
        print(len(message.content.strip().split('\n')))
        if len(args) < 2:
            fmt = '{0.mention} please provide the correct arguments'
            await self.client.send_message(message.channel, fmt.format(message.author))
            return

        lang = args[0].split('\n')[:1][0].lower()
        code = ''
        multiline = False

        if len(message.content.strip().split('\n')) > 1:
            unparsed = '\n'.join(message.content.strip().split('\n')[2:])
            code = unparsed.replace('```', '')
            multiline = True
        else:
            print(message.content.split(' ')[2:])
            code = ' '.join(message.content.split(' ')[2:])

            print(code)

        if lang == 'python' or lang == 'py':
            if not multiline:
                evaluated = eval(code)
                fmt = '```{0}```'
                await self.client.send_message(message.channel, fmt.format(evaluated))
                return
            buff = StringIO()
            sys.stdout = buff
            exec(code)
            sys.stdout = sys.__stdout__
            fmt = '```{0}```'
            await self.client.send_message(message.channel, fmt.format(buff.getvalue()))
        elif lang == 'javascript' or lang == 'js':
            evaluated = str(js2py.eval_js(code.replace('document.write', 'return ')))
            fmt = '```{0}```'
            await self.client.send_message(message.channel, fmt.format(evaluated))
        else:
            fmt = '{0.mention} please select an available language: Python'
            await self.client.send_message(message.channel, fmt.format(message.author))
