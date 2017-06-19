import discord
from WowBingo import WowBingo
import config

client = discord.Client()
bingo = WowBingo()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    """ There's a space in the keyword commands to ensure future related commands.
    i.e. ?bingo-save, ?bingo-cone """
    if message.content.startswith('?bingo '):

        msg = 'Hello {0.author.mention}'.format(message)

        if message.author.name == 'LinaeSostra' :
            msg = 'Here\'s your bingo card you trash panda {0.author.mention}'.format(message)
        elif message.author.name == 'Netflixnheal':
            msg = 'Here you go master: '

        await client.send_message(message.channel, msg)
        await client.send_file(message.channel, bingo.generate_board(message.author.name))

    elif message.content.startswith('?about '):
        msg = 'Bingo bot for dank memes...by Dan'
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.auth['token'])