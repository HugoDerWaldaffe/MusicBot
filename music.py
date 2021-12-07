import random

import discord
from discord.ext import commands as cd
import youtube_dl as yt
import ffmpeg
import os
from random import randrange

class music(cd.Cog):
    def __init__(self, client):
        self.client = client
        self.hornyMemes = memeList("horny")

    @cd.command()
    async def play(self, ctx, url):
        if ctx.author.voice is None:
            await ctx.send("Here is James. You're not in a voice channel")
            return
        current_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await current_channel.connect()
        else:
            await ctx.voice_client.move_to(current_channel)
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options" : "-vn"}
        YDL_OPTIONS = {"format" : "bestaudio", "forceip" : "0.0.0.0"}
        vc = ctx.voice_client

        with yt.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @cd.command()
    async def valtteri(self, ctx):
        await ctx.send("Is it you, James?")
        await ctx.send(file=discord.File("HappyBotas.jpg"))
        await ctx.send("Cheers ❤")

    @cd.command()
    async def bottas(self, ctx):
        #await ctx.send("Is it you, James?")
        await ctx.send(file=discord.File("formula1-f1.gif"))
        await ctx.send("Yes James? You called?")


    @cd.command()
    async def leave(self, ctx):
        ctx.voice_client.stop()
        await ctx.send("To whom it may concern: Fuck you!")
        await ctx.voice_client.disconnect()

    @cd.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("This is James, hold position!")

    @cd.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("This is James, ok take over!")

    @cd.command()
    async def horny(self, ctx):
        await ctx.send("Horny Test!")
        hornyMemes = memeList("horny")
        memeNum = random.randrange(10)
        fileName = "horny/" + hornyMemes[memeNum]
        await ctx.send(file=discord.File(fileName))


def memeList(directory):
    memes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".gif"):
                memes.append(file)
    return memes


def setup(client):
    client.add_cog(music(client))