import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

bot = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="?", intents=intents)

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @bot.command
    async def embed(ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        await ctx.send('Waiting for a title')
        title = await bot.wait_for('message', check=check)
  
        await ctx.send('Waiting for a description')
        desc = await bot.wait_for('message', check=check)

        embed = discord.Embed(title=title.content, description=desc.content, color=0x1ABC9C)
        embed.set_author(name="Turlington", icon_url="https://i.imgur.com/YiAvyZb.jpg")
    
        await ctx.send(embed=embed)

    @bot.command
    async def embednoauthor(ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        await ctx.send('Waiting for a title')
        title = await bot.wait_for('message', check=check)
  
        await ctx.send('Waiting for a description')
        desc = await bot.wait_for('message', check=check)

        embed = discord.Embed(title=title.content, description=desc.content, color=0x1ABC9C)
    
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Embed(bot))