# -*- coding: utf-8 -*-
from dingtalkchatbot.chatbot import DingtalkChatbot
from configparser import ConfigParser
import sys
import io
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

'''
# 手机号
'18xxx'  # 某人1
'''


# 消息类型调用方法
class ReleaseTask:
    # 发送 Text 类型消息@某人， 文案里必须要有自定义关键词：xx
    def releaseText(self, webhook, phone, msg, isAll):
        webhook = webhook_release
        dingding = DingtalkChatbot(webhook)
        at_mobiles = [phone]
        isAll = isAll

        dingding.send_text(msg=msg, at_mobiles=at_mobiles, is_at_all=isAll)

        print(sys.stdout)
        print(at_mobiles)
        print("text消息提醒成功")

    # 发送 Link 类型消息， 文案里必须要有自定义关键词:xx
    def releaseLink(self, webhook, title, text, msg_url, pic_url):
        webhook = webhook
        dingding = DingtalkChatbot(webhook)
        pic_url = pic_url

        dingding.send_link(title=title, text=text, message_url=msg_url, pic_url="pic_url")
        print("Link消息提醒成功")

    # 发送 markdown 类型消息，
    def releaseMarkdown(self, webhook, phone, isAll, title, mark_text):
        webhook = webhook
        dingding = DingtalkChatbot(webhook)
        at_mobiles = [phone]
        isAll = isAll

        dingding.send_markdown(title=title, at_mobiles=at_mobiles, text=mark_text, is_at_all=isAll)
        print(isAll)
        print(at_mobiles)
        print("Markdown消息提醒成功")


releaseTask = ReleaseTask()


def read_config(cfg_file):
    cfg = ConfigParser()
    cfg.read(cfg_file)  # 读取cfg_file文件
    return cfg


# 获取当前时间：年月日
time = datetime.datetime.now().strftime('%Y-%m-%d ')

filepath = "index.ini"
# 取cfg文件值
cfg = read_config(filepath)
times = int(cfg.get('release', 'times'))
isAll = cfg.get('release', 'isAll')
msgtype = str(cfg.get('release', 'msgtype'))

# 艾特列表用户
aList = ["15869113126", "18202782781"]
alength = len(aList)
aPhone = aList[times % alength]

# bot_webhook
webhook_release = 'https://oapi.dingtalk.com/robot/send?access_token' \
                  '=06780fde19e6357fa35dc412ead970cfa3ce8d6555db36c9ce25b54a5ab58334 '
# 信息参数配置
msg = time + '\n🤖️值班提醒，本周值班轮到你啦～\n 值班表：https://wepie.yuque.com/we_play/fe9ghq/qcyhx3'

title = '🤖️值班提醒'
text = '点击查看本周值班信息'
message_url = 'https://wepie.yuque.com/we_play/fe9ghq'
picUrl = 'https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png'
# aPhone = "15869113126"

mark_text = "#### 钉钉值班；杭州天气 @158xxx \n > 9度，西北风1级，空气良89，相对温度73%\n > ![screenshot](" \
            "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n > ###### 10点20分发布 [天气](" \
            "https://www.dingtalk.com) \n "

if __name__ == '__main__':
    # 发送text 消息类型
    if msgtype == "text":
        releaseTask.releaseText(webhook_release, aPhone, msg, isAll)
        print("text")
    # 发送link 消息类型
    elif msgtype == "link":
        releaseTask.releaseLink(webhook_release, title, text, message_url, picUrl)
        print("LinkMessage")
    # 发送markdown 消息类型
    elif msgtype == "markdown":
        releaseTask.releaseMarkdown(webhook_release, aPhone, isAll, title, mark_text)
        print("markdown")
    else:
        print("不支持的消息类型 %r" % msgtype)

# 更新cfg文件值
times_update = times + 1
cfg.set('release', 'times', str(times_update))
cfg.write(open(filepath, "w"))
