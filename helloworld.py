import json
import telegram.api
import random
import time
import utils

lines = ['Хоп-хей, ла-ла-лэй!', 'Где вопросы, где ответ?', 'Что ни говори', 'То ли верить то ли нет',
         'Но Бог тебя хранит']
chats = []
updates = []


file = open('scheme', mode='r', encoding='utf-8')
s = file.read()



while True:
    time.sleep(2)
#   res = telegram.api.get_updates(offset+1)
#   asJson = res.json()
    updates = utils.decode_updates(json.loads(s))

    for update in updates:

        user_chat = update.Message.Chat.id
        user_text = update.Message.text
        # make reply
        reply = ''
        telegram.api.send_message(user_chat, reply)
        offset = update.update_id + 1
















# with open('song', mode='r', encoding='utf-8') as source:
#     dataList = json.load(source)
#     print(dataList)
#
#
# def parse_line():
#     resultList = []
#     for words in resultList:
#         print("you: ")
#         inputLine = input()
#
#         if inputLine == 'stop':
#             break
#     for currentElement in dataList:
#         topic = currentElement['topic']
#         patterns = currentElement['patterns']
#         for currentPattern in patterns:
#             result = inputLine.find(currentPattern)
#             if result != -1:
#                 print("Found pattern: " + currentPattern)
#                 topicPhrases = currentElement['phrases']
#                 print("Adding topic to result list: " + topic)
#                 resultList.extend(topicPhrases)
#                 print('Result list is:')
#                 print(resultList)
#                 break
#     print('bot:')
#     if len(resultList) != 0:
#         index = random.randint(0, len(resultList)-1)
#         print(resultList[index])
#     else:
#         notheme = ['Разноцветные пташки за окном чирикали', 'Отразилась в огне, засверкала бликами',
#                    'Там, где пальмы растут и бананы, и агат']
#         index = random.randint(0, len(notheme) - 1)
#         print(notheme[index])












