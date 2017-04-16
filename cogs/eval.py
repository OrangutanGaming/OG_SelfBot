import discord
from discord.ext import commands
import inspect
import io
from contextlib import redirect_stdout
import textwrap, traceback
import argparse
import cogs.utils.formatting as formatting

from sympy import *
import sys
import mpmath
sys.modules["sympy.mpmath"] = mpmath

class Eval():
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    def get_syntax_error(self, e):
        if e.text is None:
            return "```py\n{0.__class__.__name__}: {0}\n```".format(e)
        return "```py\n{0.text}{1:>{0.offset}}\n{2}: {0}```".format(e, "^", type(e).__name__)

    @commands.command()
    async def eval(self, ctx, *, code : str):
        original = ctx.message

        code = code.strip("`")
        python = "{}"
        result = None

        env = {
            "bot": self.bot,
            "ctx": ctx,
            "message": ctx.message,
            "guild": ctx.message.guild,
            "channel": ctx.message.channel,
            "author": ctx.message.author
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await ctx.channel.send(python.format(type(e).__name__ + ": " + str(e)))
            await ctx.message.delete()
            return

        lines = ["```py"]
        lines.append(f">>> {code}")
        lines.append(">>> {}".format(python.format(result)))
        lines.append("```")

        await original.edit(content="\n".join(lines))

    @commands.command(name="exec", aliases = ["ex", "exed"])
    async def _exec(self, ctx, *, body: str):
        env = {
            "bot": self.bot,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "server": ctx.guild,
            "message": ctx.message,
            "_": self._last_result
        }

        env.update(globals())

        body = formatting.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = "async def func():\n{}".format(textwrap.indent(body, "  "))

        try:
            exec(to_compile, env)
        except SyntaxError as e:
            return await ctx.send(self.get_syntax_error(e))

        func = env["func"]
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(self.bot.blank + "```py\n{}{}\n```".format(value, traceback.format_exc()))
        else:
            value = stdout.getvalue()

            if ret is None:
                if value:
                    await ctx.send(self.bot.blank + "```py\n%s\n```" % value)
            else:
                self._last_result = ret
                await ctx.send(self.bot.blank + "```py\n%s%s\n```" % (value, ret))

    @commands.command(aliases=["olve"])
    async def solve(self, ctx, *, equation: str):
        x, y, z = symbols("x y z")
        Return = equation.split("` ")[1].replace(" ", "")
        equation = equation.split("` ")[0].replace("`", "").replace(" = ", " - ").replace("=", "-")
        result = solve(equation, Return)

        lines = ["```py"]
        lines.append(">>> {}".format(equation.replace("-", "=")))
        lines.append(f">>> {result}")
        lines.append("```")

        await ctx.message.edit(content="\n".join(lines))

    @commands.command()
    async def argtest(self, ctx):
        parser = argparse.ArgumentParser()
        parser.add_argument("square", help="display a square of a given number",
                            type=int)
        args = parser.parse_args()
        await ctx.send(args.square ** 2)

    @commands.command()
    async def content(self, ctx):
        await ctx.send(ctx.message.content)

def setup(bot):
    bot.add_cog(Eval(bot))