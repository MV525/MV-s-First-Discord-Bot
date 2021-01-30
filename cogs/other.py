import discord
from discord.ext import commands
import random

#Creating the class and initialising to allow commands to be active
class other(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.latency

    #General other/"fun" commands
    @commands.command(aliases = ["Ping", "PING", "latency"])
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")


    @commands.command(aliases = ["penissize", "PenisSize", "PS", "ps"])
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
        await ctx.send("```\nCommands for moderators:\n!purge / !clear => allows you to clear any number of messages\n!kick => kicks a specified user\n!ban => bans a specified user\n!unban => unbans a specified user and automatically sends an invite link\n\nGeneral/\"fun\" commands:\n!ping => returns ping in ms\n!penisSize => tells you how big your dick is\n!dm => allows you to dm a member in the server\n!rickRoll => rick rolls every member in the guild```")

def setup(client):
    client.add_cog(other(client))
