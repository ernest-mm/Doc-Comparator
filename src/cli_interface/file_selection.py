def show_menu_title() -> None:
    """
    Affiche le titre du menu de sélection de fichiers.
    """
    print("-" * 30 + " SELECTION DES FICHIERS " + "-" * 30)

def ask_file_path() -> None:
    """
    Demande à l'utilisateur les deux fichiers à comparer.
    """
    path_1 = input("Entrez le chemin complet du premier fichier (ou 0 pour quitter): ")
    if path_1 == "0":
        print("Retour au menu precedent...")
        return

    path_2 = input("Entrez le chemin complet du second fichier (ou 0 pour quitter): ")
    if path_2 == "0":
        print("Retour au menu precedent...")
        return
    
    print("\nChemins saisis :")
    print(f"1er fichier : {path_1}")
    print(f"2e fichier : {path_2}")


def file_selection_menu() -> None:
    show_menu_title()
    print("")

    ask_file_path()

if __name__ == "__main__":
    file_selection_menu()