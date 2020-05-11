import json
from dataclasses import dataclass, asdict
from random import sample
from pprint import pformat

import config


@dataclass
class WordPair:
    index: int
    query_word: str
    response_word: str
    n_correct: int = 0
    n_asked: int = 0


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


def read_word_pairs():
    words_file_name = f'data/{config.word_list_id}.json'
    print(f'Reading {words_file_name}.')
    with open(words_file_name, 'r', encoding='utf-8') as inputfile:
        raw_word_pairs = json.load(inputfile)    
    print(f'Read {len(raw_word_pairs)} items.')

    word_pairs = [
        WordPair(
            index=i_pair,
            query_word=raw_pair[config.query_index],
            response_word=raw_pair[config.response_index]
        )
        for i_pair, raw_pair in enumerate(raw_word_pairs)
    ]
    return word_pairs


def run_questions(word_pairs):
    n_all_pairs = len(word_pairs)
    pairs_to_ask = list(range(n_all_pairs))

    print(config.query)
    while pairs_to_ask:
        try:
            n_remaining = len(pairs_to_ask)
            index = sample(pairs_to_ask, 1)[0]
            pair = word_pairs[index]
            print(f'\n{pair.query_word}')
            answer = input()
            if answer == pair.response_word:
                print(f'Correct! {n_remaining-1} to go.')
                pair.n_correct += 1
                if pair.n_correct > pair.n_asked:
                    pairs_to_ask.remove(index)
            else:
                print(f'Incorrect. The correct answer is: {pair.response_word}. ')
            pair.n_asked += 1
        except KeyboardInterrupt:
            print('\nStopping session.')
            break
    print('')
    return word_pairs


def write_results(result_word_pairs):
    output_word_pairs = [asdict(word_pair) for word_pair in result_word_pairs]
    stats_file_name = f'data/{config.word_list_id}_stats.json'
    with open(stats_file_name, 'w', encoding='utf-8') as outputfile:
        json.dump(output_word_pairs, outputfile, ensure_ascii=False, indent=2)
    print(f'Wrote results to {stats_file_name}.')


if __name__ == '__main__':
    main()
