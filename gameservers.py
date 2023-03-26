import discord
import ampapi
import os
from mcstatus import JavaServer
from ampapi.ampapi import AMPAPIHandler
from discord.ext import commands
from dotenv import load_dotenv

server = JavaServer.lookup("")
instance_id = os.getenv('instance_id')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

API = AMPAPIHandler(
    baseUri=f"/",
    username="",
    password=""
)
API.initHandler()


result = API.Core.GetStatus()
print(result)

API.Core.SendConsoleMessage("Turlington is now connected.")

class Gameservers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def minecraftserver(self, ctx):
        await ctx.send("**Server Type:** Public Vanilla \n**Server IP/Connection:** .")
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"MC Server info command used by {author}")

    @commands.command()
    async def redmserver(self, ctx):
        await ctx.send("**Server Type:** Public Vanilla \n**Server IP/Connection:**  or search TNF in launcher.")
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"RedM Server info command used by {author}")

        await ctx.send("Hello! I am here.")

    @commands.command()
    async def mcserverstatus(self, ctx):
        status = server.status()
        print("The server is online and replied in {0} ms".format(status.latency))
        await ctx.channel.send("The server is online with {0} players and replied in {1}ms".format(status.players.online, status.latency))
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"MC Server status command used by {author}")

    @commands.command()
    async def mcserverstart(self, ctx):
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"MC Server start command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="admin")
        if role in ctx.author.roles:
            API.Core.Start()
            await ctx.send("The Minecraft server is starting, please allow a moment or two before attempting to connect.")
            print("Starting TNF Minecraft server.")
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.command()
    async def mcserverstop(self, ctx):
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"MC Server stop command used by {author}")
        role = discord.utils.get(ctx.guild.roles, name="admin")
        if role in ctx.author.roles:
            API.Core.Stop()
            await ctx.send("The Minecraft server is stopping, please allow a moment for all functions to come to a halt and world to properly save.")
            print("Shutting down TNF Minecraft server.")
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

    @commands.command()
    async def mcservercommand(self, ctx, *args):
        arguments = ' '.join(args)
        role = discord.utils.get(ctx.guild.roles, name="admin")
        if role in ctx.author.roles:
            API.Core.SendConsoleMessage(f"{arguments}")
            await ctx.send("Your command has been sent.")
            print("Sent " + arguments + " command to server console.")
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")
            channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"{arguments} command sent to MC console by {author}")

    @commands.command()
    async def mcservermessage(self, ctx, cmd):
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"{cmd} has been broadcast to the MC server by {author}")
        role = discord.utils.get(ctx.guild.roles, name="admin")
        if role in ctx.author.roles:
            API.Core.SendConsoleMessage("say " + cmd)
            await ctx.send("Your message has been broadcasted.")
            print("Broadcasted " + cmd + " to server.")
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

async def setup(bot):
    await bot.add_cog(Gameservers(bot))