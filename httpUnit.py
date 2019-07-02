import requests
from PIL import Image
from io import BytesIO
from wxpy import *
import time
import requests
import json
import sys


def getToken():
    url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxcce7931c32672f3a&secret=9a969058d48d3213a2c391d341d1921c"
    response=requests.get(url)
    return json.loads(response.text)["access_token"]

def getImage(imagePath):
    img_src='https://api.weixin.qq.com/wxa/getwxacode?access_token='+getToken()
    body = {"path": "pages/scanCompany/scanCompany?hospitalID=qd901&gID=WL1234512362"}
    # body = {"path": "directPage/halfQuit/halfQuit"}
    # body = {"path": "pages/buyScan/buyScan"};
    response = requests.post(img_src, data=json.dumps(body))
    # print(response.text)
    image = Image.open(BytesIO(response.content))
    image.save(imagePath)


# getImage("/Users/matioyoshitoki/Desktop/ChatBotWeb/web/WEB-INF/img/1.jpg")
# getImage("/home/liuting/ChatBot/1.jpg")
getImage("1.jpg")
# bot = Bot(cache_path=True, console_qr=True)# 用于接入微信的机器人
# # moodbot = Bot(cache_path=True,console_qr=-2)# 用于接入微信的机器人
# # moodbot = Bot()
# ssp = bot.friends().search('高端职业变态')[0]
# deatillist = {}
# #deatillist = {"6432476461453565953":{"q1":"0","q2":"0","q3":"0"},"11111111111":{"q1":"0","q2":"0","q3":"0"},"8888888888":{"q1":"0","q2":"0","q3":"0"},"2222222222":{"q1":"0","q2":"0","q3":"0"},"3333333333":{"q1":"0","q2":"0","q3":"0"},"4444444444":{"q1":"0","q2":"0","q3":"0"},"5555555555":{"q1":"0","q2":"0","q3":"0"},"6666666666":{"q1":"0","q2":"0","q3":"0"}}
# sent_msgs = bot.messages.search(sender=ssp)
# print(sent_msgs)
# # ssp.send('开始进行')
# sendlist=[]
# postData = {
#     'recordDate': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
# }
# response = requests.get('http://www.medicalai.net:8016/api/no/emotion/user', data=postData)
# # 通过get请求返回的文本值
# aaa = json.loads(response.text)
# # print(aaa)
# # for user in aaa['data']:
# #     deatillist[user['userId']] = {"q1": "0", "q2": "0", "q3": "0"}
# #     sendlist.append(user['userId'])
#
#
#
# # sendlist = ['18561306639'] #['6432476461453565953',"11111111111","8888888888","2222222222","3333333333","4444444444","5555555555","6666666666"]
#
# friendlist = bot.friends()
# # print(bot.mps().search("万灵精神心理人工智能"))
# # for user in friendlist:
# #     if (user.name != 'S' ):
# #         # user.send_image('wanling.png')
# #         print()
# for username in friendlist:
#     # sendfriend = bot.friends().search(username)
#     # if (sendfriend.__len__() > 0):
#     # 发送万灵云小程序
#     try:
#         # print(username)
#         username.send_image('1.jpg')
#         # sendfriend[0].send('请记录您的情绪状态：1.很高涨。 2.较高涨。3.高涨。4.正常。5.低沉。6.较低沉。7.很低沉')
#     except ResponseError as e:
#         # 将抛出 ResponseError 错误
#         print(e.err_code, e.err_msg)  # 查看错误号和错误消息
#     time.sleep(5)




# print(getToken())
# getImage("1.jpg")
# img_src='https://api.weixin.qq.com/wxa/getwxacode?access_token=13_YwTrinEa8EgOWLxMNfX4fkLFcAhmODtykVY4sOG6U5VJJ2phb06LsM04rQqf4jj7Lpf4JyrmW6fT73MIC9hodVE2XDfJeE4jwoM6hgfBGV4r1lgDZirPNPGDu1VPhZc0T4l-LoT9oSZrDQstWIPeAFASEL'
# body={"path":"page/essay"}
#
# response = requests.post(img_src, data=json.dumps(body))
#
# # print(response.text)
# image = Image.open(BytesIO(response.content))
# image.save('9.jpg')