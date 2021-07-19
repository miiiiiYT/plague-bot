# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
import random
from .setup import setup


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run('ODY2NjQ0NDk0ODc0NTc0ODc5.YPVjlQ.WmaWuzM5dHm8U84srSlGMt69fkA')