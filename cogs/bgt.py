from discord.ext import commands
import asyncio
import discord
import datetime

class BGT():
    def __init__(self, bot):
        self.bot = bot
        # self.bg_task = self.bot.loop.create_task(self.AllianceAnnounceStart())
        # self.bg_task = self.bot.loop.create_task(self.AllianceAnnounceEnd())
        self.bg_task = self.bot.loop.create_task(self.TimeTest())

    async def AllianceAnnounceStart(self):
        await self.bot.wait_until_ready()
        while True:
            now = datetime.datetime.utcnow()
            if now.date() == datetime.date(2017, 6, 12) and now.time() >= datetime.time(7):
                await self.bot.get_channel(282207136354926594).send("@everyone And so it begins!")
                break

    async def AllianceAnnounceEnd(self):
        await self.bot.wait_until_ready()
        while True:
            now = datetime.datetime.utcnow()
            if now.date() == datetime.date(2017, 6, 12) and now.time() >= datetime.time(7):
                await self.bot.get_channel(282207136354926594).send("@everyone And so it begins!")
                break

    async def TimeTest(self):
        await self.bot.wait_until_ready()
        while True:
            now = datetime.datetime.utcnow()
            if now.date() == datetime.date(2017, 6, 12) and now.time() >= datetime.time(6, 10):
                await self.bot.get_channel(281483874234793984).send("Hi")
                break


    @commands.command()
    async def custom(self, ctx, id : int, msg : str):
        await self.bot.get_channel(id).send(msg)

def setup(bot):
    bot.add_cog(BGT(bot))
