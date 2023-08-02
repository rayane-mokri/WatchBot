import os
import json
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


def filedate(filename):
    return filename.split('_')[1]


def return_articles(theme):
    for article in articles[theme][next(iter(articles[theme].keys()))]:
        resp = f"**{article['title']}** \n Link : {article['link']}"
    return resp


dirname = "articles"
json_files = [f for f in os.listdir(dirname) if f.endswith('.json')]
sorted_json_files = sorted(json_files, key=lambda x: filedate(x), reverse=True)

if sorted_json_files:
    file = sorted_json_files[0]
    file_path = os.path.join(dirname, file)

    with open(file_path) as f:
        articles = json.load(f)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command(name="ml", help="Display top weekly MachineLeaning articles on Reddit")
async def python_articles(ctx):
    try:
        for article in articles["MachineLearning"][next(iter(articles["MachineLearning"].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


@bot.command(name="python", help="Display top weekly Python articles on Reddit")
async def python_articles(ctx):
    try:
        for article in articles["python"][next(iter(articles["python"].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


@bot.command(name="coding", help="Display top weekly Coding articles on Reddit")
async def python_articles(ctx):
    try:
        for article in articles["coding"][next(iter(articles["coding"].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


@bot.command(name="rust", help="Display top weekly Rust articles on Reddit")
async def python_articles(ctx):
    try:
        for article in articles["rust"][next(iter(articles["rust"].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


@bot.command(name="cpp", help="Display top weekly C++ articles on Reddit")
async def python_articles(ctx):
    try:
        for article in articles["cpp"][next(iter(articles["cpp"].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


@bot.command(name="go", help="Display top weekly Golang articles on Reddit")
async def python_articles(ctx):
    try:
        for article in articles["golang"][next(iter(articles["golang"].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


@bot.command(name="unreal", help="Display top weekly Unreal Engine articles on Reddit")
async def python_articles(ctx):
    try:
        for article in articles["unrealengine"][next(iter(articles["unrealengine"].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


@bot.command(name='clear', help='this command will clear 15 msgs')
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        # Envoyer un message d'erreur lorsque la commande n'est pas trouvée
        await ctx.send("Commande invalide.")

bot.run(DISCORD_TOKEN)

