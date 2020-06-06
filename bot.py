from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')

@bot.command()
async def dm(ctx, *, message : str):
    channel = bot.get_channel(694333537762934865)
    await channel.send(message)

bot.run("NzE4NjgyNTI0NjkxMjAyMTE5.XtsbTQ.R7Wl5h_-KXQYadXQko1vsMYOzWg")