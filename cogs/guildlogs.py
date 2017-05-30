from discord.ext import commands
import discord
import datetime

class Extension():
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, guild):
        channel = self.bot.get_channel(281483874234793984)
        message = await channel.get_message(318847435155963904)

        embed = discord.Embed(description=f"Current server count of {self.bot.user.mention}")
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.set_footer(text=("Server count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await message.edit(embed=embed)

    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(281483874234793984)
        message = await channel.get_message(318847435155963904)

        embed = discord.Embed(description=f"Current server count of {self.bot.user.mention}")
        embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
        embed.set_footer(text=("Server count since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await message.edit(embed=embed)

def setup(bot):
    bot.add_cog(Extension(bot))