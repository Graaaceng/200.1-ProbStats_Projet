# Projet de probabilités et statistiques: Météoroligie

Projet commun du cours de probabilités et statistiques. Chaque membre développe son travail individuellement dans son dossier et sur sa propre branche.

## Organisation du dépôt

- `Alyx/`, `Grace/`, `Lucas/` : espace de travail individuel de chaque membre.
- `pyproject.toml` et `uv.lock` : configuration du projet Python et dépendances verrouillées.
- `main` : version commune du projet.

## Collaborer avec Git

Chaque personne travaille sur une branche qui lui est propre. Les fichiers communs (datasets) peuvent être directement push sur `main`.

Si il y a eu des changements sur main:
```bash
git checkout main
git pull
```
Créer une branche et travailler dessus:
```bash
git checkout -b <nom-de-la-branche>     # créer une branche
git checkout <autre-branche>            # switcher sur une autre branche
git pull
```

## Environnement Python

Le projet requiert Python 3.12 ou une version ultérieure et utilise `uv` pour gérer l'environnement et les dépendances. Après avoir installé Python et `uv`, depuis la racine du dépôt, exécutez :

```bash
uv sync
```

Pour ouvrir ou créer un notebook **marimo** :

```bash
uv run marimo edit chemin/vers/fichier.py
```