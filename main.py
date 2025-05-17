from utils import (
    int_to_list,
    generate_combinations,
    update_combination,
    calculate_score,
    generate_one_unique_four_digit_number,
    generate_report,
)

import random


def run(secret):
    n = 0
    secret = int_to_list(secret)
    all_combinations = generate_combinations()
    while len(all_combinations) > 1:
        n += 1
        guess = random.choice(all_combinations)
        score = calculate_score(guess, secret)
        all_combinations = update_combination(guess, score, all_combinations)
    return n


def main(n_test):
    steps_to_win = []
    for _ in range(n_test):
        secret = generate_one_unique_four_digit_number()
        steps_to_win.append(run(secret))
    generate_report(steps_to_win)


if __name__ == "__main__":
    n_test = 1000
    main(n_test)
