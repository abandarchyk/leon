import re
import httptransport
import sys
import utils

lines = ['Того, кого не стоило бы ждать', 'hop-hei!', 'la-la-lei']
props = utils.SystemProperties()


def process_into_pattern(input: str):
    words = input.split()
    with_regex = [word + '[\\s|,|.|-]*' for word in words]
    print('intermediate list')
    print(with_regex)
    concatenated_pattern = str.join('', with_regex)
    wrapped = r'\b' + concatenated_pattern + r'\b'
    print("final Result")
    print(wrapped)
    return wrapped


def find_lines(pattern):
    results = {}
    for current_line in lines:
        match = re.search(pattern, current_line, re.IGNORECASE)
        if match is not None:
            results[match] = current_line
            print(results)
    return results


def read_commandline_args():
    for param in sys.argv:
        print('current param is: ' + param)
        if 'id=' in param:
            bid = param[len('id='): len(param)]
            props.id = bid


read_commandline_args()
while True:
    user_input = input()
    res = httptransport.Endpoint(props.id).http_get('/some_url')













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












