import discord
from discord import colour
from discord.ext import commands
from core.classes import Cog_Extension

import hentai

class discordHentai(Cog_Extension):
  @commands.command(aliases=['隨機本本','rH'])
  async def randomHentai(self, ctx):
    r_id = hentai.Utils.get_random_id()
    doujin = hentai.Hentai(r_id)
    
    embed=discord.Embed(title=doujin.title, description=r_id, url=doujin.url)
    embed.set_thumbnail(url=doujin.thumbnail)
    embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
    embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(discordHentai(bot))
