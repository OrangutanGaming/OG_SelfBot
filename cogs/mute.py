from discord.ext import commands
import json, os

cDir = os.path.dirname(os.path.abspath(__file__))
cDir = cDir.replace("\\cogs", "")

class Mute():
    def __init__(self, bot):
        self.bot = bot

    # def muteListUpdate(self):
    #     toWrite = {}
    #     for server in self.bot.guilds:
    #         toWrite[str(server.id)] = []
    #         counter = -1
    #         for channel in server.text_channels:
    #             counter += 1
    #             try: value = self.bot.muteList[str(server.id)][counter][str(channel.id)]
    #                 for channelJSON in self.bot.muteList[str(server.id)]:
    #                     if
    #             except: value = "False"
    #             toWrite[str(server.id)].append({
    #                 str(channel.id): "False"
    #             })
    #     with open(f"{cDir}\muteList.json", "w") as muteListFile:
    #         json.dump(toWrite, muteListFile, ensure_ascii=False, indent=4)
    #
    # async def on_ready(self):
    #     self.muteListUpdate()
    #
    # async def on_channel_create(self, channel):
    #     self.muteListUpdate()
    #
    # async def on_channel_delete(self, channel):
    #     self.muteListUpdate()

    @commands.command(aliases=["ignore"])
    async def mute(self, ctx, *, choice = None):
        if not choice:
            await ctx.send("<Mention> <True/False> (Channel)")
            return
        choice = choice.lower().split(" ")
        if choice[0] == "mention":
            if choice[1].lower() == "false": option = "False"
            elif choice[1].lower() == "true": option = "True"
            else: await ctx.send(f"I don't recognise `{choice[1]}`"); return
            try:
                choice[2]
                try:
                    channelID = int(choice[2])
                    self.bot.get_channel(channelID)
                except:
                    await ctx.send("Give the Channel's ID!")
                    return

            except: channelID = ctx.channel.id
            with open(f"{cDir}\muteList.json", "r+") as muteListFile:
                new = json.load(muteListFile)
                new[channelID] = option
                json.dump(new, muteListFile, ensure_ascii=False, indent=4)

        elif choice[0] != "mention":
            return
        await ctx.send("Set")

    async def on_message(self, message):
        if message.mention_everyone:
            with open(f"{cDir}\muteList.json", "r") as muteListFile:
                muteList = json.load(muteListFile)
                muteListFile.close()
            try:
                if muteList[message.channel.id] == "True":
                    await message.channel.ack()
            except KeyError:
                pass

def setup(bot):
    bot.add_cog(Mute(bot))