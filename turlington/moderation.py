import discord
import asyncio
import datetime
from discord.ext import commands

with open("bad_words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]


class ModerationCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def purge(self, ctx: commands.Context, amount: int) -> None:
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Purge command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            msg = []
            async for x in ctx.channel.history(limit=amount):
                msg.append(x)
            await ctx.channel.delete_messages(msg)
            print(amount + " messages removed from the channel")

            channel = self.bot.get_channel(1077724210924896266)
            embed = discord.Embed(
                title="Messages have been purged",
                description=f"{amount} messages have been deleted from {channel}",
                color=0x00FFFF,
            )
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)

            await ctx.send(
                amount + " messages removed from the channel", delete_after=3
            )
        else:
            await ctx.send(
                "Sorry, you dont have the required permissions to perform this command!"
            )

    @commands.command()
    async def ban(self, ctx, member: discord.Member) -> None:
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Ban command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            await member.ban()
            channel = self.bot.get_channel(1077724210924896266)
            embed = discord.Embed(
                title=f"User has been banned",
                description=f"{member} has been banned from the server.",
                color=0x00FFFF,
            )
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print("A user has been banned")
        else:
            await ctx.send(
                "Sorry, you dont have the required permissions to perform this command!"
            )

    @commands.command()
    async def kick(self, ctx: commands.Context, member: discord.Member) -> None:
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Kick command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            await member.kick()
            channel = self.bot.get_channel(744246685932191805)
            embed = discord.Embed(
                title=f"User has been kicked",
                description=f"{member} has been kicked from the server.",
                color=0x00FFFF,
            )
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print("A user has been kicked")
        else:
            await ctx.send(
                "Sorry, you dont have the required permissions to perform this command!"
            )

    @commands.command()
    async def mute(self, ctx: commands.Context, member: discord.Member) -> None:
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Mute command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, id=1080349198374940684)
            await member.add_roles(role)
            channel = self.bot.get_channel(744246685932191805)
            embed = discord.Embed(
                title=f"User has been muted",
                description=f"{member} has been muted.",
                color=0x00FFFF,
            )
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print("A user has been muted")
        else:
            await ctx.send(
                "Sorry, you dont have the required permissions to perform this command!"
            )

    @commands.command()
    async def unmute(self, ctx: commands.Context, member: discord.Member) -> None:
        channel = self.bot.get_channel(1086293466054656100)
        await channel.send(f"Unmute command used by {ctx.author.name}")
        role = discord.utils.get(ctx.guild.roles, name="the creator")
        if role in ctx.author.roles:
            role = discord.utils.get(ctx.guild.roles, id=1080349198374940684)
            await member.remove_roles(role)
            channel = self.bot.get_channel(744246685932191805)
            embed = discord.Embed(
                title=f"User has been unmuted",
                description=f"{member} has been unmuted.",
                color=0x00FFFF,
            )
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            print("A user has been unmuted")
        else:
            await ctx.send(
                "Sorry, you dont have the required permissions to perform this command!"
            )

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        for bad_word in bad_words:
            if bad_word in message.content:
                print("Banned words scrubbed from chat.")
                await message.delete()
                await message.channel.send("That terminology is not permitted here.")
                channel = self.bot.get_channel(744246685932191805)
                embed = discord.Embed(
                    title="A censored word has been scrubbed.",
                    description=f"{message.author} has used the censored term, {bad_word}, and it has been scrubbed from the server.",
                    color=0x00FFFF,
                )
                embed.timestamp = datetime.datetime.now()
                await channel.send(embed=embed)
                channel = self.bot.get_channel(1086293466054656100)
                await channel.send(
                    f"A censored word has been used by {message.author} and scrubbed from chat."
                )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModerationCog(bot))
