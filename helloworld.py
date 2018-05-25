import random
import json
import os


def load_data():
    songs_names = os.listdir("songs")
    for current_song in songs_names:
        file = open('songs/' + current_song, mode='r', encoding='utf-8')
        song_in_lines = file.readlines()
        return song_in_lines

with open('song', mode='r', encoding='utf-8') as source:
    dataList = json.load(source)
    print(dataList)


while True:
    resultList = []
    print("you: ")
    inputLine = input()

    if inputLine == 'stop':
        break
    for currentElement in dataList:
        topic = currentElement['topic']
        patterns = currentElement['patterns']
        for currentPattern in patterns:
            result = inputLine.find(currentPattern)
            if result != -1:
                print("Found pattern: " + currentPattern)
                topicPhrases = currentElement['phrases']
                print("Adding topic to result list: " + topic)
                resultList.extend(topicPhrases)
                print('Result list is:')
                print(resultList)
                break
    print('bot:')
    if len(resultList) != 0:
        index = random.randint(0, len(resultList)-1)
        print(resultList[index])
    else:
        notheme = ['Разноцветные пташки за окном чирикали', 'Отразилась в огне, засверкала бликами',
                   'Там, где пальмы растут и бананы, и агат']
        index = random.randint(0, len(notheme) - 1)
        print(notheme[index])












