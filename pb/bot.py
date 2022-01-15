import os
import random

from discord.ext import commands
from dotenv import load_dotenv

from .util import read_prompts

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

BASE_PROMPT_LIST = read_prompts()


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="prompt", help="Responds with a prompt")
async def prompt(ctx):
    response = random.choice(BASE_PROMPT_LIST)
    await ctx.send(response)


bot.run(TOKEN)
