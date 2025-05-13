import discord
from discord.ext import commands
import asyncio
import os

from cogs.match_module import JoinView, PickPlayerView, MapBanView

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olaraq daxil oldum.")

    # Persistent düymələr aktiv olsun
    bot.add_view(JoinView())
    bot.add_view(PickPlayerView())
    bot.add_view(MapBanView())

    try:
        synced = await bot.tree.sync()
        print(f"Slash komandaları sinxronlaşdırıldı ({len(synced)} komanda).")
    except Exception as e:
        print(f"Komandalar sinxronlaşdırılarkən xəta baş verdi: {e}")

async def main():
    async with bot:
        await bot.load_extension("cogs.match_module")
        await bot.start(os.environ["DISCORD_TOKEN"])  # Tokeni burada dəyişməyin!

asyncio.run(main())
