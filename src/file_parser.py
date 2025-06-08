import os

def file_exists(filepath: str) -> bool:
    """
    Vérifie si un fichier existe à l'emplacement donné.

    :param filepath: Chemin d'accès au fichier.
    :return: True si le fichier existe, False sinon.
    """
    #TODO: Implémenter la vérification de l'existence du fichier

def read_txt_file(filepath: str) -> str:
    """ 
    Lit le contenu d'un fichier texte (.txt) et 
    renvoie le texte sous forme de chaîne de caractères.

    :param filepath: Chemin d'accès au fichier texte.
    :return: Contenu du fichier sous forme de chaîne, ou None en cas d'erreur.
    """
    #TODO: Implémenter la lecture du fichier texte

def read_pdf_file(filepath: str) -> str:
    """
    Extrait le texte d'un fichier PDF.

    :param filepath: Chemin d'accès au fichier PDF.
    :return: Texte extrait du PDF sous forme de chaîne, ou None en cas d'erreur.
    """
    #TODO: Implémenter la lecture du fichier PDF

def parse_file(filepath: str) -> str:
    """
    Détecte l'extension du fichier et appelle la fonction appropriée de lecture
    (texte ou PDF). Gère également la vérification de l'existence du fichier
    et des formats non supportés.
    
    :param filepath: Chemin d'accès au fichier.
    :return: Contenu du fichier sous forme de chaîne, 
    ou None en cas d'erreur ou si le format n'est pas supporté.
    """
    #TODO: Implémenter la détection de l'extension du fichier et 
    # appeler la fonction de lecture appropriée