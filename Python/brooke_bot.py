import discord
from bingchat import BingChat

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(username + " said " + user_message.lower() + " in " + channel)

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        print(type(message.channel))
        async for last_message in message.channel.history(limit=1):
            if "brooke" in last_message.content:
                await message.channel.send(f'Stop talking about your undying L O V E for Brooke {last_message.author.name}')
            #print(f'Last message in {message.channel.name} sent by {last_message.author.name}:\n' + last_message.content)

client.run('MTE5Njk2MzgzOTk0NjgwNTM4OQ.GMmuu5.l1LAntT67XIYcoxCAWWs-12RfXO5pIiB3Z17oU')
