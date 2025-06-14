def show_menu() -> None:
    print("="*80)
    print(' '*30 + "DOCUMENT COMPARATOR" + ' '*30)
    print("="*80)
    print(
        "Bienvenue! Cet outil vous permet de comparer le contenu de deux fichiers texte\n" +
        "(.txt ou .pdf) et met en évidence les similitudes et les différences."
    )
    print("MENU PRINCIPAL:")
    print(" "*4 + "[1] Comparaison des Documents")
    print(" "*4 + "[2] Quitter")

def ask_choice(possible_choices: set) -> int:
    choice = None
    
    while choice not in possible_choices:
        try:
            choice = int(input("Entrez votre choix (1 ou 2): "))
        except ValueError:
            choice = None
        print("Saisie incorrecte!")

    return choice

def main() -> None:
    show_menu()
    print()

    possible_choices = set([1, 2])

    choice = ask_choice(possible_choices)

    match choice:
        case 1:
            print(">> Comparaison des documents à venir...")
        case 2:
            print("Au revoir !")

if __name__ == "__main__":
    main()