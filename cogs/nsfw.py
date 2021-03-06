from discord.ext import commands
from urllib import parse
import aiohttp

from cogs.base_cog import BaseCog


class Nsfw(BaseCog):
    """Gives functions for the pervs out there ;-)"""

    def __init__(self, bot):
        super().__init__(bot)

    async def fetch_image(self, ctx, channel, randomize: bool = False, tags: list = []):
        guild = ctx.message.guild
        search = "https://konachan.com/post.json?limit=1&tags="
        tag_search = "{} ".format(" ".join(tags))
        if randomize:
            tag_search += " order:random"
        search += parse.quote_plus(tag_search)
        message = await channel.send("Fetching kona image...")
        async with aiohttp.ClientSession() as session:
            async with session.get(search) as r:
                website = await r.json()
        if website != []:
            imageURL = "https:{}".format(website[0].get("file_url")).replace(' ', '+')
            await message.edit(content="Requested by {}\n{}".format(ctx.message.author.mention, imageURL))
        else:
            await message.delete()

    @commands.command(description='Grabs a random picture from Konachan that matches your keywords.')
    @commands.guild_only()
    async def kona(self, ctx, *tags):
        """Grabs a random picture from Konachan that matches your keywords."""
        channel = self.bot.get_channel(329911858423398401)
        if not channel is None:
            try:
                await self.fetch_image(ctx, channel, True, tags)
            except Exception as e:
                await ctx.send(
                    "{}, error```py\n{}: {}\n```".format(ctx.message.author.mention, type(e).__name__, str(e)))


def setup(bot):
    cog = Nsfw(bot)
    bot.add_cog(cog)
