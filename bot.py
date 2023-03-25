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
server = JavaServer.lookup("")
intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

bot = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="?", intents=intents)


@bot.event
async def on_ready():
    print("Turlington is online and watching!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the servers."))

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

#responses and command lists
@bot.listen()
async def on_message(message: discord.Message) -> None:
    print('Turlington has been mentioned.')
    if bot.user.mentioned_in(message):
            await message.channel.send(f"Hello! I am Turlington, say `?command` for more info on what I can do! If you are having any issues with my functions please tag ian `<@288522211164160010>`.")

@bot.command(name= 'ping')
async def ping(ctx):
    await ctx.send("Hello! I am here.")

@bot.command(name='commands')
async def ping(ctx):
    await ctx.send("__All commands use ? prefix__ \n**ping** - check the status of Turlington\n**mcserver** - provides minecraft server details \n**mcserverstatus** - shows current TNF Minecraft server status\n**redmserver** - provides redmserver details" )
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"Command list access by {author}")


@bot.command(name='admincommands')
async def send_data(ctx):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"Admin command list access by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        await ctx.send("__All commands use ? prefix__ \n**kick (@user)** - kicks the mentioned user\n**ban (@user)** - bans mentioned user, must manually unban through server settings currently \n**mute (@user)** - adds muted role to user which keeps them from chatting or seeing any channels except #muted\n**purge (number)** - removes the indicated amount of messages from channel command was used in")
        await bot.logout()
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")
    

@bot.command(name='mccommands')
async def send_data(ctx):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"Minecraft command list access by {author}")
    role = discord.utils.get(ctx.guild.roles, name="minecraft admin")
    if role in ctx.author.roles:
        await ctx.send("__All commands use ? prefix__ \n**mcserverstart** - starts the minecraft server\n**mcserverstop** - stops the minecraft server\n**mcservercommand (command in quotes)Im ** - sends the entered command to the minecraft server\n**mcservermessage (message)** - broadcasts the entered message to the minecraft server")
        await bot.logout()
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

#game server commands
instance_id = "instanceID"

API = AMPAPIHandler(
    baseUri=f"http://xx.xx.xxx.xxx:8080/API/ADSModule/Servers/{instance_id}/",
    username="admin",
    password="TNFAdmin1"
)
API.initHandler()

result = API.Core.GetStatus()
print(result)

API.Core.SendConsoleMessage("Turlington is now connected.")

@bot.command(name='mcserver')
async def send_data(ctx):
    await ctx.send("**Server Type:** Public Vanilla \n**Server IP/Connection:** xx.xx.xxx.xxx:XXXXXX.")
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"MC Server info command used by {author}")

@bot.command(name='redmserver')
async def send_data(ctx):
    await ctx.send("**Server Type:** Public Vanilla \n**Server IP/Connection:** xx.xx.xxx.xxx:XXXXXX or search TNF in launcher.")
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"RedM Server info command used by {author}")

    await ctx.send("Hello! I am here.")

@bot.command(name= 'mcserverstatus')
async def mcserver(ctx):
    status = server.status()
    print("The server is online and replied in {0} ms".format(status.latency))
    await ctx.channel.send("The server is online with {0} players and replied in {1}ms".format(status.players.online, status.latency))
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"MC Server status command used by {author}")

@bot.command(name= 'mcserverstart')
async def mcserver_start(ctx):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"MC Server start command used by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        API.Core.Start()
        await ctx.send("The Minecraft server is starting, please allow a moment or two before attempting to connect.")
        print("Starting TNF Minecraft server.")
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

@bot.command(name= 'mcserverstop')
async def mcserver_stop(ctx):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"MC Server stop command used by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        API.Core.Stop()
        await ctx.send("The Minecraft server is stopping, please allow a moment for all functions to come to a halt and world to properly save.")
        print("Shutting down TNF Minecraft server.")
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

@bot.command(name= 'mcservercommand')
async def mcserver_command(ctx, *args):
    arguments = ' '.join(args)
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        API.Core.SendConsoleMessage(f"{arguments}")
        await ctx.send("Your command has been sent.")
        print("Sent " + arguments + " command to server console.")
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")
        channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"{arguments} command sent to MC console by {author}")

@bot.command(name= 'mcservermessage')
async def mcserver_broadcast(ctx, cmd):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"{cmd} has been broadcast to the MC server by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        API.Core.SendConsoleMessage("say " + cmd)
        await ctx.send("Your message has been broadcasted.")
        print("Broadcasted " + cmd + " to server.")
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")
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

#moderation commands
@bot.command(name= 'purge')
async def purge(ctx, num):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"Purge command used by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        msg = []
        async for x in ctx.channel.history(limit=int(num)):
            msg.append(x)
        await ctx.channel.delete_messages(msg)
        print(num + ' messages removed from the channel')
        channel = bot.get_channel(1077724210924896266)
        embed=discord.Embed(title=f"Messages have been purged",description=f"{num} messages have been deleted from {channel}", color=0x00FFFF)
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        warning = await ctx.send(num + ' messages removed from the channel')

        await asyncio.sleep(3)
        await warning.delete()
        await bot.logout()
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

@bot.command(name= "ban")
async def ban(ctx, user: discord.Member):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"Ban command used by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        await user.ban()
        channel = bot.get_channel(1077724210924896266)
        embed=discord.Embed(title=f"User has been banned",description=f"{user} has been banned from the server.", color=0x00FFFF)
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        print('A user has been banned')
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

@bot.command(name= 'kick')
async def kick(ctx, user: discord.Member):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"Kick command used by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        await user.kick()
        channel = bot.get_channel(744246685932191805)
        embed=discord.Embed(title=f"User has been kicked",description=f"{user} has been kicked from the server.", color=0x00FFFF)
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        print('A user has been kicked')
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

@bot.command(name= 'mute')
async def mute(ctx, user: discord.Member):
    channel = bot.get_channel(1086293466054656100)   
    author = ctx.author.name
    await channel.send(f"Mute command used by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        role = discord.utils.get(ctx.guild.roles, id= 1080349198374940684)
        await user.add_roles(role)
        channel = bot.get_channel(744246685932191805)
        embed=discord.Embed(title=f"User has been muted",description=f"{user} has been muted.", color=0x00FFFF)
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        print('A user has been muted')
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

@bot.command(name= 'unmute')
async def unmute(ctx, user: discord.Member):
    channel = bot.get_channel(1086293466054656100)
    author = ctx.author.name
    await channel.send(f"Unmute command used by {author}")
    role = discord.utils.get(ctx.guild.roles, name="admin")
    if role in ctx.author.roles:
        role = discord.utils.get(ctx.guild.roles, id= 1080349198374940684)
        await user.remove_roles(role)
        channel = bot.get_channel(744246685932191805)
        embed=discord.Embed(title=f"User has been unmuted",description=f"{user} has been unmuted.", color=0x00FFFF)
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)
        print('A user has been unmuted')
    else:
        await ctx.send("Sorry, you dont have the required permissions to perform this command!")

@bot.event    
async def on_message(message):
    for bad_word in bad_words:
        if bad_word in message.content:
            print("Banned words scrubbed from chat.")
            await message.delete()
            await message.channel.send("That terminology is not permitted here.")
            channel = bot.get_channel(744246685932191805)
            embed=discord.Embed(title=f"A censored word has been scrubbed.",description=f"{message.author} has used the censored term, {bad_word}, and it has been scrubbed from the server.", color=0x00FFFF)
            embed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            channel = bot.get_channel(1086293466054656100)
            await channel.send(f"A censored word has been used by {message.author} and scrubbed from chat.")
    await bot.process_commands(message)


bot.run(TOKEN)