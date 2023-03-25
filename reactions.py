import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix="?", intents=intents)

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

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

async def setup(bot):
    await bot.add_cog(Reactions(bot))