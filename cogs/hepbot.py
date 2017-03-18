from discord.ext import commands
import discord
import asyncio

class HepBot():
    def __init__(self, bot):
        self.bot = bot

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
                        print(channel.name + " " + channel.guild.name)
                        channels.append(channel)
                        continue
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
        await asyncio.sleep(3)
        for botspam in channels:
            await botspam.ack()

        await tmp.edit(content=f"Done. Sent to {counter} servers.")
        await ctx.message.delete()
        # await asyncio.sleep(4)
        # discord.utils.find(msg.msg == 1, channel.guild.)

def setup(bot):
    bot.add_cog(HepBot(bot))