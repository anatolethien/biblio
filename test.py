import csv

# Fonction pour lire un fichier CSV et retourner une liste de dictionnaires
def read_csv("F:\\Projet B3\\biblio\\assets\\dataset.csv")
    data = []
    with open("F:\\Projet B3\\biblio\\assets\\dataset.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# Appeler la fonction pour lire chaque fichier CSV
authors = read_csv("F:\\Projet B3\\biblio\\assets\\authors.csv")
categories = read_csv("F:\\Projet B3\\biblio\\assets\\categories.csv")
dataset = read_csv("F:\\Projet B3\\biblio\\assets\\dataset.csv")
formats = read_csv("F:\\Projet B3\\biblio\\assets\\formats.csv")
places = read_csv("F:\\Projet B3\\biblio\\assets\\places.csv")

# Fonction pour suggérer des livres en fonction du genre
def suggest_books(genre):
    # Lire le fichier "dataset"
    dataset = read_csv("dataset.csv")

    # Filtrer le dataset pour n'obtenir que les livres du genre spécifié
    genre_books = [book for book in dataset if genre in book["categories"]]

    # Si aucun livre n'a été trouvé, afficher un message
    if len(genre_books) == 0:
        print("Aucun livre de ce genre n'a été trouvé.")
        return

    # Pour chaque livre du genre, afficher le titre et l'auteur
    for book in genre_books:
        # Lire le fichier "authors" et trouver l'auteur correspondant
        authors = read_csv("authors.csv")
        author = next(a for a in authors if a["author_id"] == book["author_id"])

        print(f"Titre : {book['title']}")
        print(f"Auteur : {author['name']}")
        print()

# Appeler la fonction pour suggérer des livres de science-fiction
suggest_books("Science-Fiction")