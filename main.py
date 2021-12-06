import discord
from discord.ext import commands as cd
import music
import os

cogs = [music]

client = cd.Bot(command_prefix="+", intents=discord.Intents.all())
Bot = cd.Bot(command_prefix="")

@Bot.event
async def on_message(message):
    keywords = ["uwu", "cutie", "hot", "owo", ":heart:", "janni"]
    whench = "Silence Wench! I do not wish to be horny anymore!"
    for word in keywords:
        if word in message.content:
            await Bot.send_message(message.channel, whench)

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(os.environ["TOKEN"])