import discord
from discord.ext import commands as cd
import music
import os

cogs = [music]

client = cd.Bot(command_prefix="+", intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(os.environ["TOKEN"])