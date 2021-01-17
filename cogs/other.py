import discord
from discord.ext import commands
import random

#Creating the class and initialising to allow commands to be active
class other(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.latency

    #General other/"fun" commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")


    @commands.command(aliases = ["penissize", "PenisSize"])
    async def penisSize(self, ctx):
        penis_size = "=" * random.randint(0, 15)
        name = ctx.author.name
        await ctx.send(f"{name}\'s penis: 8{penis_size}D")


    @commands.command(aliases = ["dm"])
    async def DM(self, ctx, user: discord.User, *message):
        if message:
            await user.send(" ".join(message))
        else:
            await ctx.send(f"Please specify the messages you want to send to {user}")


    @commands.command(aliases = ["rickroll", "RickRoll"])
    async def rickRoll(self, ctx):
        for member in ctx.guild.members:
            await member.send("https://tenor.com/bjCoL.gif")

    #Overriding help command
    @commands.command(aliases = ["HELP", "Help"])
    async def help(self, ctx):
        await ctx.send("```\nMultiline\nhelp\ncommand```")        

def setup(client):
    client.add_cog(other(client))
