from discord.ext import commands
import discord
import asyncio

class HepBot():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if "Here, take some credits. Enjoy!" in message.content:
            await message.ack()

        # def check(message):
        #     return "Here, take some credits. Enjoy!" in message.content
        #
        # try:
        #     msg = await self.bot.wait_for("message", check=check, timeout=5.0)
        # except asyncio.TimeoutError:
        #     return
        # await msg.ack()

    @commands.command()
    async def hepbot(self, ctx):
        tmp = await ctx.send("Going...")
        counter = 0
        channels = []
        for server in self.bot.guilds:
            if discord.utils.find(lambda m: m.name == "HepBot", server.members):
                for channel in server.text_channels:
                    if "bot" in channel.name and "spam" in channel.name\
                            and not "music" in channel.name and not "hidden" in channel.name and not "mod" in channel.name:
                        channels.append(channel)
                        break
                    else:
                        continue
                if not channel:
                    print(f"Can't find {server.id} ({server.name})'s botspam")
                    continue

            else:
                continue

        for botspam in channels:
            await botspam.send("!payday")
            counter += 1

        await tmp.edit(content=f"Done. Sent to {counter} servers.")
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(HepBot(bot))