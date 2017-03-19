from discord.ext import commands
import asyncio
import discord

class BGT():
    def __init__(self, bot):
        self.bot = bot
        self.bg_task = self.bot.loop.create_task(self.my_background_task())

    async def my_background_task(self):
        await self.bot.wait_until_ready()
        while True:
            server = discord.utils.get(self.bot.guilds, id=281483874234793984)
            channel = discord.utils.get(server.text_channels, id=281483874234793984)
            await channel.send("s.hepbot")
            await asyncio.sleep((5*60))

def setup(bot):
    bot.add_cog(BGT(bot))