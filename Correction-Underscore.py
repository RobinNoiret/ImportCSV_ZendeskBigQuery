import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('Data/30.05_input.csv')

# Liste des champs à convertir
champs = ['Level [list]', 'Type (custom) [list]']  # Remplacez par les noms de vos champs

# Fonction pour convertir en minuscules et remplacer les espaces par des underscores
def convertir_format(df, champs):
    for champ in champs:
        df[champ] = df[champ].str.lower().str.replace(' ', '_')
    return df

# Appliquer la fonction
df = convertir_format(df, champs)

# Sauvegarder le DataFrame modifié dans un nouveau fichier CSV (optionnel)
df.to_json('Data/Correction-Underscore.json', index=False)

print(df)
