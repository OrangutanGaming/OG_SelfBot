import discord
from discord.ext import commands
import SelfIDs
import cogs.utils.prefix as Prefix
import cogs.emojis as Emojis

startup_extensions = [
    "cogs.fun",
    "cogs.eval",
    "cogs.gens",
    "cogs.botinfos",
    "cogs.hepbot",
    "cogs.ack",
    "cogs.bgt",
    "cogs.clear",
    "cogs.serverinfo",
    "cogs.count"
]

bot = commands.Bot(command_prefix=Prefix.prefixes, description="A Self Bot", max_messages=1000, self_bot=True)
bot.remove_command("help")
bot.blank = "\u200B"


def emojireplacetext(message):
    if not message: return
    try:
        output = message.content
    except:
        print(f"discord.Message obj needed. {type(message)} was given.")
        return

    for emoji in Emojis.emojis:
        if f"[{emoji}]" in output.lower():
            fEmoji = Emojis.emojis[emoji]
            output = output.replace(f"[{emoji}]", fEmoji)

    return output

@bot.event
async def on_ready():
    gamename="with Orangutans \U0001f435"
    await bot.change_presence(game=discord.Game(name=gamename))
    print("Logged in as:")
    print("Name: " + str(bot.user))
    print("ID: " + str(bot.user.id))
    print("Playing", gamename)
    print("Prefixes: " + Prefix.Prefix())

@bot.event
async def on_message(message):
    if message.author.id != bot.user.id:
        return
    if "[" in message.content:
        if not "```" in message.content or not "\u200B" in message.content:
            await message.edit(content=(emojireplacetext(message)))
    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    if after.author.id != bot.user.id:
        return
    if "[" in after.content:
        if not "```" in after.content:
            await after.edit(content=(emojireplacetext(after)))
    await bot.process_commands(after)

@bot.command()
async def load(ctx, extension_name : str):
    try: bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send(bot.blank + "```py\n{}: {}\n```".format(type(e).__name__, str(e)), delete_after=3)
        return
    await ctx.send(bot.blank + "{} loaded.".format(extension_name), delete_after=3)

@bot.command()
async def unload(ctx, extension_name : str):
    bot.unload_extension(extension_name)
    await ctx.send(bot.blank + "{} unloaded.".format(extension_name), delete_after=3)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))

# @bot.event
# async def on_command_error(error, ctx):
#     if isinstance(error, commands.MissingRequiredArgument):
#         print(error)
#     elif isinstance(error, commands.errors.CommandNotFound):
#         print("`{}` is not a valid command".format(ctx.invoked_with))
#     elif isinstance(error, commands.errors.CommandInvokeError):
#         print(error)
#     else:
#         print(error)

bot.run(SelfIDs.token, bot=False)