from random import sample

import config


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
                if pair.n_correct > (pair.n_asked - pair.n_correct):
                    pairs_to_ask.remove(index)
            else:
                print(f'Incorrect. The correct answer is: {pair.response_word}. ')
            pair.n_asked += 1
        except KeyboardInterrupt:
            print('\nStopping session.')
            break
    print('')
    return word_pairs
