import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # Railway-də əlavə edəcəyik

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} ilə giriş edildi.')

bot.run(TOKEN)
