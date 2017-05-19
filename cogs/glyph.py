from discord.ext import commands
import re
from Naked.toolshed.shell import execute_js

class Glyph():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        content = message.content
        x = (r"?")
        try: x[0]
        except IndexError:
            return
        for code in x:
            execute_js("", "")

def setup(bot):
    bot.add_cog(Glyph(bot))