from dataclasses import dataclass
import json

import config


@dataclass
class WordPair:
    index: int
    query_word: str
    response_word: str
    n_correct: int = 0
    n_asked: int = 0


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
