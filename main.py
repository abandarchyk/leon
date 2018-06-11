import os


all_lines = []


def load_data():
    songs_names = os.listdir("data/songs")
    for current_song in songs_names:
        print('...Loading songs')
        print(current_song)
        file = open('data/songs/' + current_song, mode='r', encoding='utf-8')
        song_in_lines = file.readlines()
        all_lines.extend(song_in_lines)


def complete_line(input_line: str):
    for current_line in all_lines:
        ind = current_line.find(input_line)
        if ind != -1:
            return current_line
    return 'Not found'


load_data()
while True:
    print("you: ")
    user_input = input()
    if user_input == 'stop':
        break
    result = complete_line(user_input)

    print('bot:')
    print(result)





