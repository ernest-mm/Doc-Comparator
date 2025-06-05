# Documentation de l'Intégration Continue (CI)

Ce document décrit la configuration et le fonctionnement de la CI utilisée dans ce projet via GitHub Actions.

## Emplacement du Workflow

Le workflow CI se trouve dans le fichier :
.github/workflows/ci.yml


## Déclenchement de la CI

La CI s'exécute lors des événements suivants :
- **Push** sur la branche `main`
- **Pull Request** visant la branche `main`

## Structure du Workflow

Le fichier `ci.yml` se décompose en plusieurs étapes clés :

1. **Checkout du Repository**  
   Utilisation de `actions/checkout@v4` pour récupérer le code source dans l'environnement d'exécution.

2. **Configuration de l'Environnement Python**  
   Utilise `actions/setup-python@v4` avec une stratégie de matrice pour tester le code avec différentes versions de Python (ex. 3.9, 3.11, 3.12).

3. **Installation des Dépendances**  
   Mise à jour de `pip` et installation des dépendances listées dans `requirements.txt`.  
   Installation complémentaire d'outils de qualité de code : Flake8, Black, Mypy et Coverage.

4. **Vérifications de Qualité du Code**  
   - **Flake8** : Analyse le code en utilisant la configuration définie dans `config/.flake8` (ou adaptable selon l'organisation de vos fichiers).  
   - **Black** : Vérifie que le code respecte bien le formatage.
   - **Mypy** : Réalise une analyse statique du typage en se basant sur `config/mypy.ini`.

5. **Exécution des Tests et Reporting de la Couverture**  
   - **Tests** : Exécution des tests unitaires via `pytest`.  
   - **Coverage** :  
     - `coverage run -m pytest …` lance les tests tout en collectant la couverture.
     - `coverage report --fail-under=80` affiche un rapport texte et fait échouer la CI si la couverture est inférieure à 80 %.
     - `coverage html` génère un rapport HTML dans le dossier `htmlcov`.


## Exécution Locale et Débogage

Il est possible d'exécuter le workflow en local pour tester et déboguer la CI. Voici quelques conseils :

- **Exécuter les commandes individuellement**  
  Pour vérifier le linting, le formatage ou la couverture en local, vous pouvez utiliser :
  ```bash
  # Linting du code
  flake8 --config=config/.flake8 .

  # Vérification du formatage
  black --check .

  # Analyse de typage
  mypy --config-file=config/mypy.ini .

  # Exécution des tests avec couverture
  coverage run -m pytest --maxfail=1 --disable-warnings -q
  coverage report --fail-under=80```
 

