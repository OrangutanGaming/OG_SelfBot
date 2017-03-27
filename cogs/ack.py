from discord.ext import commands
import asyncio

class Ack():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ack(self, ctx):
        await ctx.message.add_reaction("\U00002705")
        for server in self.bot.guilds:
            await server.ack()

        await ctx.message.edit(content="All Messages are now read")
        await ctx.message.remove_reaction("\U00002705", ctx.guild.me)
        await asyncio.sleep(3)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Ack(bot))