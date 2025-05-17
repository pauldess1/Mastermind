import itertools
import random
import numpy as np
import matplotlib.pyplot as plt


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


def generate_one_unique_four_digit_number():
    while True:
        num = random.randint(1000, 9999)
        digits = str(num)
        if len(set(digits)) == 4:
            return num


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


def generate_report(steps_to_win):
    print("📊 Rapport sur les performances :")
    print(f"▶️ Maximum d'étapes : {max(steps_to_win)}")
    print(f"✅ Minimum d'étapes : {min(steps_to_win)}")
    print(f"📉 Moyenne d'étapes : {np.mean(steps_to_win):.2f}")
    print(f"📏 Écart-type : {np.std(steps_to_win):.2f}")
    print(f"🔸 Médiane : {np.median(steps_to_win)}")

    # Affichage graphique
    plt.hist(steps_to_win, bins=20, color="skyblue", edgecolor="black")
    plt.title("Distribution des étapes nécessaires pour gagner")
    plt.xlabel("Nombre d'étapes")
    plt.ylabel("Fréquence")
    plt.grid(True)
    plt.show()
