import discord
from discord.ext import commands


class Responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if self.bot.user.mentioned_in(message):
            await message.channel.send(
                "Hello! I am Turlington, say `?command` for more info on what I can do! If you are having any issues with my functions please tag ian `<@288522211164160010>`."
            )

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("ping")

    @commands.command(name="generalcommands")
    async def generalcommands(self, ctx: commands.Context) -> None:
        await ctx.send(
            """
            __All commands use__ the `?` __prefix__
            **ping** - check the status of Turlington
            **mcserver** - provides minecraft server details
            **mcserverstatus** - shows current TNF Minecraft server status
            **redmserver** - provides redmserver details
            """
        )
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Command list access by {author}")

    @commands.command(name="admincommands")
    async def admin_commands(self, ctx: commands.Context) -> None:
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Admin command list access by {author}")
        role = discord.utils.get(ctx.guild.roles, name="admin")
        if role in ctx.author.roles:
            await ctx.send(
                "__All commands use ? prefix__ \n**kick (@user)** - kicks the mentioned user\n**ban (@user)** - bans mentioned user, must manually unban through server settings currently \n**mute (@user)** - adds muted role to user which keeps them from chatting or seeing any channels except #muted\n**purge (number)** - removes the indicated amount of messages from channel command was used in"
            )
            await self.bot.logout()
        else:
            await ctx.send(
                "Sorry, you dont have the required permissions to perform this command!"
            )

    @commands.command(name="minecraftcommands")
    async def minecraft_commands(self, ctx: commands.Context) -> None:
        channel = self.bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Minecraft command list access by {author}")
        role = discord.utils.get(ctx.guild.roles, name="minecraft admin")
        if role in ctx.author.roles:
            await ctx.send(
                "__All commands use ? prefix__ \n**mcserverstart** - starts the minecraft server\n**mcserverstop** - stops the minecraft server\n**mcservercommand (command in quotes)Im ** - sends the entered command to the minecraft server\n**mcservermessage (message)** - broadcasts the entered message to the minecraft server"
            )
            await self.bot.logout()
        else:
            await ctx.send(
                "Sorry, you dont have the required permissions to perform this command!"
            )


async def setup(bot):
    await bot.add_cog(Responses(bot))
