import discord
from discord.ext import commands
import SelfIDs

startup_extensions = [
    "cogs.fun"
]

bot = commands.Bot(command_prefix="[s]", description="A Self Bot", self_bot=True)

@bot.event
async def on_ready():
    gamename="with Orangutans"
    await bot.change_presence(game=discord.Game(name=gamename))
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    print("Playing", gamename)
    print("Prefixes: " + "[s]")

@bot.event
async def on_message(message):
    if message.author.bot and message.author.id != bot.user.id:
        return
    await bot.process_commands(message)

@bot.command()
async def load(ctx, extension_name : str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)), delete_after=3)
        return
    await ctx.send("{} loaded.".format(extension_name), delete_after=3)

@bot.command()
async def unload(ctx, extension_name : str):
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name), delete_after=3)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        print(error)
    elif isinstance(error, commands.errors.CommandNotFound):
        print("`{}` is not a valid command".format(ctx.invoked_with))
    elif isinstance(error, commands.errors.CommandInvokeError):
        print(error)
    else:
        print(error)

bot.run(SelfIDs.token, bot=False)