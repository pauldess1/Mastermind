from utils import (
    int_to_list,
    generate_combinations,
    update_combination,
    calculate_score,
)

import random
import numpy as np


def main(secret):
    steps_to_win = []
    for _ in range(10000):
        n = 0
        secret = int_to_list(secret)
        all_combinations = generate_combinations()

        while len(all_combinations) > 1:
            n += 1
            guess = random.choice(all_combinations)
            score = calculate_score(guess, secret)
            all_combinations = update_combination(guess, score, all_combinations)
        steps_to_win.append(n)

    print(max(steps_to_win))
    print(min(steps_to_win))
    print(np.mean(steps_to_win))


if __name__ == "__main__":
    main(secret=8912)
