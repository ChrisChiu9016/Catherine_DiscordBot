import discord
import datetime
import json
import asyncio
from discord.ext import commands
from core.classes import Cog_Extension
from discord.utils import get
import urllib.request as req
import bs4

url = "https://store.steampowered.com/feeds/newshub/app/1377580/?cc=TW&l=tchinese&snr=1_2108_9__1601"


class task(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

        async def raid():
            await self.bot.wait_until_ready()
            raid_channel = self.bot.get_channel(786039432980856852)
            member = get(raid_channel.guild.roles, name='靈魂勞工')
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M%S')
                now_date = datetime.datetime.now().strftime('%D')
                if now_time == '183000':
                    await raid_channel.send(now_date)
                    await raid_channel.send(f'{member.mention}')
                    await raid_channel.send('盆栽要剪，女王要扁。\n以上。\n')
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)

        async def news():
            # wait for bot
            await self.bot.wait_until_ready()

            # get channel and role
            news_channel = self.bot.get_channel(786040913596121090)
            member = get(news_channel.guild.roles, name='靈魂勞工')

            # request
            request = req.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            })
            with req.urlopen(request) as response:
                data = response.read().decode('utf-8')
            root = bs4.BeautifulSoup(data, "html.parser")
            # get imformation
            title = root.channel.item.find("title")
            guid = root.channel.item.find("guid", ispermalink="true")
            description = root.channel.item.find("description")
            time = root.channel.item.find("pubdate")
            author = root.channel.item.find("author")
            # embed
            embed = discord.Embed(
                title=title.string,
                description=f'{time.string[:-6]} By {author.string}',
                colour=0xFF2D00
            )
            embed.add_field(name=guid.string, value=description.string.split(
                '" />')[1].replace('<br>', '\n').replace('<img src="', '').replace('" />', ''), inline=True)
            enclosure = description.string.split(
                '" />')[0].replace('<img src="', '')
            embed.set_thumbnail(url=enclosure)

            print(f'\n目前偵測最新公告: {title.string}\n')

            # loop
            while not self.bot.is_closed():

                with req.urlopen(request) as response:
                    data = response.read().decode('utf-8')
                root = bs4.BeautifulSoup(data, "html.parser")
                new_title = root.channel.item.find("title")

                if title == new_title:
                    print(f'{datetime.datetime.now()} 沒有新公告')
                    await asyncio.sleep(60)
                else:
                    title = new_title
                    guid = root.channel.item.find("guid", ispermalink="true")
                    description = root.channel.item.find("description")
                    time = root.channel.item.find("pubdate")
                    author = root.channel.item.find("author")
                    """
                    # embed
                    embed = discord.Embed(
                        title=title.string,
                        description=f'{time.string[:-6]}UTC+0 By {author.string}',
                        colour=0xFF2D00
                    )
                    embed.add_field(
                        name=guid.string,
                        value=description.string.split(
                            '" />')[1].replace('<br>', '\n').replace('<img src="', '').replace('" />', ''),
                        inline=True
                    )
                    enclosure = description.string.split(
                        '" />')[0].replace('<img src="', '')
                    embed.set_thumbnail(url=enclosure)
                    """
                    print(f'{datetime.datetime.now()} 發現新公告:{title.string}')

                    if(len(description.string) >= 2000):
                        await news_channel.send(f'{member.mention}\n📰| {title.string} | {time.string}UTC+0\n此次更新內容較多，請至以下網址觀看完整內容:\n{guid.string}')
                    else:
                        await news_channel.send(f'{member.mention}\n📰| {title.string} | {time.string}UTC+0')
                        await news_channel.send(description.string.replace('<br>', '\n').replace('<img src="', '').replace('" />', ''))

                    # await news_channel.send(embed=embed)
                    await asyncio.sleep(60)

        task_raid = self.bot.loop.create_task(raid())
        task_news = self.bot.loop.create_task(news())
        #task_test = self.bot.loop.create_task(test())


def setup(bot):
    bot.add_cog(task(bot))
