import os
from datetime import datetime 

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hi')
async def hi(ctx):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f'안녕하세요 name:{ctx.author.name} display_name: {ctx.author.display_name()}님! : {current_time}')
    
@bot.command(name='bye')
async def bye(ctx):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await ctx.send(f'안녕히가세요 name:{ctx.author.name} display_name: {ctx.author.display_name()}님! : {current_time}')

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')

bot.run(TOKEN)