def show_menu() -> None:
    print("-"*30 + " COMPARAISON DES DOCUMENTS " + "-"*30)
    print(" Selectionnez le type de fichier: ")
    print("[1] .txt")
    print("[2] .pdf")
    print("[3] .pdf et .txt")
    print("[0] Retour")

def take_input(possible_choices: set) -> int:
    choice = None

    while choice not in possible_choices:
        try:
            choice = int(input("Entrez votre choix (0 à 3): "))
        except ValueError:
            choice = None
        
        print(("Saisie invalide, re-entrez un nombre de 0 à 3"))

    return choice

def doc_comparison_menu() -> None :
    show_menu()
    print("")

    possible_choices = set([0, 1, 2, 3])

    choice = take_input(possible_choices)

    match choice:
        case 1:
            print("<< Comparaison .txt sélectionnée >>")
        case 2:
            print("<< Comparaison .pdf sélectionnée >>")
        case 3:
            print("<< Comparaison mixte sélectionnée >>")
        case 0:
            print("<< Retour au menu principal >>")
            
if __name__ == "__main__":
    doc_comparison_menu()