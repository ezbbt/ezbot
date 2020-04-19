import discord
import asyncio
import random
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("하이")

    if message.content.startswith("!주사위"):
        food = "1 2 3 4 5 6"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await message.channel.send(foodresult)

    if message.content.startswith("!dice"):
        food = "1 2 3 4 5 6"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await message.channel.send(foodresult)

    if message.content.startswith("!12주사위"):
        food = "1 2 3 4 5 6 7 8 9 10 11 12"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await message.channel.send(foodresult)

    if message.content.startswith("!12dice"):
        food = "1 2 3 4 5 6 7 8 9 10 11 12"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber - 1]
        await message.channel.send(foodresult)

    if message.content.startswith("!사다리"):
        team = message.content[5:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "---->" + teamname[i])

    if message.content.startswith("!amidakuji"):
        team = message.content[5:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "---->" + teamname[i])

    if message.content.startswith("!사용방법"):
        await message.channel.send("============ 주사위  사용 방법 ================")
        await message.channel.send("예) !주사위  ")
        await message.channel.send("1~6까지 랜덤으로 나옴")
        await message.channel.send("============ 12주사위  사용 방법 ==============")
        await message.channel.send("예) !12주사위  ")
        await message.channel.send("1~12까지 랜덤으로 나옴")
        await message.channel.send("=========== 사다리 타기 사용 방법 ==============")
        await message.channel.send("예) 참여자 3명(이름)/결과3개 일경우")
        await message.channel.send("예) 명령어----> !사다리 이름1 이름2 이름3/당첨 꽝 꽝")
        await message.channel.send("예) 랜덤으로 당첨과 꽝이 골라짐")
        await message.channel.send("================== Ez ======================")

    if message.content.startswith("!help"):
        await message.channel.send("========== サイコロを使用する方法 ==============")
        await message.channel.send("=                                 !dice                              =")
        await message.channel.send("=                       1~6までランダム                         =")
        await message.channel.send("========== 12주サイコロを使用する方法 ===========")
        await message.channel.send("=               !12dice                       ========================")
        await message.channel.send("=            1~12までランダム                  ===================")
        await message.channel.send("=========== あみだくじを使用する方法 ============")
        await message.channel.send("=                           !amidakuji                              =")
        await message.channel.send("=               !amidakuji name1 name2/no yes               =")
        await message.channel.send("=         !amidakuji name1 name2 name3/no no yes        =")
        await message.channel.send("================== Ez ======================")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

