import os
import time
import logging
import discord

from discord.ext import commands
from dotenv import load_dotenv

import reddit

top_articles = []


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
REDDIT_ID = os.getenv('REDDIT_ID')
REDDIT_SECRET = os.getenv('REDDIT_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PSSWD = os.getenv('REDDIT_PSSWD')

topics = ["MachineLearning", "python"]
reddit_top_articles = reddit.reddit_retrieve_top(topics, REDDIT_ID, REDDIT_SECRET,
                                                REDDIT_USERNAME, REDDIT_PSSWD)
intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents = intents)

@bot.command(name='python', help='display top reddit articles')
async def nine_nine(ctx):
    for article in reddit_top_articles["python"][0]:
        resp = f"**{article['title']}** \n Link : {article['link']}"
        await ctx.send(resp)
        time.sleep(2)

@bot.command(name='clear', help='this command will clear 15 msgs')
async def clear(ctx, amount = 15):
    await ctx.channel.purge(limit=amount)

@bot.command(name='ml', help='display top reddit articles')
async def nine_nine(ctx):
    for article in reddit_top_articles["MachineLearning"][0]:
        resp = f"**{article['title']}** \n Link : {article['link']}"
        await ctx.send(resp)
        time.sleep(2)
        
bot.run(TOKEN)