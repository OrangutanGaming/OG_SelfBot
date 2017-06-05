from discord.ext import commands
import asyncio
import discord
import datetime

class BGT():
    def __init__(self, bot):
        self.bot = bot
        self.bg_task = self.bot.loop.create_task(self.AllianceAnnounceEnd())
        # self.bg_task = self.bot.loop.create_task(self.TimeTest())

    async def AllianceAnnounceEnd(self):
        await self.bot.wait_until_ready()
        while True:
            now = datetime.datetime.utcnow()
            targetD = "12.6.2017".split(".")
            targetT = "7:45".split(":")

            targetT = [int(t) for t in targetT]
            targetD = [int(t) for t in targetD]
            if now.date() == datetime.date(targetD[2], targetD[1], targetD[0]) and \
                datetime.time(targetT[0], targetT[1]) <= now.time() <= datetime.time(targetT[0], targetT[1] + 1):
                await self.bot.get_channel(281483874234793984).send("The event is now over! Stay tuned for prizes!")
                # break
            await asyncio.sleep(60)

    async def TimeTest(self):
        await self.bot.wait_until_ready()
        while True:
            now = datetime.datetime.utcnow()
            targetD = "5.6.2017".split(".")
            targetT = "15:24".split(":")

            targetT = [int(t) for t in targetT]
            targetD = [int(t) for t in targetD]
            if now.date() == datetime.date(targetD[2], targetD[1], targetD[0]) and \
                datetime.time(targetT[0], targetT[1]) <= now.time() <= datetime.time(targetT[0], targetT[1]+1):
                await self.bot.get_channel(281483874234793984).send("Hi")
                break
            await asyncio.sleep(60)


    @commands.command()
    async def custom(self, ctx, id : int, msg : str):
        await self.bot.get_channel(id).send(msg)

def setup(bot):
    bot.add_cog(BGT(bot))
