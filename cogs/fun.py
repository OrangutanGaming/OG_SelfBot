import discord
from discord.ext import commands
import time
import asyncio
import unicodedata

class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        pingT = (after - before) * 1000

        await ctx.message.edit(content="Ping. :ping_pong:")
        await ctx.send(content="Pong. :ping_pong: **{0:.0f}ms**".format(pingT))

    @commands.command()
    async def status(self, ctx, *, status: str):
        status = status.strip("`")
        await self.bot.change_presence(game=discord.Game(name=status))
        await asyncio.sleep(1)
        await ctx.message.edit(content=f"**Playing** {ctx.guild.me.game}")

    @commands.command()
    async def stat_test(self, ctx):
        await self.bot.change_presence(game=None)
        await ctx.message.edit(content="Playing set to None")

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):

        if len(characters) > 15:
            await ctx.send(f"Too many characters ({len(characters)}/15)")
            return

        fmt = "`\\U{0:>08}`: {1} - {2} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{0}>"

        def to_string(c):
            digit = format(ord(c), "x")
            name = unicodedata.name(c, "Name not found.")
            return fmt.format(digit, name, c)

        await ctx.send("\n".join(map(to_string, characters)))

def setup(bot):
    bot.add_cog(Fun(bot))