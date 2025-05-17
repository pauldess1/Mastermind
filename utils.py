import itertools


def int_to_list(n):
    if isinstance(n, list):
        return n
    else:
        string = str(n)
        liste = []
        for i in string:
            liste.append(int(i))
        return liste


def generate_combinations():
    all_combinations = [list(p) for p in itertools.permutations(range(10), 4)]
    return all_combinations


def calculate_score(liste1, liste2):
    """
    Calcule le score entre 2 listes
    Renvoie le résultat sous la forme [nb positions exactes, nb valeurs exactes]

    """
    score = [0, 0]
    for i in range(4):
        if liste1[i] == liste2[i]:
            score[0] += 1
    commun = list(set(liste1) & set(liste2))
    score[1] = len(commun) - score[0]
    return score


def update_combination(guess, score, combinations):
    updated_combinations = []
    for combination in combinations:
        if score == calculate_score(guess, combination):
            updated_combinations.append(combination)
    return updated_combinations
