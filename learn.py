import json
from pprint import pformat

import config
from interaction import run_questions
from words import WordsRepository


def main():
    words_file_name = 'data/words.json'
    stats_file_name = 'data/word_stats.json'
    config_file_name = 'config.json'

    load_config(config_file_name)
    word_repository = WordsRepository('name')
    word_pairs = word_repository.get_word_pairs(None)
    result_word_pairs = run_questions(word_pairs)
    word_repository.update_word_pairs(result_word_pairs)


def load_config(config_file_name):
    print(f'Loading config file {config_file_name}.')
    with open(config_file_name, 'r', encoding='utf-8') as inputfile:
        config_content = json.load(inputfile)
    config.word_list_id = config_content['word_list_id']
    config.query = config_content['query']
    config.query_index = config_content['query_index']
    config.response_index = config_content['response_index']
    print(f'Loaded configuration.')


if __name__ == '__main__':
    main()
