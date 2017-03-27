from discord.ext import commands
import discord
import asyncio

class Clear():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["del", "delete", "wipe"])
    async def clear(self, ctx, amount=100, channel: discord.TextChannel = None, user: discord.User = None):

        if ctx.message.channel.permissions_for(ctx.message.author).manage_messages:

            if not channel:
                channel = ctx.message.channel

            try:

                deleted = await ctx.message.channel.purge(limit=amount, before=ctx.message)
                count = len(deleted)

                if count == 1:
                    tmp = await ctx.send("Deleted {} message".format(count))
                else:
                    tmp = await ctx.send("Deleted {} messages".format(count))
                await asyncio.sleep(3)
                await ctx.channel.delete_messages([tmp, ctx.message])


            except discord.Forbidden as error:
                # await ctx.send("{} does not have permissions".format(self.bot.user.name))
                # TODO Fix ^
                return

        else:
            await ctx.send("You must have the `Manage Messages` permission in order to run that command")

def setup(bot):
    bot.add_cog(Clear(bot))


