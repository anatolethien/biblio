import json
import random

def generer_type_mbti():
    types_mbti = [
        'INTJ', 'INTP', 'ENTJ', 'ENTP',
        'INFJ', 'INFP', 'ENFJ', 'ENFP',
        'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
        'ISTP', 'ISFP', 'ESTP', 'ESFP'
    ]
    return random.choice(types_mbti)
def generer_profil():
    genres = ['Femme', 'Homme', 'Non-binaire']
    professions = ['Enseignant', 'Ingénieur', 'Médecin', 'Artiste', 'Étudiant']
    lieux = ['Paris', 'Lyon', 'Marseille', 'Bordeaux', 'Lille']
    langues = ['Français', 'Anglais', 'Espagnol', 'Allemand', 'Italien']


    profil = {
        'genre': random.choice(genres),
        'âge': random.randint(18, 70),
        'profession': random.choice(professions),
        'lieu de naissance': random.choice(lieux),
        'lieu de résidence': random.choice(lieux),
        'langues parlées': random.sample(langues, k=random.randint(1, 3)),
        'MBTI': generer_type_mbti()
    }
    return profil

def creer_base_de_donnees_json(nombre_de_profils, fichier_sortie):
    profils = [generer_profil() for _ in range(nombre_de_profils)]

    with open(fichier_sortie, 'w') as fichier:
        json.dump(profils, fichier, indent=4, ensure_ascii=False)

# Générer une base de données JSON avec 100 profils
creer_base_de_donnees_json(100, 'profils_utilisateurs.json')
