from logging import currentframe
import os
import sqlite3
from datetime import datetime 

from discord.ext import commands
from dotenv import load_dotenv

from utils.handle_db import *
from utils.handle_time import *

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
db_name = os.getenv('DISCORD_DB')
tb_name = os.getenv('DISCORD_DB_TB')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    init_db(db_name, tb_name)
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hi')
async def hi(ctx):
    current_time = get_current_time()
    start_study(ctx.author.name, tb_name, current_time)
    await ctx.send(f'{current_time} : 안녕하세요 {ctx.author.name}님!')
    
@bot.command(name='bye')
async def bye(ctx):
    current_time = get_current_time()
    await ctx.send(f'{current_time} :안녕히가세요 {ctx.author.name}님!')

@bot.command(name='list')
async def listing(ctx):
    list_all_from_db = list_study(tb_name)
    await ctx.send(list_all_from_db)

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(token)