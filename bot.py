# Python Discord Bot
import os
import discord
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file
TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise ValueError("No token provided. Please set the DISCORD_TOKEN env variable in '.env' file.")

intents = discord.Intents.default()
intents.message_content = True # Enable message content intents
intents.guilds = True # Enable guild intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)