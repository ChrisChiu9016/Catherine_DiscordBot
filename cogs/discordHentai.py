import discord
from discord import colour
from discord.ext import commands
from core.classes import Cog_Extension

import hentai

class discordHentai(Cog_Extension):
	#隨機本子		
	@commands.group(aliases=['rh'])
	async def randomHentai(self, ctx, *, argument: str):
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
		await ctx.send(doujin.image_urls.replace('\'','').replace('[','').replace(']',''))

	#指定本子
	@commands.command(aliases=['hid'])
	async def getHentai(self, ctx, *, id):
		if(hentai.Hentai.exists(id)):
			doujin = hentai.Hentai(id)
            
			embed=discord.Embed(title=str(doujin.title()), description=id, url=doujin.url)
			embed.set_thumbnail(url=doujin.thumbnail)
			embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
			embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
			await ctx.send(embed=embed)
		else:
			ctx.send(f'此ID不存在，請重試。')
	@getHentai.command()
	async def show(self, ctx):
		if(hentai.Hentai.exists(id)):
			doujin = hentai.Hentai(id)
            
			embed=discord.Embed(title=str(doujin.title()), description=id, url=doujin.url)
			embed.set_thumbnail(url=doujin.thumbnail)
			embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
			embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
			await ctx.send(embed=embed)
		else:
			ctx.send(f'此ID不存在，請重試。')
		await ctx.send(doujin.image_urls.replace('\'','').replace('[','').replace(']',''))

def setup(bot):
    bot.add_cog(discordHentai(bot))
