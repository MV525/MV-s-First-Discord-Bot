import discord
from discord.ext import commands
import os
import random
import asyncio
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents, help_command=None)

#Flask for server
from flask import Flask
from threading import Thread

app = Flask("")

#Returns "MV's bot is active" upon successful activation
@app.route("/")
def main():
  return "MV's bot is active!"

#Hosting bot on port 8000
def run():
  app.run(host="0.0.0.0", port=8000)

#Keeping bot alive
def keep_alive():
  server = Thread(target=run)
  server.start()

keep_alive()

#Loads in all the required cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
