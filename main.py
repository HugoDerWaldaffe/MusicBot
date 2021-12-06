import discord
from discord.ext import commands as cd
import music
import os

cogs = [music]
logs = open("logs.txt", "w")

client = cd.Bot(command_prefix="+", intents=discord.Intents.all())
Bot = discord.Client()

@client.event
async def on_message(message):
    keywords = ["uwu", "cutie", "hot", "owo", "❤", "janni"]
    whench = "Silence Wench! I do not wish to be horny anymore!"
    print("here")
    for word in keywords:
        if word in message.content:
            await message.channel.send(whench)

for i in range(len(cogs)):
    cogs[i].setup(client)

#Bot.run(os.environ["TOKEN"])
client.run(os.environ["TOKEN"])
