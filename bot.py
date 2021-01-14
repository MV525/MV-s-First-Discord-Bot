import discord
from discord.ext import commands
import os
import random
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready(self):
    print("MV's bot is active!")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
