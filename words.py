from dataclasses import dataclass, asdict
import json

import config


@dataclass
class WordPair:
    index: int
    query_word: str
    response_word: str
    n_correct: int = 0
    n_asked: int = 0


class WordsRepository:
    def __init__(self, name):
        self._name = name

    def get_word_pairs(self, count):
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

    def update_word_pairs(self, result_word_pairs):
        output_word_pairs = [asdict(word_pair) for word_pair in result_word_pairs]
        stats_file_name = f'data/{config.word_list_id}_stats.json'
        with open(stats_file_name, 'w', encoding='utf-8') as outputfile:
            json.dump(output_word_pairs, outputfile, ensure_ascii=False, indent=2)
        print(f'Wrote results to {stats_file_name}.')
