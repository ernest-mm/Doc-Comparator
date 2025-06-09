def show_menu() -> None:
    """
    Affiche le menu mode de comparaison.
    Retourne rien.
    """
    print("-" * 30 + " MODE DE COMPARAISON " + "-" * 30)
    print(" [1] Mode souple (recommandé)")
    print(
        " (Ignore la case (majuscule ou minuscule), " \
        "les espaces supplémentaires, et les \n " \
        " différences de ponctuation.)"
    )
    print(" [2] Mode Stricte")
    print("(Chaque chose compte : ponctuation, case, et espaces supplémentaires)")
    print(" [0] Retour")

def take_input(possible_choices: set[int]) -> int:
    """
    A ecrire
    """
    choice = None

    while choice not in possible_choices:
        try:
            choice = int(input("Entrez votre choix (0-2): "))
        except ValueError:
            choice = None
        if choice not in possible_choices:
            print("Saisie incorrecte.")

    return choice

def show_word_comparison() -> None:
    """
    A faire
    """
    print("Voulez-vous faire la comparaison mot par mot (optionnel)?")
    print("  [Y] Yes     [N] No")

def take_y_n_input() -> bool:
    """
    A faire
    """
    choice = None

    while choice not in set(['y', 'Y', 'n', 'N']):
        choice = input("Entrez votre réponse: ")
        if choice not in set(['y', 'Y', 'n', 'N']):
            print("Saisie incorrecte.")

    if choice == 'y' or choice == 'Y':
        return True
    
    return False

def comparison_mode() -> None:
    show_menu()
    print("")

    choice = take_input(set([0, 1, 2]))
    print("")

    match choice:
        case 0:
            print("Retour au menu principal")
            return
        case 1:
            print("Mode souple selectionné")
        case 2:
            print("Mode strict selectionné")

    show_word_comparison()
    print("")

    choice = take_y_n_input()

    if choice:
        print("Comparaison mot par mot selectionnée")

if __name__ == '__main__':
    comparison_mode()