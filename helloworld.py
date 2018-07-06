import json
import telegram.api
import random
import time

lines = ['Хоп-хей, ла-ла-лэй!', 'Где вопросы, где ответ?', 'Что ни говори', 'То ли верить то ли нет',
         'Но Бог тебя хранит']
chats = []


file = open('scheme', mode='r', encoding='utf-8')
pyth_obj = json.loads(file.read())


def extract_data(updates_response: json):
    results = updates_response['result']
    for result in results:
        target_chat_id = result['message']['chat']['id']
        chats.append(target_chat_id)
    lastupdate = results[len(results)-1]['update_id']
    return lastupdate


offset = 0

while True:
    time.sleep(2)
    res = telegram.api.get_updates(offset+1)
    asJson = res.json()
    if len(asJson['result']) > 0:
            offset = extract_data(asJson)
            index = random.randint(0, len(lines) - 1)
            telegram.api.send_message(chats.pop(0), lines[index])















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












