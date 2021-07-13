import discord
from discord import colour
from discord.ext import commands
from core.classes import Cog_Extension

import hentai

class discordHentai(Cog_Extension):
	#隨機本子		
	@commands.group(aliases=['rh'])
	async def randomHentai(self, ctx):
		if ctx.invoked_subcommand is None:
			r_id = hentai.Utils.get_random_id()
			doujin = hentai.Hentai(r_id)

			embed=discord.Embed(title=str(doujin.title()), description=r_id, url=doujin.url)
			embed.set_thumbnail(url=doujin.thumbnail)
			embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
			embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
			await ctx.send(embed=embed)

	@randomHentai.command()
	async def show(self, ctx):
		r_id = hentai.Utils.get_random_id()
		doujin = hentai.Hentai(r_id)

		embed=discord.Embed(title=str(doujin.title()), description=r_id, url=doujin.url)
		embed.set_thumbnail(url=doujin.thumbnail)
		embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
		embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
		await ctx.send(embed=embed)
		for url in doujin.image_urls:
			await ctx.send(url)

	#指定本子
	@commands.group(aliases=['hid'])
	async def getHentai(self, ctx, id:int):
		await ctx.send('請指定參數:simple/show')
	@getHentai.command(aliases=['s'])
	async def simple(self, ctx):
		if ctx.invoked_subcommand is None:
			if(hentai.Hentai.exists(id)):
				doujin = hentai.Hentai(id)
				
				embed=discord.Embed(title=str(doujin.title()), description=id, url=doujin.url)
				embed.set_thumbnail(url=doujin.thumbnail)
				embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
				embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
				await ctx.send(embed=embed)
				for url in doujin.image_urls:
					await ctx.send(url)
			else:
				ctx.send(f'此ID不存在，請重試。')
	@getHentai.command()
	async def show(self, ctx):
		if ctx.invoked_subcommand is None:
			if(hentai.Hentai.exists(id)):
				doujin = hentai.Hentai(id)
				
				embed=discord.Embed(title=str(doujin.title()), description=id, url=doujin.url)
				embed.set_thumbnail(url=doujin.thumbnail)
				embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
				embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
				await ctx.send(embed=embed)
				for url in doujin.image_urls:
					await ctx.send(url)
			else:
				ctx.send(f'此ID不存在，請重試。')

def setup(bot):
    bot.add_cog(discordHentai(bot))
