import discord
import asyncio
import datetime
from discord.ext import commands

with open("bad_words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def purge(self, ctx, num):
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Purge command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            msg = []
            async for x in ctx.channel.history(limit=int(num)):
                msg.append(x)
            await ctx.channel.delete_messages(msg)
            print(num + ' messages removed from the channel')
            channel = self.bot.get_channel(1077724210924896266)
            embed=discord.Embed(title=f"Messages have been purged",description=f"{num} messages have been deleted from {channel}", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            warning = await ctx.send(num + ' messages removed from the channel')

            await asyncio.sleep(3)
            await warning.delete()
            await self.bot.logout()
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.command()
    async def ban(self, ctx, user: discord.Member):
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Ban command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            await user.ban()
            channel = self.bot.get_channel(1077724210924896266)
            embed=discord.Embed(title=f"User has been banned",description=f"{user} has been banned from the server.", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print('A user has been banned')
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.command()
    async def kick(self, ctx, user: discord.Member):
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Kick command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            await user.kick()
            channel = self.bot.get_channel(744246685932191805)
            embed=discord.Embed(title=f"User has been kicked",description=f"{user} has been kicked from the server.", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print('A user has been kicked')
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.command()
    async def mute(self, ctx, user: discord.Member):
        channel = self.bot.get_channel(1086293466054656100)   
        author = ctx.author.name
        await channel.send(f"Mute command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, id= 1080349198374940684)
            await user.add_roles(role)
            channel = self.bot.get_channel(744246685932191805)
            embed=discord.Embed(title=f"User has been muted",description=f"{user} has been muted.", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print('A user has been muted')
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.command()
    async def unmute(self, ctx, user: discord.Member):
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Unmute command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, id= 1080349198374940684)
            await user.remove_roles(role)
            channel = self.bot.get_channel(744246685932191805)
            embed=discord.Embed(title=f"User has been unmuted",description=f"{user} has been unmuted.", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print('A user has been unmuted')
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.Cog.listener()   
    async def on_message(self, message):
        for bad_word in bad_words:
            if bad_word in message.content:
                print("Banned words scrubbed from chat.")
                await message.delete()
                await message.channel.send("That terminology is not permitted here.")
                channel = self.bot.get_channel(744246685932191805)
                embed=discord.Embed(title=f"A censored word has been scrubbed.",description=f"{message.author} has used the censored term, {bad_word}, and it has been scrubbed from the server.", color=0x00FFFF)
                embed.timestamp = datetime.datetime.now()
                await channel.send(embed=embed)
                channel = self.bot.get_channel(1086293466054656100)
                await channel.send(f"A censored word has been used by {message.author} and scrubbed from chat.")
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Moderation(bot))