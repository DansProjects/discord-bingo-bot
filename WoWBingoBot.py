import discord
from WowBingo import WowBingo
import config

client = discord.Client()
bingo = WowBingo()

@client.event
async def on_message(message):
    #do not respond to self - causing recursive fail
    if message.author == client.user:
        return

    if message.content.startswith('?bingo'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, '-------------')
        #generate and send image to discord
        await client.send_file(message.channel, bingo.generate_board())
    elif message.content.startswith('?about'):
        msg = 'Bingo bot for dank memes...by Dan'
        await client.send_message(message.channel, msg)
    elif message.content.startswith('?cheats'):
        msg = 'Give Dan gold for hellfire deck upgrade'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.auth['token'])