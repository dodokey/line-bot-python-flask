from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import os
import psycopg2
import random


import time
import schedule
import threading

from apiTest.authorizationkey import *


app = Flask(__name__, static_folder='', static_url_path='')
CORS(app)

# ==PostgreSQL
# conn = psycopg2.connect(
#     dbname=dburl.path[1:],
#     user=dburl.username,
#     password=dburl.password,
#     host=dburl.hostname,
#     port=dburl.port
# )
# cur = conn.cursor()
# ==PostgreSQL


# Channel Access Token
line_bot_api = LineBotApi(LineBotApiKey)
# Channel Secret
handler = WebhookHandler(LineBothandler)
# 監聽所有來自 /callback 的 Post Request


# def schedules():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


# 建立一個子執行緒
# t = threading.Thread(target=schedules)
# 執行該子執行緒
# t.start()
# == schedule functions=================


# def announce(ttp):
#     textToPush = ttp
#     cur.execute("SELECT * FROM userOrGroupID;")
#     row = cur.fetchone()
#     while row is not None:
#         line_bot_api.push_message(row[2], TextSendMessage(text=textToPush))
#         row = cur.fetchone()


# == schedule functions=================

# # schedule.every(1).minutes.do(nowtime)
# schedule.every().day.at("11:59").do(announce, ttp="吃飯囉喔喔喔~")
# schedule.every().day.at("17:59").do(announce, ttp="大家吃晚餐了嗎\nヽ(●´∀`●)ﾉ")
# schedule.every().day.at("16:00").do(announce, ttp="肚子餓惹ˊˋ")
# # schedule.every(1).hour.do(imRfaa, paramettt='hi')

txttt = ''


@app.route('/', methods=['GET'])
def index():
    global txttt
    msg = txttt
    txttt = ''
    return msg


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理PostbackEvent
@handler.add(PostbackEvent)
def handle_post_message(event):
    # can not get event text
    print("event =", event)
    line_bot_api.reply_message(
        event.reply_token,
        TextMessage(
            text=str(str(event.postback.data)),
        )
    )


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global txttt
    # event.message.text:對方傳來的文字訊息
    print('-----hoyoooooooooooo------------------------')
    thstext = event.message.text
    # profile = line_bot_api.get_profile(event.source.user_id)  # user profile
    print(event)
    print('-----------------------------')
    try:
        to = event.source.group_id
    except:
        to = event.source.user_id
    message = TextSendMessage(text=thstext + '\nˊˋ')
    line_bot_api.reply_message(event.reply_token, message)
    txttt = thstext
    # to: get ID (Group first)

    # 存下對方傳來的訊息
    # cur.execute("INSERT INTO contentlog (content) VALUES ('" + thstext + "');")
    # 存下對方傳來的訊息

    # weather api test
    # try:
    #     weatherAnswer = whatIsTheWeather(1, thstext)
    #     message = TextSendMessage(
    #         text=thstext+'嗎(๑• . •๑)\n稍晚的天氣是' +
    #         weatherAnswer['weather'] +
    #         '\n氣溫'+weatherAnswer['minT'] +
    #         '到'+weatherAnswer['MaxT'] +
    #         '度C\n降雨機率'+weatherAnswer['rainProbability'] + '％')
    #     line_bot_api.reply_message(event.reply_token, message)
    # except:
    #     pass
    # # weather api test

    # # 判斷是不是增加行事曆
    # if thstext[0] == '@' or thstext[0] == '＠':
    #     message = TextSendMessage(text=thstext[1:] + '\nˊˋ')
    #     line_bot_api.reply_message(event.reply_token, message)

    # if thstext == '美兔':
    #     cur.execute("SELECT * FROM rfaapic;")
    #     thispic = random.randint(0, cur.rowcount - 1)
    #     thispicurl = cur.fetchall()[thispic][0]
    #     message = ImageSendMessage(
    #         original_content_url=thispicurl, preview_image_url=thispicurl)
    #     line_bot_api.reply_message(event.reply_token, message)
    #     time.sleep(10)
    #     line_bot_api.push_message(to, TextSendMessage(text='(*´艸`*)'))

    # if ('臭阿肥'in thstext) or ('臭阿鼻'in thstext):
    #     message = ImageSendMessage(
    #         original_content_url='https://i.imgur.com/1JxDWma.jpg',
    #         preview_image_url='https://i.imgur.com/1JxDWma.jpg')
    #     line_bot_api.reply_message(event.reply_token, message)

    # if thstext == 'joke':
    #     result = findhahapoint(30)
    #     message = TextSendMessage(
    #         text=result['title']+'\n'+result['url'])
    #     line_bot_api.reply_message(event.reply_token, message)

    # if '猜謎'in thstext:
    #     result = guess()
    #     message = TextSendMessage(text='Q: '+result['Q'])
    #     line_bot_api.reply_message(event.reply_token, message)
    #     time.sleep(5)
    #     line_bot_api.push_message(to, TextSendMessage(text=result['A']))
    #     time.sleep(1)
    #     line_bot_api.push_message(to, TextSendMessage(text='( ^ω^)'))

    # if '公告公告' in thstext:
    #     announce(thstext[4:])
    #     message = TextSendMessage(text='OKOK')
    #     line_bot_api.reply_message(event.reply_token, message)

    # if thstext == 'work':
    #     buttons_template = TemplateSendMessage(
    #         alt_text='Buttons Template',
    #         template=ButtonsTemplate(
    #             title='這是ButtonsTemplate',
    #             text='ButtonsTemplate可以傳送text,uri',
    #             thumbnail_image_url='https://i.imgur.com/1JxDWma.jpg',
    #             actions=[
    #                 MessageTemplateAction(
    #                     label='ButtonsTemplate',
    #                     text='ButtonsTemplate'
    #                 ),
    #                 URITemplateAction(
    #                     label='VIDEO1',
    #                     uri='https://i.imgur.com/1JxDWma.jpg'
    #                 ),
    #                 PostbackTemplateAction(
    #                     label='postback',
    #                     text='postback text',
    #                     data='美兔'
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token, buttons_template)

    # if thstext == '按鈕':
    #     Confirm_template = TemplateSendMessage(
    #         alt_text='目錄 template',
    #         template=ConfirmTemplate(
    #             title='這是ConfirmTemplate',
    #             text='這就是ConfirmTemplate,用於兩種按鈕選擇',
    #             actions=[
    #                 PostbackTemplateAction(
    #                     label='Y',
    #                     text='Y',
    #                     data='action=buy&itemid=1'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='N',
    #                     text='N'
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token, Confirm_template)
    # conn.commit()


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
