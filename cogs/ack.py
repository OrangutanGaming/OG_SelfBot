from discord.ext import commands

class Ack():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ack(self, ctx, server = None):
        if not server:
            for server in self.bot.guilds:
                await server.ack()
        else:
            await ctx.guild.ack()
        await ctx.message.edit(content="All Messages are now read")

def setup(bot):
    bot.add_cog(Ack(bot))