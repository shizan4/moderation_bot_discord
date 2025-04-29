import discord
from discord import Option
from discord.ext import commands
from discord.ext.commands import MissingPermissions

bot = discord.Bot() 

servers = [server id] #server ids

@bot.event
async def on_ready():
    print("We have logged in!")

@bot.slash_command(guild_ids = servers, name = "mute", description = "mutes the bot")
@commands.has_permissions(ban_members = True, administrator = True)
async def ban(ctx, member: Option(discord.Member, description = "Who do you want to ban?"), reason: Option(str, description = "Why?", required = False)):
    if member.id == ctx.author.id: #checks to see if they're the same
        await ctx.respond("")
    elif member.guild_permissions.administrator:
        await ctx.respond("")
    else:
        if reason == None:
            reason = f"None provided by {ctx.author}"
        await member.ban(reason = reason)
        
@bot.slash_command(guild_ids = servers, name = "mute", description = "mutes the bot")
@commands.has_permissions(unban_members = True, administrator = True)
async def ban(ctx, member: Option(discord.Member, description = "Who do you want to unban?"), reason: Option(str, description = "Why?", required = False)):
    if member.id == ctx.author.id: #checks to see if they're the same
        await ctx.respond("")
    elif member.guild_permissions.administrator:
        await ctx.respond("")
    else:
        if reason == None:
            reason = f"None provided by {ctx.author}"
        await member.unban(reason = reason)
        
    

@bot.slash_command(guild_ids = servers, name = "disconnect", description = "disconnects the player")
@commands.has_permissions(kick_members = True, administrator = True)
async def kick(ctx, member: Option(discord.Member, description = "Who do you want to kick?"), reason: Option(str, description = "Why?", required = False)):
    if member.id == ctx.author.id: #checks to see if they're the same
        await ctx.respond("")
    elif member.guild_permissions.administrator:
        await ctx.respond("")
    else:
        if reason == None:
            reason = f"None provided by {ctx.author}"
        await member.kick(reason = reason)
        


bot.run('TOKEN') #token: KEEP THIS SAFE, from your developer portal