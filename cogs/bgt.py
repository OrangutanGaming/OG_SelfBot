from discord.ext import commands
import asyncio
import discord

class BGT():
    def __init__(self, bot):
        self.bot = bot
        # self.bg_task = self.bot.loop.create_task(self.my_background_task())

    # async def my_background_task(self):
    #     await self.bot.wait_until_ready()
    #     await asyncio.sleep(5)
    #     while True:
    #         await self.bot.get_channel(293128108570050560).send("s.hepbot")
    #         await asyncio.sleep(float(5*60))

    @commands.command()
    async def custom(self, ctx, id : int, msg : str):
        await self.bot.get_channel(id).send(msg)

def setup(bot):
    bot.add_cog(BGT(bot))