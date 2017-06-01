import discord
from discord.ext import commands
import time
import asyncio
import unicodedata
import cogs.emojis as Emojis
import cogs.glyphs as Glyphs
import inflect
import upsidedown
import datetime
from collections import Counter

class Fun():
    def __init__(self, bot):
        self.bot = bot

    def texttoemoji(self, text: str = None):
        if not text:
            return
        text = text.lower()
        msg = ""
        p = inflect.engine()
        chars = list(text)

        for char in chars:

            if char.isdigit():
                msg += f"{char}\u20e3"
            elif char.isalpha():
                msg += f":regional_indicator_{char}:"
                # " ".join(["   " if x==" " else ":regional_indicator_{}:".format(x) for x in "hm hm"])
            elif char == " ":
                msg += "   "
            else:
                msg += char

        return msg

    def upsidedown(self, text: str):
        return upsidedown.transform(text)

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
            await ctx.send(self.bot.blank + f"Too many characters ({len(characters)}/15)")
            return

        fmt = "`\\U{0:>08}`: {1} - {2} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{0}>"

        def to_string(c):
            digit = format(ord(c), "x")
            name = unicodedata.name(c, "Name not found.")
            return fmt.format(digit, name, c)

        await ctx.message.edit("\n".join(map(to_string, characters)))

    @commands.command(aliases=["ustatus"])
    async def cstatus(self, ctx, id=None):
        if not id: await ctx.message.edit(content="Type the ID!"); return
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
            # await ctx.send(self.bot.blank + "{0}, {1}".format(arg.split("#")[0], int(arg.split("#")[1])))
            member = discord.utils.get(ctx.guild.members, name = arg.split("#")[0], discriminator = arg.split("#")[1])

            if not member:
                await ctx.message.edit(content=f"Could not find the user `{arg.split('#')[0]}` "
                                               f"on the server `{ctx.guild.name}`")
                return
            id = member.id
        else:
            await ctx.send(self.bot.blank + "Type check not working or float given.")
            return

        embed = discord.Embed(description=f"Profile for {str(member)}", colour=member.colour)
        embed.add_field(name="Profile Link", value=f"<@{id}>")
        await ctx.message.edit(content="", embed=embed)

    @commands.command(aliases=["emojis", "emote", "emotes"])
    async def emoji(self, ctx, emoji: str = None, edit = True):
        if not emoji:
            allEmojis = "`"+"`, `".join(Emojis.emojis.keys())+"`"
            await ctx.message.edit(content=f"All available emotes are: {allEmojis}")
            return
        if not emoji.lower() in Emojis.emojis:
            await ctx.message.edit(content=f"Can't find the emoji `{emoji}`.")
            return
        emoji = emoji.lower()
        final = Emojis.emojis[emoji]
        if edit:
            await ctx.message.edit(content=final)
        else:
            await ctx.send(final)

    @commands.command()
    async def channels(self, ctx):
        channels = []
        for channel in ctx.guild.text_channels:
            channels.append(channel.name.title())
        await ctx.message.edit(content=self.bot.blank + f"All text channels on the server "
                                                        f"`{ctx.guild.name}`: `" + "`, `".join(channels) + "`")

    @commands.command()
    async def roles(self, ctx):
        roles = []
        for role in ctx.guild.roles:
            roles.append(role.name)
        await ctx.message.edit(content=self.bot.blank + f"All roles on the server `{ctx.guild.name}`: " + "`" + "`, `".join(roles)+"`")

    @commands.command()
    async def emojitext(self, ctx, *, text: str = None):

        msg = self.texttoemoji(text)

        if not msg:
            await ctx.send(self.bot.blank + "No Text!")
            return

        await ctx.message.edit(content=msg)

    @commands.command(enabled=False)
    async def react(self, ctx, channel: discord.TextChannel = None, id: int = None, *, text: str = None):
        if not channel:
            await ctx.send(self.bot.blank + "No Channel")
            return
        if not id:
            await ctx.send(self.bot.blank + "No Message ID")
            return
        if not text:
            await ctx.send(self.bot.blank + "Text?")

        message = channel.get_message(id)

        msg = self.texttoemoji(text)
        if not msg:
            await ctx.send(self.bot.blank + "No `msg` var")

        return

    @commands.command(name="upsidedown")
    async def _upsidedown(self, ctx, *, text: str):
        await ctx.send(self.upsidedown(text))

    @commands.command()
    async def quick(self, ctx, *, message = None):
        if not message: return
        message = message.strip("`")
        if "@" in message:
            pass
        msg = await ctx.send(message)
        await ctx.message.delete()
        await msg.delete()

    @commands.command()
    async def quick_mention(self, ctx, id = None):
        if not id or not id.isdigit():
            return
        id = int(id)
        user = self.bot.get_user(id)
        if not user:
            await ctx.message.edit(content="Can't find that user")
            return
        msg = await ctx.send(user.mention)
        await ctx.message.delete()
        await msg.delete()

    @commands.command(aliases=["picture", "photo"])
    async def pic(self, ctx, *, url):
        embed = discord.Embed(title="Picture", url=url)
        embed.set_image(url=url)

        try: await ctx.message.edit(content="", embed=embed)
        except: await ctx.send("Can't find that link.")

    @commands.command(aliases=["mutualguilds", "mutualg", "mutuals"])
    async def mutualservers(self, ctx, user: discord.User = None, list = False):
        if not user:
            await ctx.send("Give the user!")
            return

        profile = await user.profile()
        amount = len(profile.mutual_guilds)
        embed = discord.Embed(title=f"Amount of mutual guilds for {user}", description=f"Amount of mutual guilds with "
                                                                                       f"{user.mention}")
        embed.add_field(name="Mutual Guilds", value=str(amount))
        if list:
            listGuilds = ", ".join(x.name for x in profile.mutual_guilds)
            embed.add_field(name="List of Mutual Guilds", value=listGuilds)
        embed.set_footer(text=("Mutual Guilds since " + datetime.datetime.utcnow().strftime("%A %d %B %Y at %H:%M:%S")))

        await ctx.send(embed=embed)

    # @commands.command()
    # async def highestmutual(self, ctx):
    #     top = ["None", 0]
    #     for member in self.bot.get_all_members():
    #         profile = await member.profile()
    #         amount = len(profile.mutual_guilds)
    #
    #         if amount > top[1]:
    #             top = [str(member), amount]
    #
    #         elif amount == top[1]:
    #             pass
    #
    #     await ctx.send(f"The person with the most mutual guilds with {self.bot.user} is {top[0]} at {top[1]}")

    @commands.command(aliases=["mutualhighest", "highestmutuals", "mutualleaderboard"])
    async def highestmutual(self, ctx):
        try: await ctx.message.add_reaction("\u2705")
        except discord.Forbidden: pass

        members = Counter(str(m).replace("`", "\\`") for m in self.bot.get_all_members() if m.bot is False)
        top = members.most_common(11)[1:] # Remove Myself
        result = []
        for index, (member, count) in enumerate(top, 1):
            if index != 10:
                result.append("{}\u20e3: {} ({} servers)".format(index, member, count))
            else:
                result.append("\U0001f51f: {} ({} servers)".format(member, count))

        message = "\n".join(result)

        await ctx.send("Leaderboard for mutual servers\n" + message)
        await ctx.message.delete()

    @commands.command(aliases=["glyphs"])
    async def glyph(self, ctx, *, glyph: str = None):
        if not glyph:
            allGlyphs = "`" + "`, `".join(Glyphs.glyphs.keys()) + "`"
            await ctx.send(content=f"All available glyphs are: {allGlyphs}")
            return
        if not glyph.upper() in Glyphs.glyphs:
            await ctx.send(content=f"Can't find the glyph `{glyph}`.")
            return
        glyph = glyph.upper()
        url = Glyphs.glyphs[glyph]

        embed = discord.Embed(title=f"{glyph.upper()}")
        embed.set_image(url=url)

        await ctx.send(embed=embed)

    @commands.command()
    async def charinfo(self, ctx, *, characters: str):
        """Gives unicode info on an emoji."""

        if len(characters) > 15:
            await ctx.send(self.bot.blank + f"Too many characters ({len(characters)}/15)")
            return

        fmt = "`\\U{0:>08}`: {1} - {2} \N{EM DASH} <http://www.fileformat.info/info/unicode/char/{0}>"

        def to_string(c):
            digit = format(ord(c), "x")
            name = unicodedata.name(c, "Name not found.")
            return fmt.format(digit, name, c)

        await ctx.message.edit(content=self.bot.blank + "\n".join(map(to_string, characters)))

def setup(bot):
    bot.add_cog(Fun(bot))

# import discord
# user = discord.utils.get(ctx.guild.members, id=80088516616269824)
# if not user:
#     await ctx.send(self.bot.blank + f"Can't find a user with the ID of {id}")
#     return
# await ctx.send(self.bot.blank + f"{str(user)}'s status is: {str(user.status).title()}")

# blacklist = [
#     "bots",
#     "orangutan",
#     "role troll",
#     "v alliance leader",
#     "itrust",
#     "moderator",
#     "server admin"
# ]
# roles = []
# for role in ctx.guild.roles:
#     if role.hoist and role.name.lower() not in blacklist:
#         roles.append(role.name)
#
# rolesS = "\n".join(roles)
# await ctx.send(f"```{rolesS}```")
#
# for member in ctx.guild.members:
#     for role in member.roles:
#         if role.name in roles:
#             await member.add_roles(discord.utils.get(ctx.guild.roles, name = "Clan Member"))
#
# await ctx.send("Done")
#
# counter = 0
# for server in bot.guilds:
#     try:
#         await server.default_channel("Just to remind you, we have a Discord server: https://discord.gg/duRB6Qg")
#     except discord.Forbidden:
#         counter += 1
# await ctx.send(f"Done. Failed {counter} times.")
#
# for server in bot.guilds:
#     try:
#         async for message in server.default_channel.history(limit=200):
#                 if "Just to remind you, we have a Discord server" in message.content and message.id != ctx.message.id and ctx.author.id == 150750980097441792:
#                     try: await message.delete()
#                     except: continue
#     except:
#         continue