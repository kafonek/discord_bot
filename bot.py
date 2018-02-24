import discord
import asyncio

client = discord.Client()
client.last_pubmsg = None # for debug
client.last_privmsg = None # for debug

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.channel.is_private:
        await privmsg_recv(message)
    else:
        await pubmsg_recv(message)

async def privmsg_recv(message):
    client.last_privmsg = message
    if message.content == 'logout':
        await client.logout()
        
    elif 'bo' in message.content:
        replaced = message.content.replace('bo', '*bro*')
        await client.send_message(message.channel, replaced)
        
async def pubmsg_recv(message):
    client.last_pubmsg = message
    if message.channel.name == 'code_testing':
        if 'bo' in message.content:
            replaced = message.content.replace('bo', '*bro*')
            await client.send_message(message.channel, replaced)
            
        if 'bro' in message.content and message.author.name != client.user.name:
            await client.add_reaction(message, '\N{THUMBS UP SIGN}')
        
    