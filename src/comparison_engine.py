def compare_lines(text1: str, text2: str) -> dict:
    """
    Compare deux textes ligne par ligne.
    Retourne un dictionnaire contenant :
    - 'common': lignes identiques
    - 'diff': paires de lignes différentes (sous forme de tuples)
    - 'unique_to_text1': lignes uniquement dans le texte 1
    - 'unique_to_text2': lignes uniquement dans le texte 2
    """
    # On divise chaque texte en lignes individuelles
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    common = []
    diff = []
    unique_to_text1 = []
    unique_to_text2 = []

    # On compare les lignes position par position 
    for l1, l2 in zip(lines1, lines2):
        if l1 == l2:
            common.append(l1)
        else:
            diff.append((l1, l2))  # On garde les deux versions différentes

    # On regarde s’il reste des lignes non comparées (si l’un est plus long que l’autre)
    if len(lines1) > len(lines2):
        unique_to_text1.extend(lines1[len(lines2):])
    elif len(lines2) > len(lines1):
        unique_to_text2.extend(lines2[len(lines1):])

    return {
        'common': common,
        'diff': diff,
        'unique_to_text1': unique_to_text1,
        'unique_to_text2': unique_to_text2
    }


if __name__ == "__main__":
    t1 = "Bonjour\nComment ça va ?\nTrès bien"
    t2 = "Bonjour\nComment ça va\nTrès bien"

    resultats = compare_lines(t1, t2)
    print(resultats)