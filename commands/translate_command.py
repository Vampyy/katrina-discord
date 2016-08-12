from api.command import Command
from translate import Translator

class TranslateCommand(Command):

    client = None

    def __init__(self, client):
        super().__init__('Translate text to any language', '[2 letter ISO] [message]', ['translate', 'trans'], [])
        self.client = client
        pass

    async def onCommand(self, message, args):
        if len(args) < 2:
            fmt = '{0.mention} please provide the correct arguments'
            await self.client.send_message(message.channel, fmt.format(message.author))
            return
        text = " ".join(args[1:])
        lang = args[0]
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        await self.client.send_message(message.channel, translation)
