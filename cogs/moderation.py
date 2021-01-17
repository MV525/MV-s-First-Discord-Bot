import discord
from discord.ext import commands

#Creating the class and initialising to allow commands to be active
class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases = ["purge"])
    async def clear(self, ctx, *, clear_amount = None):
        if ctx.author.guild_permissions.manage_messages:
            if clear_amount:
                await ctx.channel.purge(limit=int(clear_amount))
                await ctx.send(f"Purged {clear_amount} messages")
            else:
                await ctx.send("Please specify how many messages you want to delete.")
        else:
            await ctx.send("You don't have the permission to do that!")


    @commands.command()
    async def kick(self, ctx, *, member: discord.Member=None):
        if ctx.author.guild_permissions.kick_members:
            if member:
                await member.kick()
                await ctx.send(f"{member} has been kicked!")
            else:
                await ctx.send("Please specify a user to kick!")
        else:
            await ctx.send("You don't have the permission to do that!")


    @commands.command()
    async def ban(self, ctx, *, member: discord.Member=None):
        if ctx.author.guild_permissions.ban_members:
            if member:
                await member.ban()
                await ctx.send(f"{member} has been banned!")
            else:
                await ctx.send("Please specify a user to ban!")
        else:
            await ctx.send("You don't have the permission to do that!")


    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        if ctx.author.guild_permissions.ban_members:
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f"Unbanned {user.name}#{user.discriminator}")
                    invite_link = await ctx.channel.create_invite(reason=None, max_uses=1, unique = True)
                    await user.send(f"You have been unbanned, {member}! Join back using: {invite_link}")
                    return
        else:
            await ctx.send("You don't have permission to do that!")



def setup(client):
    client.add_cog(moderation(client))
