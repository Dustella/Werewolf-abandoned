
from nonebot.adapters.cqhttp import Bot,PrivateMessageEvent
from nonebot import on_message
from random import shuffle
from nonebot.adapters.cqhttp.message import Message

from nonebot.plugin import on, on_command
from .config import Config



qqdict={
'lalala':111111111
# 格式：名字：QQ号
    
}

player=['zfy','wkx','whk','lhc','sty','mzg','wjn','zt','ypy','zcc']
# 玩家列表，每一项要能在qdict里找到
deck=['预言家','女巫','狼人','狼人','狼人','猎人','平民','平民','平民','丘比特']
# 职业列表，列表长度要和玩家数相同
run=on_command('start')

@run.handle()
async def decking(bot:Bot):
    qqlist=[]
    for i in player:
        qqlist.append(qqdict[i])
    role={}
    shuffle(deck)
    role=dict(zip(qqlist,deck))
    shuffle(deck)
    for i in qqlist:
        m='第六局：'+role[i]
        
        await bot.send_private_msg(user_id=i,message=m)
    run.finish()