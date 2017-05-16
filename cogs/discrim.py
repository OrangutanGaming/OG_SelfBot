from discord.ext import commands

class Discriminator():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def discrim(self, ctx):
        cDisrim = self.bot.user.discriminator
        dreamDiscs = ["0001",
                      "1000",
                      "7777",
                      "8888",
                      "9999",
                      "0101",
                      "2003",
                      "8000",
                      "8008",
                      "1234",
                      "0002",
                      "0003",
                      "0005",
                      "0006",
                      "0007",
                      "0008",
                      "0009",
                      "9876",
                      "5555",
                      "3825"
                      ]

        try:
            name = ", ".join(str(x) for x in self.bot.users if (x.discriminator == cDisrim)).replace(f"{str(self.bot.user)}, ", "").split(", ")[0]
        except IndexError:
            await ctx.send("Can't find anyone with the same discriminator as you.")
            return
        try:
            await self.bot.user.edit(password=SelfIDs.password, username=name[:-5])
            await ctx.send(f"{self.bot.user.mention} #{self.bot.user.discriminator}")
        except:
            await ctx.send("Error. You have probably already changed your username twice in the last hour. If not, PANIC!"
                           f"\nYour new username will be `{name}`. This error could also be a username that's too popular.")
            return

def setup(bot):
    bot.add_cog(Discriminator(bot))