import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from random import randint

bot = commands.Bot(command_prefix='r-')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="r-help"))


@bot.command(name="list", brief="returns list of all roles")
async def list(ctx, arg=None):
    try:
        if(arg is None):
            roles = "Your roles are: ```"
            rolesList = ctx.message.author
        elif(arg == "all"):
            roles = "This server's roles are: ```"
            rolesList = ctx.guild
        else:
            roles = arg + " role's are: ```"
            # returns list of roles for @mention
            rolesList = await ctx.guild.fetch_member(int(arg.strip("<!@>")))
        for x in rolesList.roles:
            roles += (str(x)+'\n')
        await ctx.send(roles+"```")
    except ValueError:
        await ctx.send("Invalid argument/user")

load_dotenv()
bot.run(getenv('TOKEN'))
