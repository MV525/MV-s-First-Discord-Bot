import discord
from discord.ext import commands
from discord.client import Client
from discord import message
import os
import random
import asyncio
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def main():
  return "MV's bot is active!"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

keep_alive()

background_task = discord.Client()

async def my_background_task():
    await background_task.wait_until_ready()
    counter = 0
    channel = discord.Object(id="channel_id_here")
    while not background_task.is_closed:
        counter += 1
        await background_task.send_message(channel, counter)
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print("Logged in as")
    print(background_task.user.name)
    print(background_task.user.id)
    print("------")

background_task.loop.create_task(my_background_task())


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
