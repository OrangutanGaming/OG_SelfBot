from discord.ext import commands
import json, os

cDir = os.path.dirname(os.path.abspath(__file__))
cDir = cDir.replace("\\cogs", "")

pingBlacklist = [
    215310608789143552, # RSB-Veteran
    290955609744867328, # Warchat-Raiding
    176597325249118208, # Frozenballz-GenAnnounce
    164832838087081984 # Q-Raids
]

class Mute():
    def __init__(self, bot):
        self.bot = bot

    def muteListAdd(self, channelID: str, keyword: str, everyone = False):
        with open(self.bot.muteListDir, "r+") as muteListData:
            muteListDecoded = json.load(muteListData)
        channelID = str(channelID)
        keyword = str(keyword)
        muteListToWrite = muteListDecoded
        try:
            muteListToWrite[channelID]
            # TODO Add list of keywords (There's already a keyword saved)
        except NameError:
            pass

        if not everyone:
            muteListToWrite[channelID] = keyword
        else:
            muteListToWrite[channelID] = "everyone" # When List of keywords added, will add everyone and here.
            # on_message checks if it's 'everyone'

        json.dump(muteListData, muteListToWrite)

        return True

    @commands.command(aliases=["ignore"], enabled=False)
    async def mute(self, ctx, *, choice = None):
        if not choice:
            await ctx.send("<Mention> <True/False> (ChannelID)")
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
            with open(f"{cDir}\muteList.json", "w+") as muteListFile:
                new = json.load(muteListFile)
                new[channelID] = option
                json.dump(new, muteListFile, ensure_ascii=False, indent=4)

        elif choice[0] != "mention":
            await ctx.send("`s.mute`")
            return
        await ctx.send("Set")

    async def on_message(self, message):
        if "@everyone" in message.clean_content or "@here" in message.clean_content:
            if message.channel.id in pingBlacklist:
                await message.ack()
            # with open(f"{cDir}\muteList.json", "r") as muteListFile:
            #     muteList = json.load(muteListFile)
            # try:
            #     if muteList[message.channel.id] == "True":
            #         await message.channel.ack()
            # except KeyError:
            #     pass

    # async def on_ready(self):
    #     with open(f"{cDir}/muteList.json", "r"):
    #         pass

def setup(bot):
    bot.add_cog(Mute(bot))