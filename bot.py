import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ticket(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("Your ticket has been received! Support will contact you soon.")
    else:
        await ctx.author.send("Please use this command in DM with me!")
        await ctx.send(f"{ctx.author.mention}, I sent you a DM!")

bot.run(os.getenv("DISCORD_TOKEN"))
