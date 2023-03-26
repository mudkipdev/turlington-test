import discord
import datetime
from discord.ext import commands

WELCOME_GIF = "https://i.imgur.com/kQOJjQf.jpg"
WELCOME_LOG_GIF = "https://i.imgur.com/6anFs9h.jpg"
LEAVE_GIF = "https://i.imgur.com/2pohyKU.png"
WELCOME_CHANNEL = 1077747721336799282
LOG_CHANNEL = 1077724210924896266
DEFAULT_ROLE = 1077754252950241372


class JoinLeaveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        channel = self.bot.get_channel(WELCOME_CHANNEL)
        embed = discord.Embed(
            title="Welcome!",
            description=f"{member.mention} just joined the server! Make sure to give them a warm welcome!",
            color=0x00FFFF,
        )
        embed.add_field(
            name="",
            value="Thank you for joining the TNF Server, make sure to check out #server-rules before sending your first message!",
        )
        embed.timestamp = datetime.datetime.now()
        embed.set_thumbnail(url=WELCOME_GIF)
        await channel.send(embed=embed)

        channel = self.bot.get_channel(WELCOME_LOG_CHANNEL)
        embed = discord.Embed(
            title="User Joined",
            description=f"{member} just joined the server!",
            color=0x00FFFF,
        )
        embed.set_footer(text=member.id)
        embed.set_thumbnail(url=WELCOME_LOG_GIF)
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)

        await member.send(
            "Welcome to the TNF server, we are happy to have you here! Please be sure to read all the rules before agreeing and when you are done feel free to check out either our RedM or Minecraft servers."
        )
        await member.add_roles(member.guild.get_role(DEFAULT_ROLE))

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member) -> None:
        channel = self.bot.get_channel(LOG_CHANNEL)
        embed = discord.Embed(
            title=f"User Left",
            description=f"{member} just left the server!",
            color=0x00FFFF,
        )
        embed.set_footer(text=member.id)
        embed.set_thumbnail(url=LEAVE_GIF)
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(JoinLeaveCog(bot))
