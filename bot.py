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

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): #checks if command is on cooldown
        message = f"This command is still on cooldown! Please wait {str(error.retry_after)[0]} seconds!"
        await ctx.send(message)

status_list = cycle(["being the best bot", "being the worst bot"])
#Background task:
@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity = discord.Activity(name = next(status_list), type = discord.ActivityType.competing))

#Loads in all the required cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

keep_alive.keep_alive() #Keeping bot alive
key = os.environ["BOT_TOKEN"]
client.run(key)
