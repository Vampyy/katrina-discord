import discord
import asyncio
import json
import prettytable

from commands.shutdown_command import ShutdownCommand
from commands.prune_command import PruneCommand
from commands.chat_command import ChatCommand
from commands.math_command import MathCommand
from commands.translate_command import TranslateCommand
from commands.eval_command import EvalCommand
from commands.bchat_command import BotChatCommand
from commands.chester_command import ChesterCommand
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer

bot = discord.Client()
config = json.load(open('config.json'))
prefix = '-'
commands = [
    ShutdownCommand(bot),
    PruneCommand(bot),
    ChatCommand(bot),
    BotChatCommand(bot),
    MathCommand(bot),
    TranslateCommand(bot),
    EvalCommand(bot),
    ChesterCommand(bot)
]

chatbot = ChatBot("katrina")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")



@bot.event
async def on_ready():
    print('katrina is logged in')


@bot.event
async def on_member_join(member):
    website = 'http://ptp.github.io'
    fmt = 'Welcome {0.mention} to KBVE.'
    await bot.send_message(member.server, fmt.format(member, website))


@bot.event
async def on_message(message):
    print(message.content)
    if message.content.startswith('<@206231011321708545>'):
        res = chatbot.get_response(message.content.replace('<@206231011321708545>', ''))
        print(res)
        fmt = '{0.mention} {1}'
        reply = fmt.format(message.author, res)
        await bot.send_message(message.channel, reply)
    if message.content.startswith(prefix):
        args = message.content.replace(prefix, '').split(' ')
        for command in commands:
            for name in command.getNames():
                newArgs = args[1:]
                if name == args[0]:
                    if command.getRoles():
                        if message.author.top_role.name.lower() in command.getRoles():
                            await command.onCommand(message, newArgs)
                            break
                        else:
                            await bot.send_message(message.channel,
                                                   'You don\'t have permission for this command')
                    else:
                        await command.onCommand(message, newArgs)
                        break
    if message.content.startswith(prefix + 'help'):
        helpMessage = prettytable.PrettyTable(
            ['Command', 'Aliases', 'Description', 'Usage', 'Required role(s)'])
        for command in commands:
            usage = '{0}{1} {2}'
            helpMessage.add_row([prefix + command.getNames()[:1][0], ", ".join(command.getNames()[1:]), command.getDescription(
            ), usage.format(prefix, command.getNames()[:1][0], command.getUsage()), ",".join(command.getRoles())])
        await bot.send_message(message.channel, '```' + helpMessage.get_string() + '```')
bot.run(config['token'])
