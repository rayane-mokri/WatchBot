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


def choose_subject(subject):
    match subject:
        case "ml" | "machine learning" | "Machine Learning" | "ML":
            sub = "MachineLearning"
        case "go" | "Go" | "golang":
            sub = "golang"
        case "Rust":
            sub = "rust"
        case "code" | "Code":
            sub = "coding"
        case "Unreal" | "unreal" | "unrl":
            sub = "unrealengine"
        case _:
            sub = subject

    return sub


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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Commande invalide.")


@bot.command(name='clear', help='this command will clear 15 msgs')
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command(name="reddit", help="Display top 5 weekly. Topic covered : Python, Coding, Rust, Golang, Unreal Engine, C++")
async def reddit(ctx, subject):
    sub = choose_subject(subject)
    try:
        for article in articles[sub][next(iter(articles[sub].keys()))]:
            resp = f"**{article['title']}** \n Link : {article['link']}"
            await ctx.send(resp)
            time.sleep(2)
    except:
        await ctx.send("No articles")


bot.run(DISCORD_TOKEN)


