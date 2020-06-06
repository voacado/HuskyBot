from discord.ext import commands
from datetime import datetime
import discord

# Specific information necessary for bot to function
# Obtain channel ID by right-clicking the channel and clicking "Copy ID"
CHANNEL_ID = ID_GOES_HERE #Channel ID MUST be an int, not a string!

# Obtain bot token from Discord Developer Site
BOT_TOKEN = "TOKEN_GOES_HERE" # Token ID MUST be a string (in quotes)!

# Creates the instance, uses "!" to activate commands
bot = commands.Bot(command_prefix='!')

# "!conf" command
@bot.command()
async def conf(ctx, *, message : str):

    # Assigns Discord channel (given channel ID)
    channel = bot.get_channel(CHANNEL_ID)

    # datetime object containing current date and time
    now = datetime.now()
    currentTime = now.strftime("%d/%m %H:%M")

    # Create embed message (looks better)
    embed = discord.Embed(description=message)

    # Set date/time as footer of embed
    embed.set_footer(text=currentTime)

    # Send message to channel
    await channel.send(embed=embed)

    # Inform user their message has been sent
    await ctx.send("Your message has been sent!")

# Runs the bot given bot token ID
bot.run(BOT_TOKEN)
