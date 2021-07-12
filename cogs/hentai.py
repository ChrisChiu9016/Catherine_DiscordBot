import discord
from discord.ext import commands
from core.classes import Cog_Extension

import hentai

class hentai(Cog_Extension):
  @commands.command(aliases=['隨機本本','rH'])
  async def randomHentai(self, ctx):
    await ctx.send(hentai.Utils.get_random_hentai())
