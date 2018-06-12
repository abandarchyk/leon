import os
import re


all_lines = []


def load_data():
    songs_names = os.listdir("data/songs")
    print('...Loading songs')
    for current_song in songs_names:
        print(current_song)
        file = open('data/songs/' + current_song, mode='r', encoding='utf-8')
        song_in_lines = file.readlines()
        all_lines.extend(song_in_lines)


def check_line(pattern, test_line: str):
    print('...Checking pattern: ' + pattern + ' in line: ' + test_line)
    match = re.search(pattern, test_line, re.IGNORECASE)
    if match is not None:
        return True
    return False


def complete_line(match, test_line):
    res = test_line
    start_index = match.start()
    if start_index is 0:
        end_index = match.end()
        res = test_line[end_index: len(test_line)]
    return res


def make_reply(input: str):
#get match
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
    isFound = False;
    for current_line in all_lines:
        isFound = check_line(pat, current_line)
        if isFound:
            bot_reply = complete_line(matcher, current_line)
            break




