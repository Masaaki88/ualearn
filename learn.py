import json
from dataclasses import dataclass, asdict
from random import sample


@dataclass
class WordPair:
    index: int
    ukrainian: str
    german: str
    n_correct: int = 0
    n_asked: int = 0


def main():
    words_file_name = 'data/words.json'
    stats_file_name = 'data/word_stats.json'
    
    word_pairs = read_word_pairs(words_file_name)
    result_word_pairs = run_questions(word_pairs)
    write_results(result_word_pairs, stats_file_name)


def read_word_pairs(words_file_name):
    print(f'Reading {words_file_name}.')
    with open(words_file_name, 'r', encoding='utf-8') as inputfile:
        raw_word_pairs = json.load(inputfile)    
    print(f'Read {len(raw_word_pairs)} items.')

    word_pairs = [
        WordPair(index=i_pair, ukrainian=raw_pair[0], german=raw_pair[1])
        for i_pair, raw_pair in enumerate(raw_word_pairs)
    ]
    return word_pairs


def run_questions(word_pairs):
    n_all_pairs = len(word_pairs)
    pairs_to_ask = list(range(n_all_pairs))

    print('\nTranslate the following words:')
    while pairs_to_ask:
        try:
            n_remaining = len(pairs_to_ask)
            index = sample(pairs_to_ask, 1)[0]
            pair = word_pairs[index]
            print(f'\n{pair.ukrainian}')
            answer = input()
            if answer == pair.german:
                print(f'Correct! {n_remaining-1} to go.')
                pair.n_correct += 1
                pairs_to_ask.remove(index)
            else:
                print(f'Incorrect. The correct answer is: {pair.german}. ')
            pair.n_asked += 1
        except KeyboardInterrupt:
            print('\nStopping session.')
            break
    print('')
    return word_pairs


def write_results(result_word_pairs, stats_file_name):
    output_word_pairs = [asdict(word_pair) for word_pair in result_word_pairs]
    with open(stats_file_name, 'w', encoding='utf-8') as outputfile:
        json.dump(output_word_pairs, outputfile, ensure_ascii=False, indent=2)
    print(f'Wrote results to {stats_file_name}.')


if __name__ == '__main__':
    main()
