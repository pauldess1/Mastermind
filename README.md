# 🎯 Mastermind

Ce projet est une simulation d'un **solveur automatique du jeu Mastermind**, écrit en Python.  
L'objectif est de déterminer en combien d'essais un algorithme simple peut deviner une combinaison secrète.

---

## 📌 Objectif

- Simuler 10 000 parties de Mastermind avec une stratégie de guessing aléatoire.
- Calculer les statistiques du nombre d'essais nécessaires pour trouver la combinaison secrète.
- Implémenter les règles classiques du Mastermind (feedback par score).
- Préparer le terrain pour tester d'autres stratégies (ex. Knuth, minimax...).

---

## 🧠 Règles de base du Mastermind

- La combinaison secrète est composée de **4 chiffres** distincts choisis parmi `0` à `9`.
- À chaque tentative, le joueur reçoit un **score** en retour :
  - `x` chiffres bien placés.
  - `y` chiffres mal placés mais présents.

---

## 📂 Structure du projet

```bash
.
├── main.py                  
├── utils.py                 
# Fonctions utilitaires (conversion, scoring, filtrage)
├── README.md              
```

## 🚀 Lancer le projet

### ✅ Prérequis

- Python 3.7 ou supérieur
- [NumPy](https://numpy.org/)

### ▶️ Exécution

1. Clone ou télécharge ce dépôt.
2. Assure-toi que `utils.py` est bien dans le même dossier que `main.py`.
3. Exécute le script principal :

```bash
python main.py
```
## Rendus
<p align="center">
  <img src="images\perfs.png" alt="Image 1" width="60%" />
</p>
<p align="center">
  <img src="images\graph.png" alt="Image 2" width="80%" />
</p>


## 📈 Idées d’amélioration

Voici quelques pistes pour enrichir le projet et tester d'autres approches :

- 🔍 **Implémenter l'algorithme de Knuth** : une stratégie optimale qui garantit de trouver la combinaison en 5 coups maximum.
- 🧠 **Comparer plusieurs stratégies de guessing** : aléatoire, fréquence, entropie, etc.
- 💬 **Ajouter une interface en ligne de commande (CLI)** : pour permettre à un utilisateur de jouer contre le solveur.
- 🧪 **Effectuer des tests unitaires** : pour garantir la fiabilité des fonctions de scoring et de filtrage.
- 📊 **Visualiser les performances** : graphiques du nombre d'essais selon les stratégies ou selon la combinaison secrète.

---


