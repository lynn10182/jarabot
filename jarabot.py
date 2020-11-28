import discord
from discord.ext import commands
from random import randint
import datetime
import random
import asyncio
import os

d = datetime.datetime.now()
client = commands.Bot(command_prefix="자라야 ")

@client.event
async def on_ready(): 
    print('start')
    await client.change_presence(
                                         status=discord.Status.online,
                                         activity=discord.Game(name="자라"))  

@client.event
async def on_message(message):  
    author = message.author  
    channel = message.channel  
    content = message.content

    if author.bot:  
        return None 
   
    if content == "자라야":
        await channel.send("왜 불러 용건 없으면 자라")
    
    if content.startswith("자라야뽑기"):
        msg1 = content.split(' ')
        if len(msg1) > 1:
            srp = random.choice(msg1[1:])
        else:
            srp = random.choice()
        embed = discord.Embed(title="뽑기 결과", description=srp)
        await channel.send(embed=embed)
    
    if message.content.startswith("자라야청소"):
        msg = content.split(' ')
        try:
            if int(msg[1]) < 100:
                await message.delete()
                await channel.purge(limit=int(msg[1]))
                await channel.send("다량의 메시지를 삭제했어!")
            else:
                await message.delete()
                await channel.send("100개 이상의 메시지는 삭제할 수 없어!")
        except discord.DiscordException:
            return

    await client.process_commands(message)  
 
@client.command() 
async def 따라해(ctx, *args):
   
    content = ' '.join(args) 
    
    if args == (): 
        await ctx.send("뭘 따라해?")  
        return None

    await ctx.send(content)  

@client.command() 
async def 주사위(ctx, *args):
    await ctx.send(f"데굴데굴... :game_die: **{randint(1, 6)}**")

@client.command()
async def 안녕(ctx, *args):
    await ctx.send(f"{ctx.author.name} 안녕! 가서 자라")

@client.command()
async def 끝말잇기(ctx, *args):
    await ctx.send("이리듐")

@client.command()
async def 스틸(ctx, *args):
    await ctx.send("동물농장 마을의 이장이야! 서버 총관리자지")

@client.command()
async def Steel(ctx, *args):
    await ctx.send("동물농장 마을의 이장이야! 서버 총관리자지")

@client.command()
async def 리니(ctx, *args):
    await ctx.send("이 서버의 부관리자야! 나 자라봇의 창조자이기도 하지!")

@client.command()
async def 오늘(ctx, *args):
    await ctx.send(f"오늘은 {datetime.date.today()} !")

@client.command()
async def 자라(ctx, *args):
    await ctx.send("내 대사다 따라하지 말고 자라")

@client.command()
async def 거북이(ctx, *args):
    await ctx.send("헛소리 하지 말고 자라")

@client.command() 
async def 자니(ctx, *args):
    responses2 = ["*밖이야...*?",
                 "*자는구나...*",
                 "*많이 보고싶다...*",
                 "*보면 연락줘...*",
                 "*곧 생일이지...? 축하해...*",
                 "*우리.. 좋았잖아...*",
                 "*그래... 잘자...*",
                 "*난 너가 많이 그리워...*",
                 "*우리... 그때로 다시 돌아갈 수 있을까...?*"]
    await ctx.send(f"{random.choice(responses2)}")

@client.command()
async def 자는구나(ctx):
    await ctx.send("다음 말이 예상이 가는 건 기분탓?")

@client.command()
async def 잘자(ctx):
    message = await ctx.send("**그만해 역겨워**")
    await asyncio.sleep(2)
    await message.edit(content="자라 ㅋ")
    
@client.command()
async def 우냐(ctx, *args):
    await ctx.send("안울어")

@client.command()
async def 싫어(ctx, *args):
    await ctx.send("나도 싫어")

@client.command()
async def 놀자(ctx, *args):
    await ctx.send("놀지 말고 자라")

@client.command()
async def 뭐해(ctx, *args):
    await ctx.send("알 필요 없으니깐 자라")

@client.command()
async def 죽어(ctx, *args):
    await ctx.send("ㅠㅠ")

@client.command()
async def 꺼져(ctx, *args):
    await ctx.send("그 말 사람한테 하면 주의 받을 수 있다?")

@client.command()
async def 누구(ctx, *args):
    await ctx.send("나? 동물농장을 소개하기 위해 만들어진 세계관 최강의 봇이지! 그러니깐 자라")

@client.command()
async def 호감도(ctx, *args):
    await ctx.send("그딴 거 없으니깐 자라")

@client.command()
async def 바보(ctx):
    message = await ctx.send("**너가 더 바보임**")
    await asyncio.sleep(2)
    await message.edit(content="자라 ㅋ")

@client.command()
async def 규칙(ctx, *args):
    await ctx.send("서버 규칙 채널을 꼭 확인하길 바래!")

@client.command()
async def 역할(ctx, *args):
    await ctx.send("역할을 얻고 싶다면 전직-동아리선택방과 색깔-역할지급방을 이용하면 돼!")

@client.command()
async def 코로나(ctx, *args):
    await ctx.send("우리 서버에는 코로나19 알림봇이 있어! 애용해주길 바래")

@client.command()
async def 어서오세요(ctx, *args):
    await ctx.send("신입 환영 채널이야")

@client.command()
async def 패치내역(ctx, *args):
    await ctx.send("서버-패치내역 채널은 말 그대로 우리 서버의 패치내역이 기록되는 곳이야!")

@client.command()
async def 다과회(ctx, *args):
    await ctx.send("우리 서버의 5인 음성방!")

@client.command()
async def 먹이창고(ctx, *args):
    await ctx.send("우리 서버의 1인 음성방! 고독하게 나만의 시간을 가질 수 있는 방이야")

@client.command()
async def 게시판(ctx, *args):
    await ctx.send("관리자가 서버 공지를 올리는 채널이야!")
 
@client.command()
async def 건의사항(ctx, *args):
    await ctx.send("서버 관리자들에게 서버에 관한 건의를 할 수 있는 채널이야! 캠 키고 깡 춰주세요 이런 건 안받아..^^")

@client.command()
async def 홍보서버(ctx, *args):
    await ctx.send("우리 서버를 홍보하기 위해 만들어진 채널이야")

@client.command()
async def 알콩달콩(ctx, *args):
    await ctx.send("우리 서버의 2인 음성방! :face_with_hand_over_mouth: 둘이서 오붓한 시간을 가질 수 있...")
    await asyncio.sleep(3)
    await message.edit(content="2인 음성방이야! ...자라 ㅋ")

@client.command()
async def 자기소개(ctx, *args):
    await ctx.send("신입들이 자기소개를 하는 방이야! 나이 속이거나 거짓말하면... 혼나는 거 알지?^^")

@client.command()
async def 동아리(ctx, *args):
    await ctx.send("우리 서버에는 다양한 동아리가 있어! 각각의 동아리 역할을 얻고 싶다면 역할 신청방 카테고리를 이용하면 돼")

@client.command()
async def 마을회관(ctx, *args):
    await ctx.send("우리 서버의 메인 채팅방이야")
 
@client.command()
async def 동네회관(ctx, *args):
    await ctx.send("우리 서버의 서브 채팅방이야")

@client.command()
async def 갤러리(ctx, *args):
    await ctx.send("자유롭게 사진을 올릴 수 있는 방이야! 그렇다고 위험한 사진을 올리는 건... 안되는 거 알지?^^")

@client.command()
async def 링크(ctx, *args):
    await ctx.send("우리 서버에서 링크는 (젤다방말고)링크방에 올려야 해! 링크방에서 잡담은 금지인 거 알지?")

@client.command()
async def 일기장(ctx, *args):
    await ctx.send("자유롭게 일기를 쓸 수 있는 채널이야!")

@client.command()
async def 음악(ctx, *args):
    await ctx.send("우리 서버에는 음악 동아리가 있으니 관심 있으면 들어와!")

@client.command()
async def 게임(ctx, *args):
    await ctx.send("우리 서버에는 게임 동아리가 있으니 관심 있으면 들어와!")

@client.command()
async def 그림(ctx, *args):
    await ctx.send("MAGAM... 이 아니라 우리 서버에는 그림 동아리가 있으니 관심 있으면 들어와!")

@client.command()
async def 공부(ctx, *args):
    await ctx.send("싫어요 ...가 아니라 우리 서버에는 공부 동아리가 있으니 관심 있으면 들어와!")

@client.command()
async def TRPG(ctx, *args):
    await ctx.send("우리 서버에는 TRPG 동아리도 있다구! 관심 있으면 들어와")

@client.command()
async def 잘가(ctx, *args):
    await ctx.send("가지마... ㅠㅠ")

@client.command()
async def 연합(ctx, *args):
    await ctx.send("우리 서버는 연합을 받는 중이야! 서버 연합을 원한다면 관리자에게 개인 DM을 보내줘")

@client.command()
async def 수다(ctx, *args):
    await ctx.send("나는 수다쟁이다! 하는 사람은 우리 서버의 수다 동아리 역할을 받아봐")
 
@client.command()
async def 관리자(ctx, *args):
    await ctx.send("우리 서버의 총관리자는 Steel님, 부관리자는 리니님이야!")

@client.command()
async def 동물농장(ctx, *args):
    await ctx.send("우리 서버 이름이야! 이름 잘 지었지?^^")

@client.command()
async def 오락실(ctx, *args):
    await ctx.send("우리 서버의 게임방이야! 원래 게임 동아리방은 따로 있지만, 게임 알림을 받고 싶지 않은 사람은 오락실을 이용해줘!")

@client.command()
async def 도움말(ctx, *args):
    await ctx.send("나에게 이 서버에 관해 궁금한 걸 물어보면 돼! ```예) 자라야 Steel```")

@client.command()
async def 명령어(ctx, *args):
    await ctx.send("나에게 이 서버에 관해 궁금한 걸 물어보면 돼! ```예) 자라야 Steel```")
 
@client.command()
async def 끄투(ctx, *args):
    await ctx.send("자라투스트라는이렇게말했다... 가 아니라 게임 선택 채널에서 끄투 역할을 받을 수 있어")

@client.command()
async def 마크(ctx, *args):
    await ctx.send("게임 선택 채널에서 마크 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 마인크래프트(ctx, *args):
    await ctx.send("게임 선택 채널에서 마크 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 롤(ctx, *args):
    await ctx.send("게임 선택 채널에서 롤 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 리그오브레전드(ctx, *args):
    await ctx.send("게임 선택 채널에서 롤 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 메이플(ctx, *args):
    await ctx.send("게임 선택 채널에서 메이플스토리 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 어몽어스(ctx, *args):
    await ctx.send("임포스터는 바로 너... 가 아니라 게임 선택 채널에서 어몽어스 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 옵치(ctx, *args):
    await ctx.send("게임 선택 채널에서 오버워치 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 오버워치(ctx, *args):
    await ctx.send("게임 선택 채널에서 오버워치 역할을 받을 수 있어! 관심 있으면 받아봐")

@client.command()
async def 배추(ctx, *args):
    await ctx.send("우리 서버엔 배추봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.command()
async def 마냥(ctx, *args):
    await ctx.send("우리 서버엔 마냥봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.command()
async def 아야나(ctx, *args):
    await ctx.send("우리 서버엔 아야나봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.command()
async def Ayana(ctx, *args):
    await ctx.send("우리 서버엔 Ayana봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.command()
async def 그루비(ctx, *args):
    await ctx.send("우리 서버엔 그루비봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.command()
async def Groovy(ctx, *args):
    await ctx.send("우리 서버엔 Groovy봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.command()
async def 프레드(ctx, *args):
    await ctx.send("우리 서버엔 프레드봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")
 
@client.command()
async def Fredboat(ctx, *args):
    await ctx.send("우리 서버엔 Fredboat봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.command()
async def 미육(ctx, *args):
    await ctx.send("우리 서버의 레벨업 담당 봇! 명령어는 걔한테 직접 물어봐")

@client.command()
async def MEE6(ctx, *args):
    await ctx.send("우리 서버의 레벨업 담당 봇! 명령어는 걔한테 직접 물어봐")

@client.command()
async def 크시(ctx, *args):
    await ctx.send("우리 서버엔 크시봇이 초대되어 있어! 명령어는 걔한테 직접 물어봐")

@client.event
async def on_command_error(ctx, error):
    await ctx.send("무슨 말인지 모름 ㅈㅅ... 커맨드 추가를 원한다면 봇리니를 멘션해줘!"
                   
access_token = os.env['TOKEN']
client.run(access_token)
