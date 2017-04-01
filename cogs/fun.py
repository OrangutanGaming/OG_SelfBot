import discord
from discord.ext import commands
import time
import asyncio
import unicodedata
import cogs.emojis as Emojis
import inflect

class Fun():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        pingT = (after - before) * 1000

        await ctx.message.edit(content="Ping. :ping_pong:")
        await ctx.send(content="Pong. :ping_pong: **{0:.0f}ms**".format(pingT))

    @commands.command()
    async def status(self, ctx, *, status: str):
        status = status.strip("`")
        await self.bot.change_presence(game=discord.Game(name=status))
        await asyncio.sleep(1)
        await ctx.message.edit(content=f"**Playing** {ctx.guild.me.game}")

    @commands.command()
    async def stat_test(self, ctx):
        await self.bot.change_presence(game=None)
        await ctx.message.edit(content="Playing set to None")

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):

        if len(characters) > 15:
            await ctx.send(f"Too many characters ({len(characters)}/15)")
            return

        fmt = "`\\U{0:>08}`: {1} - {2} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{0}>"

        def to_string(c):
            digit = format(ord(c), "x")
            name = unicodedata.name(c, "Name not found.")
            return fmt.format(digit, name, c)

        await ctx.message.edit("\n".join(map(to_string, characters)))

    @commands.command(aliases=["ustatus"])
    async def cstatus(self, ctx, id):
        try: id = int(id)
        except: await ctx.message.edit(content="Type the ID!"); return
        member = discord.utils.get(self.bot.get_all_members(), id=id)
        if not member:
            await ctx.message.edit(content=f"Can't find a user with the ID of {id}")
            return
        await ctx.message.edit(content=f"{str(member)}'s status is: {str(member.status).title()}")

    @commands.command()
    async def profile(self, ctx, *, arg = None):
        if not arg: arg = str(ctx.author)

        Int = arg.isdigit()

        if Int:
            id = int(arg)
            member = discord.utils.get(ctx.guild.members, id=id)

            if not member:
                await ctx.message.edit(content=f"Could not find the user with the ID of `{arg}` "
                                               f"on the server `{ctx.guild.name}`")
                return
        elif not Int:
            # await ctx.send("{0}, {1}".format(arg.split("#")[0], int(arg.split("#")[1])))
            member = discord.utils.get(ctx.guild.members, name = arg.split("#")[0], discriminator = arg.split("#")[1])

            if not member:
                await ctx.message.edit(content=f"Could not find the user `{arg.split('#')[0]}` "
                                               f"on the server `{ctx.guild.name}`")
                return
            id = member.id
        else:
            await ctx.send("Type check not working or float given.")
            return

        embed = discord.Embed(description=f"Profile for {str(member)}", colour=member.colour)
        embed.add_field(name="Profile Link", value=f"<@{id}>")
        await ctx.message.edit(content="", embed=embed)

    @commands.command(aliases=["emojis", "emote", "emotes"])
    async def emoji(self, ctx, emoji: str = None, edit = True):
        if not emoji:
            await ctx.message.edit(content=f"All available emotes are: {Emojis.rEmojis}")
            return
        if not emoji.lower() in Emojis.emojis:
            await ctx.message.edit(content=f"Can't find the emoji `{emoji}`.")
            return
        emoji = emoji.lower()
        final = getattr(Emojis, emoji)
        if edit:
            await ctx.message.edit(content=final)
        else:
            await ctx.send(final)

    @commands.command()
    async def channels(self, ctx):
        channels = []
        for channel in ctx.guild.text_channels:
            channels.append(channel.name.title())
        await ctx.send(", ".join(channels))

    @commands.command()
    async def emojitext(self, ctx, *, text: str = None):
        if not text: await ctx.send("No Text!"); return
        text = text.lower()
        msg = ""
        p = inflect.engine()
        chars = list(text)

        for char in chars:
            Int = char.isdigit()

            if Int:
                msg += f":{p.number_to_words(int(char))}: "
            else:
                msg += f":regional_indicator_{char}: "

        await ctx.message.edit(content=msg)

def setup(bot):
    bot.add_cog(Fun(bot))

# import discord
# user = discord.utils.get(ctx.guild.members, id=80088516616269824)
# if not user:
#     await ctx.send(f"Can't find a user with the ID of {id}")
#     return
# await ctx.send(f"{str(user)}'s status is: {str(user.status).title()}")

