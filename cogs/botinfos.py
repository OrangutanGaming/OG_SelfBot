from discord.ext import commands
import discord
import SelfIDs
import cogs.utils.prefix as Prefix

class Bot():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["uinfo"])
    async def userinfo(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        if member.status is discord.Status.online:
            status = "<:online:212789758110334977>"
        elif member.status is discord.Status.idle:
            status = "<:away:212789859071426561>"
        elif member.status is discord.Status.do_not_disturb:
            status = "<:do_not_disturb:236744731088912384>"
        else:
            status = "<:offline:212790005943369728>"

        embed = discord.Embed(title=f"User Info for {status}{member}",
                              colour=member.colour)

        avatar_url = member.avatar_url.replace("webp", "png")
        embed.set_thumbnail(url=avatar_url.replace("size=1024", "size=256"))
        embed.set_footer(text=("Account Created at " + member.created_at.strftime("%A %d %B %Y, %H:%M:%S")))
        embed.set_author(name=f"{member}", url=avatar_url, icon_url=avatar_url)

        if member.game:
            embed.add_field(name="Status", value=f"**Playing** {member.game.name}")
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Member Since ",
                        value=member.joined_at.strftime("%A %d %B %Y, %H:%M:%S"))

        roleString = ""
        for role in member.roles:
            if role.name == "@everyone":
                continue
            roleString += role.name + ", "
        roleString = roleString[:-2]

        embed.add_field(name="Roles", value=roleString)

        if member.avatar_url:
            embed.set_image(url=member.avatar_url)
            embed.add_field(name="Avatar URL", value=member.avatar_url)

        await ctx.send(embed=embed)

    # @commands.command()
    # async def info(self, ctx):
    #     server = ctx.message.guild
    #     membObj = server.me
    #     embed = discord.Embed(title="Information on {}".format(self.bot.user.name),
    #                           colour=0xfe8600)
    #     embed.set_image(url=self.bot.user.avatar_url)
    #     embed.set_footer(text=("Bot created at " + self.bot.user.created_at.strftime("%A %d %B %Y, %H:%M:%S")))
    #
    #     embed.add_field(name="ID", value=self.bot.user.id)
    #     embed.add_field(name="Member Since ",
    #                     value=membObj.joined_at.strftime("%A %d %B %Y, %H:%M:%S"))
    #     roleString = ""
    #     for role in membObj.roles:
    #         if role.name == "@everyone":
    #             continue
    #         roleString += role.name + ", "
    #     roleString = roleString[:-2]
    #
    #     embed.add_field(name="Roles", value=roleString)
    #
    #     if self.bot.user.avatar_url:
    #         embed.set_image(url=self.bot.user.avatar_url)
    #         embed.add_field(name="Avatar URL", value=self.bot.user.avatar_url)
    #
    #     embed.add_field(name="Owner", value="OGaming#7135")
    #     embed.add_field(name="Prefixes", value=Prefix.Prefix("`") + "`@OG_Bot`")
    #     embed.add_field(name="GitHub", value="https://github.com/OrangutanGaming/OG_Bot")
    #     embed.add_field(name="Server Count", value=str(len(self.bot.guilds)))
    #
    #     await ctx.message.edit(content="", embed=embed)

    @commands.command(aliases=["sinfo"])
    async def serverinfo(self, ctx):
        server = ctx.message.guild

        embed = discord.Embed(title="Server Info for {}".format(server.name), colour=0xffa500)

        embed.set_image(url=server.icon_url)
        embed.set_footer(text=("Server created at " + server.created_at.strftime("%A %d %B %Y, %H:%M:%S")))

        embed.add_field(name="ID", value=server.id)

        def Roles(server):
            counter = 0
            for role in server.roles:
                if role.name == "@everyone":
                    continue
                counter += 1
            return str(counter)

        def Bots(server):
            count = 0
            for member in server.members:
                if member.bot:
                    count += 1
                else:
                    continue

            return str(count)

        embed.add_field(name="Roles", value=Roles(server))
        embed.add_field(name="Owner", value=server.owner)
        embed.add_field(name="Region", value=server.region)
        embed.add_field(name="Member Count", value=server.member_count)
        embed.add_field(name="Bot Count", value=Bots(server))
        embed.add_field(name="Text Channel Count", value=str(len(server.text_channels)))
        embed.add_field(name="Voice Channel Count", value=str(len(server.voice_channels)))
        embed.add_field(name="Total Channel Count", value=str(len(server.channels)))
        if server.icon_url:
            embed.set_image(url=server.icon_url)
            embed.add_field(name="Avatar URL", value=server.icon_url)

        await ctx.message.edit(content="", embed=embed)


    @commands.command()
    async def member_count(self, ctx):
        await ctx.message.edit(content="`{0.name}` has {0.member_count} members.".format(ctx.guild))

def setup(bot):
    bot.add_cog(Bot(bot))