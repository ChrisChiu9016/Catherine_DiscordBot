import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import datetime


class main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'延遲為{round(self.bot.latency*1000)}毫秒')

    @commands.command()
    async def 骰子(self, ctx):
        random.seed(datetime.datetime.now())
        await ctx.send(f'{ctx.author.mention} {random.randint(1, 6)}')

    @commands.command(aliases=['td', 'trpgdice'])
    async def _dice(self, ctx, *, n):
        random.seed(datetime.datetime.now())
        val = random.randint(1, int(float(n)))
        await ctx.send(f'D{n} = {val}')

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def test0(self, ctx):
        emoji = discord.utils.get(self.bot.emojis, name='LAFA')
        await ctx.send(f'{emoji}')


def setup(bot):
    bot.add_cog(main(bot))
