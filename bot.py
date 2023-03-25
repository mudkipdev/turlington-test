#Turlington-Test

import asyncio
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

with open("bad_words.txt") as file: # bad-words.txt contains one blacklisted phrase per line
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

bot = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="?", intents=intents)
extensions = ("extensions.example",)

@bot.event
async def setup_hook():
    for extension in extensions:
        await bot.load_extension('moderation')
        await bot.load_extension('responses')

@bot.event
async def on_ready():
    print("Turlington is online and watching!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the servers."))

#join and leave
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1077747721336799282)
    embed=discord.Embed(title="Welcome!",description=f"{member.mention} just joined the server! Make sure to give them a warm welcome!", color=0x00FFFF)
    embed.add_field(name= "", value="Thank you for joining the TNF Server, make sure to check out #server-rules before sending your first message!", inline=False)
    embed.timestamp = datetime.datetime.now()
    embed.set_thumbnail(url="https://i.imgur.com/kQOJjQf.jpg")
    await channel.send(embed=embed)
    channel = bot.get_channel(1077724210924896266)
    embed=discord.Embed(title=f"User Joined",description=f"{member} just joined the server!", color=0x00FFFF)
    embed.set_footer(text=member.id)
    embed.set_thumbnail(url= "https://i.imgur.com/6anFs9h.jpg")
    embed.timestamp = datetime.datetime.now()
    await channel.send(embed=embed)
    await member.send("Welcome to the TNF server, we are happy to have you here! Please be sure to read all the rules before agreeing and when you are done feel free to check out either our RedM or Minecraft servers.")
    default_role = discord.utils.get(member.guild.roles, id=1077754252950241372)
    await member.add_roles(default_role)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1077724210924896266)
    embed=discord.Embed(title=f"User Left",description=f"{member} just left the server!", color=0x00FFFF)
    embed.set_footer(text=member.id)
    embed.set_thumbnail(url= "https://i.imgur.com/2pohyKU.png")
    embed.timestamp = datetime.datetime.now()
    await channel.send(embed=embed)
 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("**Try after {0} second ".format(round(error.retry_after, 2)))   

#embed commands
@bot.command('embed')
async def make_embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await bot.wait_for('message', check=check)
  
    await ctx.send('Waiting for a description')
    desc = await bot.wait_for('message', check=check)

    embed = discord.Embed(title=title.content, description=desc.content, color=0x1ABC9C)
    embed.set_author(name="Turlington", icon_url="https://i.imgur.com/YiAvyZb.jpg")
    
    await ctx.send(embed=embed)

@bot.command('embednoauthor')
async def make_embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await bot.wait_for('message', check=check)
  
    await ctx.send('Waiting for a description')
    desc = await bot.wait_for('message', check=check)

    embed = discord.Embed(title=title.content, description=desc.content, color=0x1ABC9C)
    
    await ctx.send(embed=embed)

#reaction role events
@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1080163076235595806:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '❌':
            role = discord.utils.get(guild.roles, id= 1080163217877254174)
        elif payload.emoji.name == '❌':
            role = discord.utils.get(guild.roles, id= 1080163217877254174)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '🟡':
            role = discord.utils.get(guild.roles, id= 1080272712288718909)
        elif payload.emoji.name == '🟡':
            role = discord.utils.get(guild.roles, id= 1080272712288718909)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, id= 1080277850827001916)
        elif payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, id= 1080277850827001916)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, id= 1080278011280101486)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, id= 1080278011280101486)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '⚫':
            role = discord.utils.get(guild.roles, id= 1080272666830844054)
        elif payload.emoji.name == '⚫':
            role = discord.utils.get(guild.roles, id= 1080272666830844054)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '💗':
            role = discord.utils.get(guild.roles, id= 1080278269615689768)
        elif payload.emoji.name == '💗':
            role = discord.utils.get(guild.roles, id= 1080278269615689768)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '🧿':
            role = discord.utils.get(guild.roles, id= 1080272432235032597)
        elif payload.emoji.name == '🧿':
            role = discord.utils.get(guild.roles, id= 1080272432235032597)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '🐥':
            role = discord.utils.get(guild.roles, id= 1080278571588784259)
        elif payload.emoji.name == '🐥':
            role = discord.utils.get(guild.roles, id= 1080278571588784259)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")
        message_id = payload.message_id
    if message_id == 1080270435880546384:  #ID depends on message
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == '🔴':
            role = discord.utils.get(guild.roles, id= 1080272351423385680)
        elif payload.emoji.name == '🔴':
            role = discord.utils.get(guild.roles, id= 1080272351423385680)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None: 
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added")
            else:
                print("Member not found")
        else:
            print("Role not found")

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1080163076235595806:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '❌':
            role = discord.utils.get(guild.roles, id= 1080163217877254174)
        elif payload.emoji.name == '❌':
            role = discord.utils.get(guild.roles, id= 1080163217877254174)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '🟡':
            role = discord.utils.get(guild.roles, id= 1080272712288718909)
        elif payload.emoji.name == '🟡':
            role = discord.utils.get(guild.roles, id= 1080272712288718909)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, id= 1080277850827001916)
        elif payload.emoji.name == '🔵':
            role = discord.utils.get(guild.roles, id= 1080277850827001916)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, id= 1080278011280101486)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, id= 1080278011280101486)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '⚫':
            role = discord.utils.get(guild.roles, id= 1080272666830844054)
        elif payload.emoji.name == '⚫':
            role = discord.utils.get(guild.roles, id= 1080272666830844054)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '💗':
            role = discord.utils.get(guild.roles, id= 1080278269615689768)
        elif payload.emoji.name == '💗':
            role = discord.utils.get(guild.roles, id= 1080278269615689768)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '🧿':
            role = discord.utils.get(guild.roles, id= 1080272432235032597)
        elif payload.emoji.name == '🧿':
            role = discord.utils.get(guild.roles, id= 1080272432235032597)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '🐥':
            role = discord.utils.get(guild.roles, id= 1080278571588784259)
        elif payload.emoji.name == '🐥':
            role = discord.utils.get(guild.roles, id= 1080278571588784259)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")
    message_id = payload.message_id
    if message_id == 1080270435880546384:
        guild_id = payload.guild_id
        guild = bot.get_guild(payload.guild_id)

        if payload.emoji.name == '🔴':
            role = discord.utils.get(guild.roles, id= 1080272351423385680)
        elif payload.emoji.name == '🔴':
            role = discord.utils.get(guild.roles, id= 1080272351423385680)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)
        
        if role is not None:
            member = await guild.fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed")
            else:
                print("Member not found")
        else:
            print("Role not found")

bot.run(TOKEN)