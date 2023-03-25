import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

bot = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="?", intents=intents)

class responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @bot.listen()
    async def mentioned(message: discord.Message) -> None:
        print('Turlington has been mentioned.')
        if bot.user.mentioned_in(message):
            await message.channel.send(f"Hello! I am Turlington, say `?command` for more info on what I can do! If you are having any issues with my functions please tag ian `<@288522211164160010>`.")

    @bot.command
    async def generalcommands(ctx):
        await ctx.send("__All commands use ? prefix__ \n**ping** - check the status of Turlington\n**mcserver** - provides minecraft server details \n**mcserverstatus** - shows current TNF Minecraft server status\n**redmserver** - provides redmserver details" )
        channel = bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Command list access by {author}")


    @bot.command
    async def admincommands(ctx):
        channel = bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Admin command list access by {author}")
        role = discord.utils.get(ctx.guild.roles, name="admin")
        if role in ctx.author.roles:
            await ctx.send("__All commands use ? prefix__ \n**kick (@user)** - kicks the mentioned user\n**ban (@user)** - bans mentioned user, must manually unban through server settings currently \n**mute (@user)** - adds muted role to user which keeps them from chatting or seeing any channels except #muted\n**purge (number)** - removes the indicated amount of messages from channel command was used in")
            await bot.logout()
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")
    
    @bot.command
    async def minecraftcommands(ctx):
        channel = bot.get_channel(1086293466054656100)
        author = ctx.author.name
        await channel.send(f"Minecraft command list access by {author}")
        role = discord.utils.get(ctx.guild.roles, name="minecraft admin")
        if role in ctx.author.roles:
            await ctx.send("__All commands use ? prefix__ \n**mcserverstart** - starts the minecraft server\n**mcserverstop** - stops the minecraft server\n**mcservercommand (command in quotes)Im ** - sends the entered command to the minecraft server\n**mcservermessage (message)** - broadcasts the entered message to the minecraft server")
            await bot.logout()
        else:
            await ctx.send("Sorry, you dont have the required permissions to perform this command!")

async def setup(bot):
    await bot.add_cog(responses(bot))