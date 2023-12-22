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
