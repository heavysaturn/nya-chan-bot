import random
from discord.ext import commands
from cogs.base_cog import BaseCog


class Random(BaseCog):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(description='Explains Time Blindness')
    async def nixietime(self, ctx):
        msg = "F(NixieTime) is defined as a function of F that represents the current time plus a non-deterministic random " \
              "value denoting a temporal period.  The exact value of the delta is unknown and changes constantly based on " \
              "fluctuation in the space time continuum and doctor who paradoxes"
        await ctx.channel.send(msg)


def setup(bot):
    cog = Random(bot)
    bot.add_cog(cog)