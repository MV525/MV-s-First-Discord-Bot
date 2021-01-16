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

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
