from discord.ext import commands
import discord

EMBED_COLOR = 0x1ABC9C


class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx: commands.Context) -> None:
        def check(message) -> bool:
            return message.author == ctx.author and message.channel == ctx.channel

        # TODO: handle timeout nicely
        await ctx.send("Waiting for a title")
        title = await self.bot.wait_for("message", check=check)

        await ctx.send("Waiting for a description")
        description = await self.bot.wait_for("message", check=check)

        embed = discord.Embed(
            title=title.content, description=description.content, color=EMBED_COLOR
        )
        embed.set_author(name="Turlington", icon_url="https://i.imgur.com/YiAvyZb.jpg")

        await ctx.send(embed=embed)

    @commands.command(name="embednoauthor")
    async def embed_with_no_author(self, ctx: commands.Context) -> None:
        def check(message) -> bool:
            return message.author == ctx.author and message.channel == ctx.channel

        # TODO: handle timeout nicely
        await ctx.send("Waiting for a title")
        title = await self.bot.wait_for("message", check=check)

        await ctx.send("Waiting for a description")
        description = await self.bot.wait_for("message", check=check)

        await ctx.send(
            embed=discord.Embed(
                title=title.content, description=description.content, color=EMBED_COLOR
            )
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EmbedCog(bot))
