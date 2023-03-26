import os
from ampapi.ampapi import AMPAPIHandler
from dotenv import load_dotenv
from discord.ext import commands
import discord
import mcstatus

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

extensions = (
    "embed",
    "joinleave",
    "moderation",
    "responses",
    "reactions",
    "gameservers",
    "jishaku",
)
bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


@bot.event
async def setup_hook():
    for extension in extensions:
        await bot.load_extension(extension)


@bot.event
async def on_ready():
    print("Turlington is online and watching!")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="the servers."
        )
    )


@bot.event
async def on_command_error(ctx, exception, /):
    if isinstance(exception, commands.CommandOnCooldown):
        await ctx.send(
            "Try again after {0} seconds.".format(round(exception.retry_after, 2))
        )


bot.run(TOKEN)
