import os
import re
import random


all_lines = []


def load_data():
    songs_names = os.listdir("data/songs")
    print('...Loading songs')
    for current_song in songs_names:
        print(current_song)
        file = open('data/songs/' + current_song, mode='r', encoding='utf-8')
        song_in_lines = file.readlines()
        all_lines.extend(song_in_lines)


def find_lines(pattern):
    results = {}
    for current_line in all_lines:
        match = re.search(pattern, current_line, re.IGNORECASE)
        if match is not None:
            results[match] = current_line
            print(results)
    return results


def reply_for_matched(match, source_line):
    start_index = match.start()
    if start_index is 0:
        end_index = match.end()
        source_line = ' ..' + source_line[end_index: len(source_line)]
    return source_line



def make_reply(user_input: str):
    pattern = r'\b' + user_input + r'\b'





#if 0 - complete
#if not 0 - whole string
    # if match is None
    # determine topic


load_data()


while True:
    print("you: ")
    user_input = input()
    if user_input == 'stop':
        break
    pat = r'\b' + user_input + r'\b'
    results = find_lines(pat)
    reply = 'Not Found'
    if len(results) > 0:
        rnd_match = random.choice(list(results))
        rnd_value = results.get(rnd_match)
        reply = reply_for_matched(rnd_match, rnd_value)
#    elif len(results) is 0:
#        print('Not found')
#   prepare_intelletual_reply
    print('bot:')
    print(reply)







