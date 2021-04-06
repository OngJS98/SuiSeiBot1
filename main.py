import discord
import os
import random
import re
from datetime import datetime,time,timedelta
from keep_alive import keep_alive


client = discord.Client() 

rolldice = ["rolldice", "Rolldice", "ROLLDICE","骰子"]
dice_number = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]

#change soon
food = ["今日は何を食べる","我今天要吃什麼好"]

foodtype = ["推薦什麼餐點"]
foodtypeans = ["西餐","中餐","日式料理","便利店","速食店","你今天節食吧(,,・ω・,,),","紅蘿蔔以外的都好(,,・ω・,,),"]


foodbld = ["統一超商","全家","OK超商","萊爾富","義美"]
foodk = ["肯德基","麥當勞","漢堡王","赛百味"]
foodj = open('foodjapan.txt','r').readline().split(',')
foodc = open('foodcn.txt','r').readline().split(',')
foodw = open('foodwestern.txt','r').readline().split(',')


#打招呼
suichan = ["すいちゃん", "星姐", "星姊", "星街" ,"彗醬", "彗彗","星街彗星", "星街すいせい", "すいせい","すいすい"]


ohayo = ["おはよ", "早安", "おはいよ", "早上好"]

konnichiwa = ["こんにちは","午安"]
suikonnichiwa = ["こんにちは <:sui_wink2:758194434185363496>","こんにちは <:sui_wink1:758194355147374592>"]

oyasumi = ["おやすみ","晚安"]
konbanha = ["こんばんは","晚上好"]

suiohayo = ["おはよ〜٩(๑❛ᴗ❛๑)و"]
suioyasumi = ["おやすみ!"]
suikonbanha = ["こんばんは~"]

kkawaii = ["今日もかわいい","今天也很可愛"]
#Ans
futou = ["斧あげる","給你斧頭","給妳斧頭"]
suifutou = ["やっはり斧は最高！"]

ILY = ["我愛你","我愛妳","愛してる","愛してるう"]
suithx = ["ありがとう<:sui_wink1:758194355147374592>"]

enderman = ["後ろエンダーマン","後面有終界使者"]
suienderman = ["あああああ来るな"]

nodo = ["喉は大事です","喉嚨很重要"]
replynodo = ["そうですね～"]

utau = ["歌"]
umai = ["うまい","上手","好聽"]

shotacon = ["ショタコン","正太控"]
shonencon = ["少年コン","少年控"]

bu = ["不"]

kyoumo = ["<:z_sui_3:757619039420809407>", "<:z_sui_2:757619141044731986>",
    "<:z_sui_1:757619211299193031>"]

kyoumo1 = ["<:z_sui_3:757619039420809407>","<:z_sui_2:757619141044731986>","<:z_sui_1:757619312361209889>"]


wife = ["我婆"]
waifu = ["waifu","wife","婆",]
me = ["我","me"]
me1 = ["我和"]
me2 = ["和我"]

marr = ["結婚"]
marr1 = ["結婚しよ","結婚"]

#otsumachi = ["<:x_otsumati:758363113879109692>"]
fbkmikata = ["仲間になるから","我會當妳同伴的","我會當你的同伴"]
fbkmikataAns = ["でも白上、信じられないな…<:sui_FBK:757621922774122547>"]

@client.event
async def on_ready():
  print('login testing {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
	  return

  msg = message.content

  #utc timezone to timenow(MY/TW timezone)
  
  timenow1 = datetime.now() + timedelta(hours = 8)
  timenow2 = timenow1.time()

  #if msg.startswith("test"):
    #await message.channel.send("hi")
  
  #testing delete message
  if msg.startswith("suitest!"):
      smsg = msg
      await message.channel.purge(limit = 1)
      await message.channel.send("**"+smsg+"**")

  #ss! (#頻道) // (想發的信息)
  if msg.startswith("ss!"):
    #channeltestingA = client.get_channel(757577056023478353)
    ctt = msg.replace("ss!","")
    cttA = ctt.split("//")[0]
    cttAA = int(re.search(r'\d+', cttA).group())
    channelAA = client.get_channel(cttAA)
    cttA1 = str(cttA)
    cttB = ctt.replace(cttA1,"")
    cttC = cttB.replace("//","")
    await channelAA.send(cttC)

  #if msg == "s!time now":
    #await message.channel.send(timenow)

  if (message.channel.id == 757943406247804978):
    if all(word in msg for word in kyoumo):
      await message.add_reaction("<:sui_kira:757308892194799837>")
      await message.add_reaction("<:sui_hihihi:757308892307914879>")
      await message.add_reaction("<a:sui_singing:780032205153501205>")
      await message.add_reaction("<:sui_heart:773140341913944094>")


    if all(word in msg for word in kyoumo1):
      await message.add_reaction("<:sui_kira:757308892194799837>")
      await message.add_reaction("<:sui_hihihi:757308892307914879>")
      await message.add_reaction("<a:sui_singing:780032205153501205>")
      await message.add_reaction("<:sui_heart:773140341913944094>")


  if (message.channel.id != 757302697425895505) and (message.channel.id != 774167144791408641) and (message.channel.id != 774167182924972032) and (message.channel.id != 817019027750387786):
    for word in suichan:
      if msg.startswith(word):
        #星姐早安
        if any(word in msg for word in ohayo):
          await message.channel.send(message.author.mention + "さん" + " " +  random.choice(suiohayo) + " ☀️")

        #星姐午安
        elif any(word in msg for word in konnichiwa):
          await message.channel.send(message.author.mention + "さん" + " " + random.choice(suikonnichiwa))

        #星姐晚安
        elif any(word in msg for word in oyasumi):
          await message.channel.send(message.author.mention + "さん" + " " + random.choice(suioyasumi)+"<:sui_sleep:757619541969862756>")

        #星姐斧頭
        elif any(word in msg for word in futou):
          if len(msg) <= 10:
            await message.channel.send("やっはり斧は最高! <:x_sui_hehe:757619481186140230><:x_ono_right:757307835515273266>")

        #正太控
        elif any(word in msg for word in shotacon):
          if len(msg) <= 10:
            if any(word in msg for word in bu):
              break
            else:
              await message.channel.send("は？殺す<:suii_angry:757308892882534400> ")

        #少年控
        elif any(word in msg for word in shonencon):
          if len(msg) <= 10:
            if any(word in msg for word in bu):
              break
            else:
              await message.channel.send("そうそうそう、少年コンですよすいちゃんは<:sui_hihihi:757308892307914879> ")

        #星姐我愛你
        elif any(word in msg for word in ILY):
          await message.channel.send(random.choice(suithx))

        #星姐我會當你的同伴
        elif any (word in msg for word in fbkmikata):
          await message.channel.send(random.choice(fbkmikataAns))

        #星姐背後有安德
        elif any(word in msg for word in enderman):
          await message.channel.send(random.choice(suienderman)+"!!!"+"<:sui_scare:758194509280051220> ")

        #星姐我愛你
        elif any(word in msg for word in ILY):
          await message.channel.send(random.choice(suithx))
          
        #星姐骰子
        elif any (word in msg for word in rolldice):
          await message.channel.send(random.choice(dice_number))

        #星姐和我結婚（醒）
        elif any(word in msg for word in me):
          if any(word in msg for word in marr):
            if len(msg) <= 9:
              if any(word in msg for word in bu):
                break
              else:
                await message.add_reaction("<:wake:800722537188163585>")
                #await message.channel.send('無茶')
                await message.channel.send(file=discord.File(r'MUCHA.mp3'))
                break   


          if any(word in msg for word in waifu):
            if len(msg) <= 9:
              if any(word in msg for word in bu):
                break
              else:
                await message.add_reaction("<:wake:800722537188163585>")
                break  

        #星姐推薦什麼餐點
        elif any (word in msg for word in foodtype):
          A = random.choice(foodtypeans)

          if A == "西餐":
            await message.channel.send(A +"的"+ random.choice(foodw))
            break
          if A == "中餐":
            await message.channel.send(A +"的"+ random.choice(foodc))
            break
          if A == "日式料理":
            await message.channel.send(A +"的"+ random.choice(foodj))
            break
          if A == "便利店":
            await message.channel.send(random.choice(foodbld)+"的餐點感覺不錯")
            break
          if A == "速食店":
            await message.channel.send("去"+ random.choice(foodk)+"看看吧")
            break

          else:
            await message.channel.send(A)
            break

        #星姐幫我選擇:_;_
        if msg.startswith(word+("幫我選擇")):
          s1 = msg.split(':')[1]
          s2 = s1.split(';')
          #await message.channel.send(random.choice(s2))
          await message.channel.send('<:suii_think:757307874027241542>')
          await message.channel.send("すいちゃん為你挑選的是："+" " + random.choice(s2) + " " + "<:sui_point:814791810606039060>")


        elif msg.startswith(word+("推薦什麼中餐")):
          await message.channel.send(random.choice(foodc))

        elif msg.startswith(word+("推薦什麼西餐")):
          await message.channel.send(random.choice(foodw))

        elif msg.startswith(word+("推薦什麼日式料理")):
          await message.channel.send(random.choice(foodj))

        elif msg.startswith(word+("推薦什麼便利店")):
          await message.channel.send(random.choice(foodbld))

        elif msg.startswith(word+("推薦什麼速食店")):
          await message.channel.send(random.choice(foodk))

  #lock 星の彼方
  if (message.channel.id != 817019027750387786):

    #timecheck
    if msg == "sttime":
      #await message.channel.send(time(4,00))
      #await message.channel.send(time(13,00))
      await message.channel.send(timenow1)

    #if any(word in msg for word in ohayo):
    #ohayo = ["おはよ","早安","おはいよ,"早上好"]
    if msg == "おはよ":
      if time(4,00) <= timenow2 <= time(12,00):
        await message.add_reaction("<:_ohamati:758468919320903701>")
      else: 
        await message.add_reaction("<:sui_wtf:793109764358930462>")

    if msg == "早安":
      if time(4,00) <= timenow2 <= time(12,00):
        await message.add_reaction("<:_ohamati:758468919320903701>")
      else: 
        await message.add_reaction("<:sui_wtf:793109764358930462>")
    if msg == "おはよう":
      if time(4,00) <= timenow2 <= time(12,00):
        await message.add_reaction("<:_ohamati:758468919320903701>")
      else: 
        await message.add_reaction("<:sui_wtf:793109764358930462>")
    if msg == "早":
      if time(4,00) <= timenow2 <= time(12,00):
        await message.add_reaction("<:_ohamati:758468919320903701>")
      else: 
        await message.add_reaction("<:sui_wtf:793109764358930462>")
    if msg == "早上好":
      if time(4,00) <= timenow2 <= time(12,00):
        await message.add_reaction("<:_ohamati:758468919320903701>")
      else: 
        await message.add_reaction("<:sui_wtf:793109764358930462>")
    
    #gudnight
    if msg == "おやすみ":
      await message.add_reaction("<:sui_sleep:757619541969862756>")
    if msg == "晚安":
      await message.add_reaction("<:sui_sleep:757619541969862756>")
    
    
    #おはまちreaction
    if msg.startswith("<:_ohamati:758468919320903701>"):
      await message.add_reaction("<:x_sui_hehe:757619481186140230>")
      await message.add_reaction(":_ohamati:758468919320903701>")

    #おつまちreaction
    if msg.startswith("<:x_otsumati:758363113879109692>"):
      await message.add_reaction("<:sui_sleep2:759107119462088724>")
      await message.add_reaction("<:x_otsumati:758363113879109692>")
  
  #yoshi emote in bot channel
  if (message.channel.id == 815181832386773002):
    if msg == "<:x_yoshi:757308891980759040>":
      await message.add_reaction("<:sui_yada:757635800325292134>")
  
  #hoshimachi
  if (message.channel.id == 757580448661766214):
    if msg.startswith("星待ち"):
        await message.add_reaction("<a:sui_shock:780032205581320222>")
        await message.add_reaction("<:sui_onekai:803000295729790986>")

keep_alive()

client.run(os.getenv('TOKEN')) 

