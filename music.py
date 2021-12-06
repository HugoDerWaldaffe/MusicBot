import discord
from discord.ext import commands as cd
import youtube_dl as yt
import ffmpeg

class music(cd.Cog):
    def __init__(self, client):
        self.client = client

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
        await ctx.send("Cheers <3")


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


    async def on_message(self, message, ctx):
        print(message)
        keywords = ["uwu", "cutie", "hot", "owo", ":heart:", "janni"]
        for word in keywords:
            if word in message.content:
                await ctx.send("Silence Wench! I do not wish to be horny anymore!")
                #await ctx.send()

def setup(client):
    client.add_cog(music(client))