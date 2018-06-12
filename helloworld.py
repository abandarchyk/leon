import re


lines = []


def load_data():
    file = open('data/songs/debug', mode='r', encoding='utf-8')
    song_in_lines = file.readlines()
    lines.extend(song_in_lines)


def check_line(pattern, test_line: str):
    print('Checking pattern: ' + pattern + ' in line: ' + test_line)
    match = re.search(pattern, test_line)
    return match


def complete_line(match, test_line):
    if match is not None:
        start_index = match.start()
        if start_index is 0:
            end_index = match.end()
            new_line = test_line[end_index: len(test_line)]
            print(new_line)
        else:
            print(test_line)


load_data()
for current_line in lines:
    user_input = 'она любила'
    pat = r'\b' + user_input + r'\b'
    match_result = check_line(pat, current_line)
    print(match_result)
    complete_line(match_result, current_line)



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












