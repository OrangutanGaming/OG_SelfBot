from discord.ext import commands
import discord
import cogs.utils.formatting as formatting

class ServerInfo():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["rolecount"])
    async def rolec(self, ctx, oRole: str = None, list = False, mention = False):

        def status(user):
            if user.status is discord.Status.offline:
                return ":notebook:"
            elif user.status is discord.Status.idle:
                return ":orange_book:"
            elif user.status is discord.Status.online:
                return ":green_book:"
            elif user.status is discord.Status.dnd:
                return ":closed_book:"
            else:
                return ""

        online = 0
        if not oRole:
            await ctx.message.edit(content="You must specify a role")
            return

        oRole = formatting.quote(oRole)
        role = discord.utils.get(ctx.guild.roles, name=oRole)

        if not role:
            await ctx.message.edit(content=f"Can't find the role {oRole}")
            return

        counter = len(role.members)
        for member in role.members:
            if member.status is discord.Status.online or member.status is discord.Status.idle:
                online += 1

        await ctx.message.edit(content=f"There are {counter} people with the role `{role.name}`. "
                                       f"{online} are online or idle.")

        if list:
            names=[]

            for user in role.members:
                uStatus = status(user)
                if mention: names.append(f"{user.mention} {uStatus}")
                else: names.append(f"`{str(user)}` {uStatus}")
            names = ", ".join(names)
            if len(names) > 1981: # msg doesn't breach 2k char limit
                return

            await ctx.send(self.bot.blank + f"Their names are: {names}")

def setup(bot):
    bot.add_cog(ServerInfo(bot))