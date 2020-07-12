import json
from dataclasses import asdict
from pprint import pformat

import config
from loading import read_word_pairs
from interaction import run_questions


def main():
    words_file_name = 'data/words.json'
    stats_file_name = 'data/word_stats.json'
    config_file_name = 'config.json'

    load_config(config_file_name)
    word_pairs = read_word_pairs()
    result_word_pairs = run_questions(word_pairs)
    write_results(result_word_pairs)


def load_config(config_file_name):
    print(f'Loading config file {config_file_name}.')
    with open(config_file_name, 'r', encoding='utf-8') as inputfile:
        config_content = json.load(inputfile)
    config.word_list_id = config_content['word_list_id']
    config.query = config_content['query']
    config.query_index = config_content['query_index']
    config.response_index = config_content['response_index']
    print(f'Loaded configuration.')


def write_results(result_word_pairs):
    output_word_pairs = [asdict(word_pair) for word_pair in result_word_pairs]
    stats_file_name = f'data/{config.word_list_id}_stats.json'
    with open(stats_file_name, 'w', encoding='utf-8') as outputfile:
        json.dump(output_word_pairs, outputfile, ensure_ascii=False, indent=2)
    print(f'Wrote results to {stats_file_name}.')


if __name__ == '__main__':
    main()
