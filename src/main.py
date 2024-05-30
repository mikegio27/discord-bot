#!/usr/bin/python3.11
import os
from discord.ext import commands
from cogs.music  import Music
from discord import Intents
from utils.logging import logger

token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='-', intents=Intents.all())

@bot.event
async def on_ready():
    logger.info(f'{bot.user} is running.')
    await bot.add_cog(Music(bot))

bot.run(token)

