from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')

@bot.command()
async def dm(ctx, *, message : str):
    channel = bot.get_channel(ID here) #Channel ID MUST be an int, not a string!
    await channel.send(message)

bot.run("Token ID here") # Token ID MUST be a string (in quotes)!