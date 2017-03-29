from discord.ext import commands
import discord
import asyncio

class HepBot():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if "Here, take some credits. Enjoy!" in message.content \
                or "Too soon. For your next payday you have to wait" in message.content:
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
        banned_ids=[]
        """
        banned_ids = [290953743233581057, # WarChat
                      166488311458824193, # RV
                      110373943822540800, # Discord Bots
                      213819570656378880, # WFRSB
                      81384788765712384, # Discord API
                      109379086845009920, # V (old)
                      281968634086031363 # V (New)
                      ]
        """

        banned_channel_names=["music", "hidden", "mod"]
        for server in self.bot.guilds:
            if discord.utils.find(lambda m: m.name == "HepBot", server.members):
                for channel in server.text_channels:
                    if "bot" in channel.name and "spam" in channel.name\
                            and not channel.name in banned_channel_names and not server.id in banned_ids:
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
            try:
                await botspam.send("!payday")
            except discord.Forbidden as error:
                print(f"{error}: {botspam.name}, {botspam.id}, {botspam.guild.name}")
            counter += 1

        await tmp.edit(content=f"Done. Sent to {counter} servers.")
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(HepBot(bot))