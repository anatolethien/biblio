import json
import mysql.connector
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder
import numpy as np


# Charger les profils utilisateurs à partir d'un fichier JSON
def charger_profils(fichier_json):
    with open(fichier_json, 'r') as file:
        return json.load(file)


# Connexion à la base de données SQL
def connexion_sql():
    return mysql.connector.connect(
        host="hostname",  # hostname a changer
        user="username",  # username a changer
        password="password",
        database="database_name"  # nom de la BDD
    )

# Préparation des données pour la similarité cosinus
def preparer_donnees(profils):
    # Extraction des données catégorielles
    donnees_cat = [[profil['genre'], profil['profession'], profil['religion'], profil['MBTI']] for profil in profils]

    # Encodage one-hot des données catégorielles
    encoder = OneHotEncoder(sparse=False)
    donnees_cat_encoded = encoder.fit_transform(donnees_cat)

    # Création des vecteurs de données
    vecteurs = []
    for i, profil in enumerate(profils):
        vecteur = [
            profil['âge'],
            # Ajoutez d'autres caractéristiques numériques ici si nécessaire
        ]
        vecteur.extend(donnees_cat_encoded[i])
        vecteurs.append(vecteur)

    return np.array(vecteurs)


# Trouver des utilisateurs avec des profils similaires
def trouver_similaires(profil_cible, tous_les_profils):
    vecteurs = preparer_donnees(tous_les_profils)
    index_cible = tous_les_profils.index(profil_cible)
    similarites = cosine_similarity([vecteurs[index_cible]], vecteurs)
    scores = similarites[0]
    meilleurs_scores = np.argsort(scores)[::-1][1:]  # Ignorer le score du profil cible lui-même
    return [tous_les_profils[i] for i in meilleurs_scores if scores[i] > 0.5]  # Seuil de similarité


# Suggérer des livres (fonction inchangée)
def suggerer_livres(profil_utilisateur, tous_les_profils):


def suggerer_livres(profil_utilisateur, tous_les_profils):
    utilisateurs_similaires = trouver_similaires(profil_utilisateur, tous_les_profils)
    suggestions = []
    connexion = connexion_sql()
    cursor = connexion.cursor()

    for utilisateur in utilisateurs_similaires:
        query = "SELECT livre FROM inventaire_livres WHERE utilisateur_id = %s"
        cursor.execute(query, (utilisateur['id'],))
        for (livre,) in cursor:
            if livre not in suggestions:
                suggestions.append(livre)

    connexion.close()
    return suggestions


# Exemple d'utilisation (à adapter selon vos besoins)
fichier_json = "chemin/vers/le/fichier.json"
profils = charger_profils(fichier_json)
profil_utilisateur = profils[0]  # Exemple de sélection d'un utilisateur
suggestions = suggerer_livres(profil_utilisateur, profils)
print(suggestions)
