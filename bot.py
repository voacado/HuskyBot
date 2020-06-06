from discord.ext import commands
from datetime import datetime
import discord

####################

# Specific information necessary for bot to function
# Obtain guild ID by right-clicking the server and clicking "Copy ID"
GUILD_ID = SERVER ID GOES HERE # Guild ID MUST be an int, not a string!

# Obtain channel ID by right-clicking the channel and clicking "Copy ID"
CHANNEL_ID = CHANNEL ID GOES HERE #Channel ID MUST be an int, not a string!

# Obtain bot token from Discord Developer Site
BOT_TOKEN = "TOKEN ID GOES HERE" # Token ID MUST be a string (in quotes)!

####################

# Creates the instances, uses "!" to activate commands
bot = commands.Bot(command_prefix='!')

# "!conf" command
@bot.command()
async def conf(ctx, *, message : str):

    # Obtains User ID and nickname to verify user is in guild/server
    userID = (ctx.message.author.id)
    server = bot.get_guild(GUILD_ID)
    member = server.get_member(userID)

    # If member is a member of the server, they will have a name (instead of None)
    if member != None:
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

    # If member is not a member is the server, they will be tagged None
    else:
      await ctx.send("You are not a member of the server! The message was not sent.")     

# Runs the bot given bot token ID
bot.run(BOT_TOKEN)
