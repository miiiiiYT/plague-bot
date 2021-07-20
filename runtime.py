import discord, discord.colour
from discord.ext import commands
from token_var import token_var


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(msg):
    if msg.guild == None:
        msg.reply('This bot only works in groups.')
    else:
        # if msg.author.roles 
        print(msg.author.roles)

@bot.command()
async def setup(ctx, *args):
	try:
		cr_guild = ctx.message.guild
		cr_guild.create_role(name=args[0], permissions=0, color=discord.colour.Color.dark_green(), reason='Setup')
	except Exception as e:
		print(e)
		ctx.reply('Something went wrong.')


bot.run(token_var)