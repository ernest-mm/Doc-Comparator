def afficher_menu():
    print("-----------------SELECTION DES FICHIERS----------------")
    print("Entrez le chemin complet du premier chemins :")
    print("Entrez le chemin complet du second chemins :")
    print("\n(Si vous voulez rentrer au menu precedent, tapez 0)\n")

def demander_chemin(numero):
    chemin = input(f"chemin du fichier {numero} : ")
    if chemin == "0":
        print("Retour au menu precedent...")
        print("sortie du programme")
        sys.exit()
    elif chemin == "2":
        print("entrez le 2eme chemin...")
        return None
    return chemin
def main():
    afficher_menu()
    chemin1 = demander_chemin(1)
    if chemin1 is None:
        return
    
    chemin2 = demander_chemin(2)  
    if chemin2 is None:
        return
    print("\n chemin saisis :")
    print(f"1er fichier : {chemin1}")
    print(f"2e fichier : {chemin2}")

if  __name__ == "__main__":
    main()

