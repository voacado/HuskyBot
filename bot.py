from discord.ext import commands
from datetime import datetime
import discord

# Creates the instance, uses "!" to activate commands
bot = commands.Bot(command_prefix='!')

# "!dm" command
@bot.command()
async def conf(ctx, *, message : str):

    # Assigns Discord channel
    channel = bot.get_channel(Your Channel ID Here) #Channel ID MUST be an int, not a string!

    # Create embed message (looks better)
    embed = discord.Embed(title=message)

    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # Set date/time as footer of embed
    embed.set_footer(text=dt_string)

    # Send message to channel
    await channel.send(embed=embed)

bot.run("Your Token ID Here") # Token ID MUST be a string (in quotes)!