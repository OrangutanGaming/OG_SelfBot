from discord.ext import commands

class Ack():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ack(self, ctx, server = None):
        servers = None
        await ctx.message.add_reaction("\U00002705")
        if not server:
            for server in self.bot.guilds:
                await server.ack()
                servers = False
        else:
            await ctx.guild.ack()
            servers = True

        if servers is True:
            await ctx.message.edit(content="All Messages are now read")
        else:
            await ctx.message.edit(content="This server is now read")
        await ctx.message.clear_reactions()

def setup(bot):
    bot.add_cog(Ack(bot))