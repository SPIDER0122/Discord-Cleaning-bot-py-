
###################
####python 3.x#####
#discord.py==1.4.0#
###################

import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print("봇 온라인 성공")
    game = discord.Game('상태메시지 ~하는중')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개가 삭제되었습니다', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                await message.channel.send('``명령어 사용권한이 없습니다.``')
        except:
            pass


client.run('ODc2Mjc0Mjc1MzM2NzQwOTQ0.YRhsAw.LQh4USeEGgoFoLaTbFWP1pzdWX4')
