# Python Discord Bot
import os
import discord
from dotenv import load_dotenv
from mc_helpers import *

# Load environment variables from .env file
load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise ValueError("No token provided." \
                     "Please set the DISCORD_TOKEN env variable in '.env' file.")
GUILD = os.getenv('DISCORD_GUILD')
MC_SERVER = os.getenv('MC_SERVER')
MC_PORT = os.getenv('MC_PORT')

mc_server = MCServer(MC_SERVER, int(MC_PORT))

intents = discord.Intents.default()
intents.message_content = True # Enable message content intents
intents.guilds = True # Enable guild intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return # Ignore messages from the bot itself

    if message.content == '!mc':
        response = mc_server.get_status_message()
        await message.channel.send(response)

client.run(TOKEN)