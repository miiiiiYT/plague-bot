import discord, discord.colour, json, traceback
from discord.ext import commands
from token_var import token_var


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

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
		gid = msg.guild.id
		

@bot.command()
async def setup(ctx, *args):
	try:
		cr_guild = ctx.message.guild
		perms = discord.Permissions()
		perms.value = 0
		rtn_role = await cr_guild.create_role(name=args[0], permissions=perms, color=discord.colour.Color.dark_green(), reason='Setup')
		out = {
			rtn_role.guild.id: rtn_role.id
        }

		with open("./roles.json", "r+") as file:
			data_ = json.load(file)
			data_.update(out)
			file.seek(0)
			json.dump(data_, file)

		await ctx.reply('Create role. Ready to play!')

	except Exception:
		traceback.print_exc()
		await ctx.reply('Something went wrong.')


bot.run(token_var)