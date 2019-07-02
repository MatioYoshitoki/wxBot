#!/usr/bin/env python3.6
#coding=utf-8
import datetime
import time
from concurrent.futures import ProcessPoolExecutor

from wxpy import *

from db_oper import MySQL

# def qrBack():
#     print("获得新的二维码")

botID = "master"
bot = Bot(cache_path=True, console_qr=True)# 用于接入微信的机器人
# print(bot.friends());


# sent_msgs = bot.messages.search(sender=ssp)
# print(sent_msgs)
# ssp.send('开始进行')


def recordmood():
    sleepTime_day = 1 * 60;
    sleepTime_night = 3 * 60;
    sleepTime_now = 0;
    while True:
        hours = int(datetime.datetime.now().strftime('%H'))
        if ((hours>0 and hours<7) or (hours>19 and hours<24)):
            if (sleepTime_now!=sleepTime_night):
                sleepTime_now = sleepTime_night
                continue
        else:
            if (sleepTime_now!=sleepTime_day):
                sleepTime_now = sleepTime_day
                continue
        print(bot.chats())
        gp = bot.chats().search('成人线青岛运营群')[0]
        print(gp)
        mysql = MySQL()
        sql = "SELECT CustomerID FROM TChatSession WHERE DReadFlag = '0' AND UpdateTime >= DATE_ADD(NOW(),INTERVAL -1 HOUR)";
        data = mysql.exe(sql=sql)
        if len(data) != 0:
            gp.send("发现未读的客户图文咨询消息，请及时回复")
        time.sleep(sleepTime_now)

    # friends = bot.friends()
    # for friend in friends:
    #     remark_name = friend.remark_name
    #     v0 = remark_name.split("&amp;")
    #     print(friend.nick_name + "===>" + friend.remark_name)
    #     print(friend.signature)
        # if len(v0) != 2:
        #     continue
        # remark_name = v0[0]
        # user_id = v0[1][2:20]
        # gender = friend.sex
        # city = friend.city
        # province = friend.province
        #
        # mysql = MySQL()
        # sql = "SELECT * FROM TWXUser WHERE UserID = '"+user_id+"' AND RemarkName = '"+remark_name+"' AND BotID = '"+botID+"'";
        # data = mysql.exe(sql=sql)
        # if len(data) != 0:
        #     continue
        #
        # # snow = MySnow(dataID="00")
        # sql = "INSERT INTO TWXUser (id, RemarkName, UserID, City, Province, Gender, BotID) VALUES ("+str(snow.get_id())+", '"+remark_name+"', '"+user_id+"', '"+city+"', '"+province+"', '"+str(gender)+"', '"+botID+"')"
        # mysql.exe(sql=sql)

            #

            # print(friend.alias)
            # print("\n")

        # print(bot.friends())
        # time.sleep(60)
#

#接受来自朋友的语音消息
# @bot.register(msg_types=RECORDING)
# def reply_my_friend(msg):
#     return "语音已收到"
#
# @bot.register(msg_types=TEXT, chats=Friend)
# def reply_my_friend(msg):
#     print(msg)
#     # mysql = MySQL()
#     # sql = "INSERT INTO TWXLog (GroupName, NickName, LogContent) VALUES ('" + msg.chat.name + "', '" + msg.member.name + "', '" + msg.text + "')"
#     # mysql.exe(sql=sql)
#     return "测试信息已收到，稍后接入闲聊。"
#
# @bot.register(msg_types=NOTE, chats=Friend)
# def system_msg(msg):
#     print(msg)
#     # mysql = MySQL()
#     # sql = "INSERT INTO TWXLog (GroupName, NickName, LogContent) VALUES ('" + msg.chat.name + "', '" + msg.member.name + "', '" + msg.text + "')"
#     # mysql.exe(sql=sql)
#     # return "测试信息已收到，稍后接入闲聊。"
#
# @bot.register(msg_types=PICTURE, chats=Friend)
# def reply_my_friend(msg):
#     mysql = MySQL()
#     sql = "INSERT INTO TWXLog (GroupName, NickName, LogContent) VALUES ('" + msg.chat.name + "', '" + msg.member.name + "', '" + msg.text + "')"
#     mysql.exe(sql=sql)
#     return "测试图片已收到。"


#接受群消息被@时回复
# @bot.register(Group, TEXT)
# def auto_reply(msg):
#     # 如果是群聊，但没有被 @，则不回复
#     if isinstance(msg.chat, Group) and not msg.is_at:
#         return
#     else:
#         # 回复消息内容和类型
#         return '收到 @{} 的消息: {} '.format(msg.member.name, msg.text)

@bot.register(Group, RECORDING)
def auto_reply(msg):
    return

@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    # if '心镜' in msg.text.lower():
        # 接受好友 (msg.card 为该请求的用户对象)
    new_friend = bot.accept_friend(msg.card)
    # 或 new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('您好,我是您的心理小助手。\n打印评测报告请点击下方图片，识别图中二维码。')
    new_friend.send_image('1.jpg');






# httpUnit.getImage("1.jpg")
# 堵塞线程，并进入 Python 命令行
pool = ProcessPoolExecutor(max_workers=4)
record = pool.submit(recordmood())
# future1 = pool.submit(sendmessagebytime(0,00,'晚安晚安~[月亮][月亮]'))
# embed()
