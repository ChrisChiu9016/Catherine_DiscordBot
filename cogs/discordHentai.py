import discord
from discord import colour
from discord.ext import commands
from core.classes import Cog_Extension

import hentai


class discordHentai(Cog_Extension):
	#隨機本子		
	#if ctx.invoked_subcommand is None: 檢查是否有參數
	@commands.group(aliases=['h'])
	async def hentai(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("請配合參數使用。")

	@hentai.command()
	async def random(self, ctx):
		r_id = hentai.Utils.get_random_id()
		doujin = hentai.Hentai(r_id)

		embed=discord.Embed(title=str(doujin.title()), description=r_id, url=doujin.url)
		embed.set_thumbnail(url=doujin.thumbnail)
		embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
		embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
		await ctx.send(embed=embed)

	@hentai.command()
	async def id(self, ctx, id:str):
		if(hentai.Hentai.exists(id)):
			doujin = hentai.Hentai(id)
					
			embed=discord.Embed(title=str(doujin.title()), description=id, url=doujin.url)
			embed.set_thumbnail(url=doujin.thumbnail)
			embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
			embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
			await ctx.send(embed=embed)

	@hentai.command()
	async def search(self, ctx, *, params:str):
		count=0
		for doujin in hentai.Utils.search_by_query(params, sort=hentai.Sort.PopularWeek):
			if count < 5:
				embed=discord.Embed(title=str(doujin.title()), description=doujin.id, url=doujin.url)
				embed.set_thumbnail(url=doujin.thumbnail)
				embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
				embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
				await ctx.send(embed=embed)

				count = count + 1

			else: break
			
	@hentai.command()
	async def help(self, ctx):
		await ctx.send("參數一覽:\n    random : 隨機挑選一個本本\n    id : 指定神的語言搜尋\n    search : 根據指定內容搜尋")

def setup(bot):
    bot.add_cog(discordHentai(bot))
