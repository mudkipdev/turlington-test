import discord
import datetime
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix="?", intents=intents)

class Joinleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

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

async def setup(bot):
    await bot.add_cog(Joinleave(bot))