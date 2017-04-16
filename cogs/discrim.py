from discord.ext import commands

class Discriminator():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def discrim(self, ctx):
        cDisrim = self.bot.user.discriminator
        try:
            name = ", ".join(str(x) for x in self.bot.users if (x.discriminator == cDisrim)).replace(f"{str(self.bot.user)}, ", "").split(", ")[0]
        except IndexError:
            await ctx.send("Can't find anyone with the same discriminator as you.")
            return
        await ctx.send(name)

def setup(bot):
    bot.add_cog(Discriminator(bot))