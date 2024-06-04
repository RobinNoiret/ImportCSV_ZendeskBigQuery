import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('Data/30.05_input.csv')

# Liste des champs à convertir
champs = ['Need partner training [flag]', 'Need customer training [flag]']

# Fonction pour convertir 'no' en 'false' et 'yes' en 'true'
def convertir_yes_no_en_bool(df, champs):
    for champ in champs:
        df[champ] = df[champ].replace({'no': 'false', 'yes': 'true'})
    return df

# Appliquer la fonction
df = convertir_yes_no_en_bool(df, champs)

# Sauvegarder le DataFrame modifié dans un nouveau fichier CSV (optionnel)
df.to_json('Data/Correction-Bool.json', index=False)

print(df)
