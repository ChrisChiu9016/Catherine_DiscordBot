import discord
from discord.ext import commands
from core.classes import Cog_Extension


class picture(Cog_Extension):

    @commands.command()
    async def 破貓(self, ctx):
        await ctx.send(f'https://cdn.discordapp.com/attachments/625206991928688690/786936948739932180/procat.jpg')

    @commands.command()
    async def 好耶(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786939055849734154/nice.jpg')

    @commands.command()
    async def 星爆(self, ctx):
        await ctx.send('https://media.discordapp.net/attachments/786026725968314392/792370818633564190/unnamedsadasdasdas.png?width=600&height=603')

    @commands.command(aliases=['스타버스트스트림'])
    async def 星爆氣流斬(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938817022132225/fast.gif')

    @commands.command()
    async def 哈洽馬(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938861686358016/hachama.png')

    @commands.command()
    async def WTM(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938901134442536/WTM.gif')

    @commands.command()
    async def 狗幹(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938962245451807/re0dog.gif')

    @commands.command()
    async def 賤人(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938770753585202/bitch.jpg')

    @commands.command(aliases=['混帳'])
    async def 渾帳(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938340125048852/basterd.jpg')

    @commands.command()
    async def 戲劇化(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938551282696192/dramatic.png')

    @commands.command()
    async def 復活(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/786628336142123048/-7Q5-fjgpZlT3cSu0-g4.png')

    @commands.command()
    async def 東方(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/786628625154703410/3cfca3ecbbe295ae67c40fe900328f68.png')

    @commands.command()
    async def 廚(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/786628907255857223/ae206e9343a1b318848434e84b2755ba.png')

    @commands.command(aliases=['gura', 'a'])
    async def shark(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/625206991928688690/786938431103565844/shark.gif')

    @commands.command()
    async def 這些機會(self, ctx):
        await ctx.send('https://cdn2.ettoday.net/images/2461/2461955.jpg')

    @commands.command()
    async def peko(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/786992749064880188/tenor.gif')

    @commands.command()
    async def 屁股(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786582221058342953/786993845224472586/image0.jpg')

    @commands.command()
    async def padoru(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786031651024666634/786995197585260554/1512462527_padoru_padoru.gif')

    @commands.command()
    async def 閉嘴(self, ctx):
        await ctx.send('https://truth.bahamut.com.tw/s01/201805/7b00e066363758793411ec9435fd6dca.PNG?w=1000')

    @commands.command()
    async def 血流成河(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/787319206105841685/b31efa0d0273409637d09443032250ab.png')

    @commands.command()
    async def 盆栽要剪(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/787320049433706506/o8jcBFu.png')

    @commands.command()
    async def 怎麼這樣(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/787371967526338560/unknown.png')

    @commands.command()
    async def 好宅喔(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/788453648975790092/bTLrRPg.png')

    @commands.command()
    async def 起床(self, ctx, member: discord.Member, *, reason=None):
        url = 'https://cdn.discordapp.com/attachments/786026725968314392/789177728901185576/image0-1.gif'
        await ctx.send(f'{member.mention} {url}')

    @commands.command(aliases=['屁眼派對'])
    async def 屁眼(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/786026725968314392/789481200019439666/5fe60090a7ad6982.gif")

    @commands.command()
    async def 騙人的吧(self, ctx):
        await ctx.send('https://truth.bahamut.com.tw/s01/201609/47eb58a327c095b5a80512e8e4720bf3.PNG')

    @commands.command()
    async def 開扁(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786026725968314392/790293422052605971/70f9be68b01e7fa291717f53ab6e853d.png')

    @commands.command()
    async def 幹你娘(self, ctx):
        await ctx.send('https://i.imgur.com/9qEOe3T.jpg')

    @commands.command()
    async def 上香(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/790950749294034954/da33657252f212ab74eebf168c1fd5db.png')

    @commands.command()
    async def staycool(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786034797049806861/790951321191841832/91ca5cc1a523c635a5a7a88210291d2c.JPG')

    @commands.command()
    async def 憲哥(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786026725968314392/792042298245513246/SPOILER_58RrBdN.jpg')

    @commands.command()
    async def 私(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786031651024666634/792367106770731008/image0.jpg')

    @commands.command()
    async def mic(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786026725968314392/793094430499930142/unknown.png')

    @commands.command()
    async def 吃瓜(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786026725968314392/793097057068908574/VytRssC.jpg')

    @commands.command()
    async def ㄩㄇ(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786026725968314392/795960563124797440/unknown.png')

    @commands.command()
    async def 台女(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/786026725968314392/801032924467822622/776237272017928202.png')


def setup(bot):
    bot.add_cog(picture(bot))
