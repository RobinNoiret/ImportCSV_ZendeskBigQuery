import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('Data/30.05_input.csv')

# Liste des champs à nettoyer
champs = ['Product feedback status [list]', 'POD [list]', 'JIRA URL [txt]', 'Categories [list]']  # Remplacez par les noms de vos champs

# Fonction pour remplacer '-' par None
def remplacer_tiret_par_null(df, champs):
    for champ in champs:
        df[champ] = df[champ].replace('-', None)
    return df

# Appliquer la fonction
df = remplacer_tiret_par_null(df, champs)

# Sauvegarder le DataFrame modifié dans un nouveau fichier CSV (optionnel)
df.to_json('Data/correctionNull.json', index=False)

print(df)
