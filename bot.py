import discord
from discord.ext import commands
import os
import keep_alive
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents, help_command=None)

keep_alive.keep_alive() #Keeping bot alive

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} - {bot.user.id}")
#Loads in all the required cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
