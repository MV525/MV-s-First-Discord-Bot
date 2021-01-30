import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import keep_alive
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents, help_command=None)

@client.event
async def on_ready():
    change_status.start()
    print(f"Logged in as {client.user.name} - {client.user.id}")

status_list = cycle(["MV's bot is the best bot", "MV's bot is the worst bot"])
#Background task:
@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity = discord.Activity.name(next(status_list)))

#Loads in all the required cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

keep_alive.keep_alive() #Keeping bot alive
client.run("")
