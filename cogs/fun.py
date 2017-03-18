import discord
from discord.ext import commands
import time
import asyncio

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
        await ctx.message.edit(content=f"**Playing** {guild.me.game}")

    @commands.command()
    async def stat_test(self, ctx):
        await self.bot.change_presence(game=None)
        await ctx.message.edit(content="Playing set to None")

def setup(bot):
    bot.add_cog(Fun(bot))