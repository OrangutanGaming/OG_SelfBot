from discord.ext import commands

class Gens():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["countuser", "countusers"])
    async def countu(self, ctx, option : str, value):
        if not option:
            await ctx.message.edit(content="Options missing")
            return

        option = option.lower()

        if option == "disc" or option == "discrim":
            option = "discriminator"

        output = ", ".join(str(x) for x in self.bot.users if getattr(x, option) == value)

        if not output: output = f"There are no members with the {option.title()} of {value}"
        else: output = f"All members with the {option.title()} of `{value}` on the same servers as `{self.bot.user}`: " + "```" + output + "```"

        await ctx.message.edit(content=output)

    @commands.command(aliases = ["countserver", "countservers"])
    async def counts(self, ctx, option: str, *, value):
        if not option:
            await ctx.message.edit(content="Options missing")
            return

        option = option.lower()

        output = ", ".join(x.name + "({})".format(x.id) for x in self.bot.guilds if getattr(x, option) == value)

        if not output: output = f"There are no servers with the {option.title()} of {value}"
        else: output = f"All servers with the {option.title()} of {value} that `OGaming#7135` is part of: " + "```" + output + "```"

        await ctx.message.edit(content=output)


def setup(bot):
    bot.add_cog(Gens(bot))

# x.name for x in bot.users if x.discriminator == '0001'