import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('Data/30.05_input.csv')

# Liste des champs à transformer
champs = ['Satisfaction Score']  # Remplacez par les noms de vos champs

# Fonction pour transformer les valeurs en {score=valeur} et les convertir en minuscules
def formatter_valeurs(df, champs):
    for champ in champs:
        df[champ] = df[champ].apply(lambda x: f"{{score={str(x).lower()}}}" if str(x).lower() != 'not offered' else '{score=unoffered}')
    return df

# Appliquer la fonction
df = formatter_valeurs(df, champs)

# Sauvegarder le DataFrame modifié dans un nouveau fichier JSON (optionnel)
df.to_json('Data/Correction-SatisfactionRating.json', index=False)

print(df)
