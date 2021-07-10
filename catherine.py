# -*- coding: UTF-8 -*-
import discord
import os
from discord.ext import commands
from discord.utils import get
import json
import asyncio
import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
bot = commands.Bot(command_prefix='!')


# Setting `Playing ` status
# await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

# 開機時
@bot.event
async def on_ready():
    print("Bot is Online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="可悲過氣遊戲"))
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename} Loaded')

# Cogs相關


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f'load {extension}')
    await ctx.send(f'加載 {extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'unload {extension}')
    await ctx.send(f'卸除 {extension}')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f'reload {extension}')
    await ctx.send(f'重新加載 {extension}')


# 關鍵字觸發


@bot.event
async def on_message(msg):
    if msg.author != bot.user:
        if '魔眼' in msg.content or '騙人的吧' in msg.content or '紅鼻子' in msg.content or '叛教徒尼可拉斯' in msg.content or 'キリト' in msg.content or '努西' in msg.content or '魔劍瓦蘭姆' in msg.content or 'Dicey Cafe' in msg.content or '西田' in msg.content or '加百列' in msg.content or '索爾提莉娜' in msg.content or '羅妮耶' in msg.content or '媞潔' in msg.content or '溫貝爾' in msg.content or '萊歐斯' in msg.content or '黑暗領域' in msg.content or '渦羅' in msg.content or '薄鹽鱈魚子' in msg.content or '強尼·布萊克' in msg.content or '黑星手槍' in msg.content or '100層' in msg.content or '紅玉宮' in msg.content or '黑鐵宮' in msg.content or '沉睡騎士' in msg.content or '紺野木綿季' in msg.content or '北海鮭魚卵' in msg.content or '羅莎莉雅' in msg.content or '聖龍聯合' in msg.content or '壺井遼太郎' in msg.content or '哥德夫利' in msg.content or 'ordinal scale' in msg.content or 'Augma' in msg.content or '詩乃' in msg.content or 'M-9000' in msg.content or '死槍' in msg.content or '黑卡蒂' in msg.content or '影光G4' in msg.content or 'FN Five-seveN' in msg.content or 'underworld' in msg.content or '劍技連攜' in msg.content or '莉茲貝特' in msg.content or '日蝕' in msg.content or '雙重扇形斬' in msg.content or '斜斬' in msg.content or '奪命擊' in msg.content or '菊岡誠二郎' in msg.content or '明日奈' in msg.content or '艾恩格朗特' in msg.content or '二刀流' in msg.content or '浮游城' in msg.content or '獨行玩家' in msg.content or '攻略組' in msg.content or '提亞貝魯' in msg.content or '有紀' in msg.content or '四方斬' in msg.content or 'switch' in msg.content or '西瓜榴槤機' in msg.content or '星光連流擊' in msg.content or '晶彥' in msg.content or '茅場' in msg.content or '月夜黑貓' in msg.content or '不可破壞物件' in msg.content or '水晶無效' in msg.content or '傳送水晶' in msg.content or '我要殺死你' in msg.content or '尤娜' in msg.content or '鸚鵡螺' in msg.content or '瑛二' in msg.content or '序列征戰' in msg.content or '狗頭人之王伊爾凡格' in msg.content or 'the seed' in msg.content or 'link start' in msg.content or 'Congratulations' in msg.content or '聖堂教會' in msg.content or '最高司祭' in msg.content or '元老院' in msg.content or '這雖然是遊戲 但可不是鬧著玩的' in msg.content or '還要更快' in msg.content or '午夜大衣' in msg.content or '黑衣劍士' in msg.content or '直葉' in msg.content or '西莉卡' in msg.content or '畢娜' in msg.content or '結衣' in msg.content or 'ALO' in msg.content or '守衛精靈' in msg.content or '整合騎士' in msg.content or '須鄉' in msg.content or '奧伯龍' in msg.content or '照燒蛋黃醬披薩' in msg.content or '系統限制' in msg.content or '風林火山' in msg.content or '尤金' in msg.content or '殺人兇手' in msg.content or '微笑棺木' in msg.content or '血盟' in msg.content or '克拉帝爾' in msg.content or '上級修劍' in msg.content or '尤吉歐' in msg.content or '絕劍' in msg.content or '雷根' in msg.content or '牙王' in msg.content or '狂暴補師' in msg.content or '攻略知鬼' in msg.content or '閃光' in msg.content or '雨緣' in msg.content or '金木樨' in msg.content or '劍技' in msg.content or '聖母聖詠' in msg.content or '完全潛行' in msg.content or 'stay cool' in msg.content or 'system call' in msg.content or 'NERvGear' in msg.content or '斷剛聖劍' in msg.content or '封弊者' in msg.content or '科巴茲' in msg.content or '藍薔薇' in msg.content or '希茲克利夫' in msg.content or '骸骨獵殺者' in msg.content or 'SAO' in msg.content or '桐谷' in msg.content or '和人' in msg.content or '桐人' in msg.content or '刀劍' in msg.content or '星爆' in msg.content or 'kirito' in msg.content or '閃耀魔眼' in msg.content or '74層' in msg.content or '十秒' in msg.content or '十六下' in msg.content or '雙刀' in msg.content or '雜燴' in msg.content or '亞絲娜' in msg.content or '克萊茵' in msg.content or '登出' in msg.content or '闡釋者' in msg.content or '逐暗者' in msg.content or '10秒' in msg.content or '16下' in msg.content:
            await msg.add_reaction("👎")
        if '凱薩琳' in msg.content and '串燒' not in msg.content and '聖誕快樂' not in msg.content:
            await msg.channel.send('叫我嗎?')
        if '海葵' in msg.content:
            await msg.channel.send('爽啦')
        if '串燒' in msg.content:
            if '凱薩琳' in msg.content:
                await msg.channel.send('串你媽肛門')
            else:
                await msg.add_reaction("😡")
        if '我不能說' in msg.content:
            await msg.channel.send('https://cdn.discordapp.com/attachments/786582221058342953/786994226634293278/45e9a86e3e5d748ed08047b45e8c72d4.JPG')
        if '村莊' in msg.content:
            await msg.channel.send('https://cdn.discordapp.com/attachments/786026725968314392/792065144939216926/03.png')
    else:
        if '英八' in msg.content:
            await msg.add_reaction("<:PRIMAL_hero:786180780434391040>")
        if '普八' in msg.content:
            await msg.add_reaction("<:PRIMAL:786180162206302228>")
        if '隱匿' in msg.content:
            await msg.add_reaction("<:LAFA:786179635070631966>")
        if '女王' in msg.content:
            await msg.add_reaction("<:lunar:799210734805319680>")

    await bot.process_commands(msg)

bot.run(TOKEN)
