import discord
from discord import colour
from discord.ext import commands
from core.classes import Cog_Extension

import hentai


class discordHentai(Cog_Extension):
	#隨機本子		
	#if ctx.invoked_subcommand is None: 檢查是否有參數
	@commands.group()
	async def hentai(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("請配合參數使用。")

	@hentai.group()
	async def random(self, ctx, show=""):
		r_id = hentai.Utils.get_random_id()
		doujin = hentai.Hentai(r_id)
		language = str([language.name for language in doujin.language]).replace('\'','').replace('[','').replace(']','').upper()

		embed=discord.Embed(title=str(doujin.title()), description=f'#{r_id} {language}', url=doujin.url, color=0xFF6600)
		embed.set_thumbnail(url=doujin.thumbnail)
		if len(doujin.artist): embed.add_field(name="Artist", value=str([artist.name for artist in doujin.artist]).replace('\'','').replace('[','').replace(']',''), inline=False)
		if len(doujin.parody): embed.add_field(name="Parody", value=str([parody.name for parody in doujin.parody]).replace('\'','').replace('[','').replace(']',''), inline=False)
		if len(doujin.character): embed.add_field(name="Character", value=str([character.name for character in doujin.character]).replace('\'','').replace('[','').replace(']',''), inline=False)
		if len(doujin.tag): embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
		embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
		await ctx.send(embed=embed)

		if show == "show":
				for url in doujin.image_urls:
					await ctx.send(url.replace('\'',''))

	@hentai.group()
	async def id(self, ctx, id:str, show=""):
		if(hentai.Hentai.exists(id)):
			doujin = hentai.Hentai(id)
			language = str([language.name for language in doujin.language]).replace('\'','').replace('[','').replace(']','').upper()

			embed=discord.Embed(title=str(doujin.title()), description=f'#{id} {language}', url=doujin.url, color=0xFF6600)
			embed.set_thumbnail(url=doujin.thumbnail)
			if len(doujin.artist): embed.add_field(name="Artist", value=str([artist.name for artist in doujin.artist]).replace('\'','').replace('[','').replace(']',''), inline=False)
			if len(doujin.parody): embed.add_field(name="Parody", value=str([parody.name for parody in doujin.parody]).replace('\'','').replace('[','').replace(']',''), inline=False)
			if len(doujin.character): embed.add_field(name="Character", value=str([character.name for character in doujin.character]).replace('\'','').replace('[','').replace(']',''), inline=False)
			if len(doujin.tag): embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
			embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
			await ctx.send(embed=embed)

			if show == "show":
				for url in doujin.image_urls:
					await ctx.send(url.replace('\'',''))
					   

	@hentai.command()
	async def search(self, ctx, *, params:str):
		count=0
		for doujin in hentai.Utils.search_by_query(params, sort=hentai.Sort.PopularWeek):
			if count < 5:
				language = str([language.name for language in doujin.language]).replace('\'','').replace('[','').replace(']','').upper()

				embed=discord.Embed(title=str(doujin.title()), description=f'#{doujin.id} {language}', url=doujin.url, color=0xFF6600)
				embed.set_thumbnail(url=doujin.thumbnail)
				if len(doujin.artist): embed.add_field(name="Artist", value=str([artist.name for artist in doujin.artist]).replace('\'','').replace('[','').replace(']',''), inline=False)
				if len(doujin.parody): embed.add_field(name="Parody", value=str([parody.name for parody in doujin.parody]).replace('\'','').replace('[','').replace(']',''), inline=False)
				if len(doujin.character): embed.add_field(name="Character", value=str([character.name for character in doujin.character]).replace('\'','').replace('[','').replace(']',''), inline=False)
				if len(doujin.tag): embed.add_field(name="Tags", value=str([tag.name for tag in doujin.tag]).replace('\'','').replace('[','').replace(']',''), inline=False)
				embed.add_field(name="Pages", value=doujin.num_pages, inline=False)
				await ctx.send(embed=embed)

				count = count + 1
	
			else: break
			 
	@hentai.command()
	async def help(self, ctx):
		await ctx.send("參數一覽:\n    random : 隨機挑選一個本本\n    id : 指定神的語言搜尋\n    search : 根據指定內容搜尋")

def setup(bot):
    bot.add_cog(discordHentai(bot))
