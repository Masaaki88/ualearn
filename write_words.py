import json


def main():
    file_name = get_file_name()
    word_pairs = record_word_pairs()
    store_word_pairs(word_pairs, file_name)
    print('Done.')


def get_file_name():
    short_file_name = input('Enter file name: ')
    return f'./data/{short_file_name}.json'


def record_word_pairs():
    print('Recording word pairs. Enter blank space to stop.')

    word_pairs = []
    while True:
        first_word = input('\nEnter first word: ')
        if not first_word:
            break
        second_word = input('Enter second word: ')
        if not second_word:
            break
        word_pairs.append((first_word, second_word))

    print(f'\nRecorded {len(word_pairs)} word pairs. ')
    return word_pairs


def store_word_pairs(word_pairs, file_name):
    print(f'Writing word pairs to {file_name}.')
    with open(file_name, 'w', encoding='utf-8') as outputfile:
        json.dump(word_pairs, outputfile, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
