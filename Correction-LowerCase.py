import pandas as pd

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('Data/30.05_input.csv')

# Liste des champs à convertir en minuscules
champs = ['Priority', 'Status', 'Ticket type', 'Severity [list]',]  # Remplacez par les noms de vos champs

# Fonction pour convertir en minuscules
def convertir_en_minuscules(df, champs):
    for champ in champs:
        df[champ] = df[champ].str.lower()
    return df

# Appliquer la fonction
df = convertir_en_minuscules(df, champs)

# Sauvegarder le DataFrame modifié dans un nouveau fichier CSV (optionnel)
df.to_json('Data/Correction-LowerCase.json', index=False)

print(df)
