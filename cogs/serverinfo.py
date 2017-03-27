from discord.ext import commands
import discord

class ServerInfo():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["rolecount"])
    async def rolec(self, ctx, role: discord.Role = None, list = False, mention = False):
        online = 0
        if not role:
            await ctx.message.edit(content="You must specify a role")
            return

        if not role:
            await ctx.message.edit(content=f"Can't find the role {role}")
            return

        counter = len(role.members)
        for member in role.members:
            if member.status is discord.Status.online or member.status is discord.Status.idle:
                online += 1

        await ctx.message.edit(content=f"There are {counter} people with the role `{role.name}`. {online} are online.")

        if list:
            names=[]
            if mention: names = ", ".join(user.mention for user in role.members)
            else: names = ", ".join(f"`{str(user)}`" for user in role.members)

            await ctx.send(f"Their names are: {names}")

def setup(bot):
    bot.add_cog(ServerInfo(bot))