import discord
from discord.ext import commands
import random
import requests

#Creating the class and initialising to allow commands to be active
class other(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.latency

    #General other/"fun" commands
    @commands.command(aliases = ["Ping", "PING", "latency", "Latency"])
    async def ping(self, ctx):
        await ctx.send(f"{ctx.author.name}, your latency is: {round(self.client.latency * 1000)}ms")


    @commands.command(aliases = ["penissize", "PenisSize", "PS", "ps"])
    async def penisSize(self, ctx):
        await ctx.send(f"{ctx.author.name}\'s penis: 8{'=' * random.randint(0, 15)}D")


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
        await ctx.send("```\nCommands for moderators:\n!purge / !clear => Allows you to clear any number of messages\n!kick => Kicks a specified user\n!ban => Bans a specified user\n!unban => Unbans a specified user\n\nGeneral/\"fun\" commands:\n!ping => Returns ping in ms\n!penisSize => Tells you how big your dick is\n!dm => Allows you to dm a member in the server\n!rickRoll => Rick rolls every member in the guild\n!fox => Displays a random fox!\n!cat => Displays a random cat!\n!advice => Gives you a piece of advice :)\n!chucknorris => Gives you a random fact about Chuck Norris\n!joke => Tells a random joke!\n!mathfact => Displays a random fact about the number you specify```")

    @commands.command(aliases = ["FOX"])
    async def fox(self, ctx):
        response = requests.get("https://randomfox.ca/floof")
        fox = response.json()
        await ctx.send(fox["image"])
    
    @commands.command(aliases = ["CAT"])
    async def cat(self, ctx):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        cat = response.json()

        for item in cat:
            await ctx.send(item["url"])
    
    @commands.command(aliases = ["ADVICE"])
    async def advice(self, ctx):
        response = requests.get("https://api.adviceslip.com/advice")
        advice = response.json()
        await ctx.send(advice["slip"]["advice"])

    @commands.command(aliases = ["chuckNorris", "ChuckNorris"])
    async def chucknorris(self, ctx):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        chucknorris = response.json()
        await ctx.send(chucknorris["value"])
    
    @commands.command(aliases = ["JOKE", "jokes"])
    async def joke(self, ctx):
        response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
        joke = response.json()
        await ctx.send(joke["joke"])
    
    @commands.command(aliases = ["mathfacts", "mathFact"])
    async def mathfact(self, ctx, number = None):
        if number:
            response = requests.get(f"http://numbersapi.com/{number}/?json")
            number_fact = response.json()
            await ctx.send(number_fact["text"])
        else:
            await ctx.send("You haven't specified a number or have given an incorrect value! Type !mathfact (or !mathfacts, !matHFact) followed by a number (such as: !mathfact 5)!")

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user) #1 use per user every 10 seconds
    async def reaction_response_test(self, ctx, message):
        msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
        await ctx.send(msg)
        

def setup(client):
    client.add_cog(other(client))
