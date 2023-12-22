import numpy as np
import json
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# chemin du fichier json des users, à changer avc une bdd en prod
chemin_fichier = 'profils_utilisateurs.json'

# Charger les profils depuis le fichier JSON
with open(chemin_fichier, 'r') as fichier:
    profils = json.load(fichier)

# traitement des données

encoder = OneHotEncoder(sparse=False)
donnees_cat = [[profil['genre'], profil['profession'], profil['âge'], profil['MBTI']] for profil in profils]
donnees_cat_encoded = encoder.fit_transform(donnees_cat)

# Créer des vecteurs pour la similarité cosinus
vecteurs = []
for i, profil in enumerate(profils):
    vecteur = [profil['âge']]
    vecteur.extend(donnees_cat_encoded[i])
    vecteurs.append(vecteur)


# Fonction pour trouver des profils similaires
def trouver_similaires(profil_index, vecteurs, top_n=5):
    profil_cible = vecteurs[profil_index]
    similarites = cosine_similarity([profil_cible], vecteurs)[0]
    indices_similaires = np.argsort(similarites)[::-1][1:top_n+1]  # Ignorer le premier élément (profil lui-même)
    return indices_similaires

# Exemple d'utilisation
index_profil_cible = 87  # Index test
indices_similaires = trouver_similaires(index_profil_cible, vecteurs)
print("Profils similaires à l'index", index_profil_cible, ":", indices_similaires)

