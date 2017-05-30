from discord.ext import commands
import discord
import datetime

class Extension():
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, guild):
        channel = self.bot.get_channel(318846410466394123)
        messageID = 318847435155963904
        message = None
        async for msg in channel.history():
            if msg.id == messageID:
                message = msg
                break

        if not message:
            await channel.send("Can't find the message.")
            return

        embed = discord.Embed(description=f"Current server count of {self.bot.user.mention}")
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.set_footer(text="Server count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S"))

        await message.edit(embed=embed)

    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(318846410466394123)
        messageID = 318847435155963904
        message = None
        async for msg in channel.history():
            if msg.id == messageID:
                message = msg
                break

        if not message:
            await channel.send("Can't find the message.")
            return

        embed = discord.Embed(description=f"Current server count of {self.bot.user.mention}")
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.set_footer(text=("Server count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await message.edit(embed=embed)

def setup(bot):
    bot.add_cog(Extension(bot))