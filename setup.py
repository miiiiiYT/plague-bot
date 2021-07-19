from .main import bot
import discord.colour

@bot.command()
async def setup(ctx, *args):
	try:
		cr_guild = ctx.message.guild
		cr_guild.create_role(name=args[0], permissions=0, color=discord.colour.Color.dark_green(), reason='Setup')
	except Exception as e:
		print(e)
		ctx.reply('Something went wrong.')
