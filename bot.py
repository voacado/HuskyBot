from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')

@bot.command()
async def dm(ctx, *, message : str):
    channel = bot.get_channel("Channel ID here")
    await channel.send(message)

bot.run("Token ID here")