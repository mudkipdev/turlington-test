#Turlington-Test

import asyncio
import jishaku
import numbers
import os
import datetime
import tasks
import time
import mcstatus
import requests
from mcstatus import JavaServer
from ampapi.ampapi import AMPAPIHandler
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv

with open("bad_words.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

extensions = ("embed","joinleave","moderation","responses","jishaku", "reactions",)
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def setup_hook():
    for extension in extensions:
        await bot.load_extension(extension)

@bot.event
async def on_ready():
    print("Turlington is online and watching!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the servers."))
 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("**Try after {0} second ".format(round(error.retry_after, 2)))   

bot.run(TOKEN)