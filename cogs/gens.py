from discord.ext import commands

class Gens():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def count(self, ctx, option : str, value):
        if not option:
            await ctx.message.edit(content="Options missing")
            return

        option = option.lower()

        if option == "disc":
            option = "discriminator"

        output = ", ".join(x.name for x in self.bot.users if getattr(x, option) == value)

        output = f"All members with the {option.title()} of {value} on the same servers as `OGaming#7135`: " + "```" + output + "```"

        await ctx.message.edit(content=output)


def setup(bot):
    bot.add_cog(Gens(bot))

# x.name for x in bot.users if x.discriminator == '0001'