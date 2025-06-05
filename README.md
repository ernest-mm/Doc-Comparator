# Doc-Comparator

## Intégration Continue

Ce projet utilise GitHub Actions pour automatiser plusieurs contrôles de qualité et tests à chaque push 
ou pull request sur la branche `main`. 
Le pipeline CI effectue notamment les actions suivantes :

- **Linting et Formatage** :  
  Exécute Flake8 (vérification du code), Black (vérification du formatage) et Mypy (vérification du typage statique).

- **Exécution des Tests et Couverture** :  
  Lance les tests unitaires via `pytest` tout en collectant la couverture de code avec `coverage.py`.
  Un seuil minimal de 80 % de couverture est imposé.

Pour plus de détails sur le fonctionnement de la CI, voir le fichier [`CI.md`](docs/CI.md).
