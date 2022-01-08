import discord
from discord.ext import commands
from discord.utils import get
from core.classes import Cog_Extension
import urllib.request as req
import bs4

url = "https://store.steampowered.com/feeds/newshub/app/1377580/?cc=TW&l=tchinese&snr=1_2108_9__1601"


class soulworker(Cog_Extension):

    @commands.command()
    async def 巴哈(self, ctx):
        await ctx.send('https://forum.gamer.com.tw/B.php?bsn=21911')

    @commands.command()
    async def wiki(self, ctx):
        await ctx.send('https://wikiwiki.jp/soulworker/')

    @commands.command()
    async def 新手(self, ctx):
        await ctx.send('https://forum.gamer.com.tw/C.php?bsn=21911&snA=5423')

    @commands.command()
    async def 勳章(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786039150200619068/786548886436053013/LFNWCrP.png')

    @commands.command()
    async def 稱號(self, ctx):
        await ctx.send('https://docs.google.com/spreadsheets/d/1g7hBQr1wBfR3Gne1UhDb58PDUwRwo3L8jWdMh8XESXs/edit#gid=1287689317')

    @commands.command()
    async def 前置(self, ctx):
        await ctx.send('https://forum.gamer.com.tw/C.php?bsn=21911&snA=5425&tnum=2')

    @commands.command()
    async def AR卡(self, ctx):
        await ctx.send('https://forum.gamer.com.tw/C.php?bsn=21911&snA=5511')

    # @commands.command()
    # async def news(self, ctx):
    #     member = get(ctx.channel.guild.roles, name="靈魂勞工")
    #     request = req.Request(url, headers={
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    #     })
    #     with req.urlopen(request) as response:
    #         data = response.read().decode('utf-8')
    #     root = bs4.BeautifulSoup(data, "html.parser")

    #     title = root.channel.item.find("title")
    #     guid = root.channel.item.find("guid", ispermalink="true")
    #     description = root.channel.item.find("description")
    #     time = root.channel.item.find("pubdate")
    #     author = root.channel.item.find("author")
        
    #     embed = discord.Embed(
    #         title=title.string,
    #         description=f'{time.string[:-6]} By {author.string}',
    #         colour=0xFF2D00
    #     )
    #     embed.add_field(name=guid.string, value=description.string.split(
    #         '" />')[1].replace('<br>', '\n').replace('<img src="', '').replace('" />', ''), inline=True)
    #     enclosure = description.string.split(
    #         '" />')[0].replace('<img src="', '')
    #     embed.set_thumbnail(url=enclosure)
    #     await ctx.send(embed=embed)

    #     if(len(description.string) >= 2000):
    #         await ctx.send(f'此次更新內容較多，請至以下網址觀看完整內容:\n{guid.string}')
    #     else:
    #         await ctx.send(f'📰| {title.string} | {time.string}UTC+0')
    #         await ctx.channel.send(description.string.replace('<br>', '\n').replace('<img src="', '').replace('" />', ''))


def setup(bot):
    bot.add_cog(soulworker(bot))
